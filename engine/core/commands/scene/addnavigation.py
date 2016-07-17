"""
AddNavigationCommand class. Part of the StoryTechnologies Builder project.

July 16, 2016
Brett Alistair Kromkamp (brett.kromkamp@gmail.com)
"""

from engine.store.models.association import Association
from engine.core.coreexception import CoreException


class AddNavigationCommand:

    def __init__(self, database_path, src_scene='', dest_scene='', src_scene_role='previous', dest_scene_role='next'):
        self.database_path = database_path
        self.src_scene = src_scene
        self.dest_scene = dest_scene
        self.src_scene_role = src_scene_role
        self.dest_scene_role = dest_scene_role

    def do(self):
        if self.src_scene == '' or self.dest_scene == '':
            raise CoreException("Missing 'source scene' or 'destination scene' parameter")
