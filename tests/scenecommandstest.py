"""
SceneCommandsTest class. Part of the StoryTechnologies Builder project.

July 16, 2016
Brett Alistair Kromkamp (brett.kromkamp@gmail.com)
"""

import unittest

from engine.core.commands.scene.initscene import InitSceneCommand
from engine.core.commands.scene.addnavigation import AddNavigationCommand
from engine.core.commands.scene.addprop import AddPropCommand
from engine.core.commands.scene.addcharacter import AddCharacterCommand


class SceneCommandsTest(unittest.TestCase):

    def setUp(self):
        self.database_path = '/home/brettk/Source/storytechnologies/story-engine/topics.db'

    def testInitSceneCommand(self):
        pass

    def testAddNavigationCommand(self):
        pass

    def testAddPropCommand(self):
        pass

    def testAddCharacterCommand(self):
        pass

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
