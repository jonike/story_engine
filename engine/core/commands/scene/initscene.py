"""
InitSceneCommand class. Part of the StoryTechnologies Builder project.

July 16, 2016
Brett Alistair Kromkamp (brett.kromkamp@gmail.com)
"""

from engine.store.models.topic import Topic
from engine.store.models.occurrence import Occurrence
from engine.store.models.metadatum import Metadatum
from engine.core.models.scene import Scene
from engine.core.coreexception import CoreException


class InitSceneCommand:

    def __init__(self, database_path, scene):
        self.database_path = database_path
        self.scene = scene

    def do(self):
        if self.scene is None:
            raise CoreException("Missing 'scene' parameter")
