"""
AddCharacterCommand class. Part of the StoryTechnologies Builder project.

July 16, 2016
Brett Alistair Kromkamp (brett.kromkamp@gmail.com)
"""

from engine.core.coreexception import CoreException


class AddCharacterCommand:
    def __init__(self, database_path, scene_identifier='', character=None):
        self.database_path = database_path
        self.scene_identifier = scene_identifier
        self.character = character

    def do(self):
        if self.scene_identifier == '' or self.prop is None:
            raise CoreException("Missing 'scene identifier' or 'character' parameter")
