"""
GetSceneCommand class. Part of the StoryTechnologies Builder project.

July 19, 2016
Brett Alistair Kromkamp (brett.kromkamp@gmail.com)
"""

from engine.core.coreexception import CoreException


class GetSceneCommand:
    def __init__(self, database_path, scene_identifier=''):
        self.database_path = database_path
        self.scene_identifier = scene_identifier

    def do(self):
        if self.scene_identifier == '':
            raise CoreException("Missing 'scene identifier' parameter")
