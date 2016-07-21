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
from engine.core.models.scene import Scene
from engine.core.models.asset import Asset
from engine.store.commands.topic.topicexists import TopicExistsCommand


class SceneCommandsTest(unittest.TestCase):

    def setUp(self):
        self.database_path = '/home/brettk/Source/storytechnologies/story-engine/topics.db'

    def testInitSceneCommand(self):
        asset1 = Asset('/home/brettk/Videos/windmill1.gif', 'image')
        asset2 = Asset('/home/brettk/Videos/robot7.mp4', 'video')
        asset3 = Asset('/home/brettk/Source/blender/blend4web/robot-b4w5.html', 'html')

        scene1 = Scene('scene-001', 'Test Scene 001', 1)
        scene1.add_assets([asset1, asset2, asset3])
        InitSceneCommand(self.database_path, scene1).do()

        asset4 = Asset('/home/brettk/Source/blender/blend4web/church-b4w.html', 'html')

        scene2 = Scene('scene-002', 'Test Scene 002', 2)
        scene2.add_asset(asset4)
        InitSceneCommand(self.database_path, scene2).do()

        self.assertTrue(True, TopicExistsCommand(self.database_path, 'scene-001').do())
        self.assertTrue(True, TopicExistsCommand(self.database_path, 'scene-002').do())

    def testAddNavigationCommand(self):
        pass

    def testAddPropCommand(self):
        pass

    def testAddCharacterCommand(self):
        pass

    def testGetSceneCommand(self):
        pass

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
