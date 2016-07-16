"""
SceneCommandsTest class. Part of the StoryTechnologies Builder project.

July 16, 2016
Brett Alistair Kromkamp (brett.kromkamp@gmail.com)
"""

import unittest
import os.path

from engine.core.commands.scene.initscene import InitSceneCommand
from engine.core.commands.scene.addpath import AddPathCommand
from engine.core.commands.scene.addprop import AddPropCommand
from engine.core.commands.scene.addcharacter import AddCharacterCommand


class SceneCommandsTest(unittest.TestCase):

    def setUp(self):
        self.database_path = '/home/brettk/Source/storytechnologies/story-engine/topics.db'

    def testInitSceneCommand(self):
        pass

    def testAddPathCommand(self):
        pass

    def testAddPropCommand(self):
        pass

    def testAddCharacterCommand(self):
        pass

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
