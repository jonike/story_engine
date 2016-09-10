"""
SetNavigation class. Part of the StoryTechnologies Builder project.

July 16, 2016
Brett Alistair Kromkamp (brett.kromkamp@gmail.com)
"""

from storyengine.store.models.association import Association
from storyengine.core.coreexception import CoreException
from storyengine.store.commands.association.setassociation import SetAssociation


class SetNavigation:

    def __init__(self, database_path,
                 src_scene_identifier='',
                 dest_scene_identifier='',
                 src_scene_role='previous',
                 dest_scene_role='next'):
        self.database_path = database_path
        self.src_scene_identifier = src_scene_identifier
        self.dest_scene_identifier = dest_scene_identifier
        self.src_scene_role = src_scene_role
        self.dest_scene_role = dest_scene_role

    def do(self):
        if self.src_scene_identifier == '' or self.dest_scene_identifier == '':
            raise CoreException("Missing 'source scene' or 'destination scene' parameter")
        association = Association(
            instance_of='navigation',
            src_topic_ref=self.src_scene_identifier,
            dest_topic_ref=self.dest_scene_identifier,
            src_role_spec=self.src_scene_role,
            dest_role_spec=self.dest_scene_role)
        SetAssociation(self.database_path, association).do()
