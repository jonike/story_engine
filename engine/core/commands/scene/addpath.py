"""
AddPathCommand class. Part of the StoryTechnologies Builder project.

July 16, 2016
Brett Alistair Kromkamp (brett.kromkamp@gmail.com)
"""

from engine.core.commands.scene.sceneexception import SceneException


class AddPathCommand:

    def __init__(self, database_path, scene=None):
        self.database_path = database_path
        self.scene = scene

    def do(self):
        if self.scene is None:
            raise SceneException("Missing 'scene' parameter")
