"""
SetNavigation class. Part of the StoryTechnologies project.

July 16, 2016
Brett Alistair Kromkamp (brett.kromkamp@gmail.com)
"""

from topicmapengine.core.models.association import Association
from storyengine.core.coreerror import CoreError
from topicmapengine.core.commands.association.setassociation import SetAssociation


class SetNavigation:

    def __init__(self, database_path, map_identifier,
                 src_scene_identifier='',
                 dest_scene_identifier='',
                 src_scene_role='previous',
                 dest_scene_role='next'):
        self.database_path = database_path
        self.map_identifier = map_identifier
        self.src_scene_identifier = src_scene_identifier
        self.dest_scene_identifier = dest_scene_identifier
        self.src_scene_role = src_scene_role
        self.dest_scene_role = dest_scene_role

    def execute(self):
        if self.src_scene_identifier == '' or self.dest_scene_identifier == '':
            raise CoreError("Missing 'source scene' or 'destination scene' parameter")
        association = Association(
            instance_of='navigation',
            src_topic_ref=self.src_scene_identifier,
            dest_topic_ref=self.dest_scene_identifier,
            src_role_spec=self.src_scene_role,
            dest_role_spec=self.dest_scene_role)
        SetAssociation(self.database_path, self.map_identifier, association).execute()
