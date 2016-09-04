"""
SceneCommandsTest class. Part of the StoryTechnologies Builder project.

July 16, 2016
Brett Alistair Kromkamp (brett.kromkamp@gmail.com)
"""

import unittest

from engine.core.commands.scene.setscene import SetSceneCommand
from engine.core.commands.scene.setnavigation import SetNavigationCommand
from engine.core.commands.scene.setprop import SetPropCommand
from engine.core.commands.scene.setcharacter import SetCharacterCommand
from engine.core.commands.scene.getscene import GetSceneCommand
from engine.core.models.character import Character
from engine.core.models.prop import Prop
from engine.core.models.scene import Scene
from engine.core.models.asset import Asset
from engine.store.commands.topic.topicexists import TopicExistsCommand


class SceneCommandsTest(unittest.TestCase):

    def setUp(self):
        self.database_path = '/home/brettk/Source/storytechnologies/story-engine/data/test1.sqlite'

    def testSceneCommands(self):
        pass

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
