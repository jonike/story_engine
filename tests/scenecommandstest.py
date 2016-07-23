"""
SceneCommandsTest class. Part of the StoryTechnologies Builder project.

July 16, 2016
Brett Alistair Kromkamp (brett.kromkamp@gmail.com)
"""

import unittest

from engine.core.commands.scene.putscene import PutSceneCommand
from engine.core.commands.scene.putnavigation import PutNavigationCommand
from engine.core.commands.scene.putprop import PutPropCommand
from engine.core.commands.scene.putcharacter import PutCharacterCommand
from engine.core.commands.scene.getscene import GetSceneCommand
from engine.core.models.character import Character
from engine.core.models.prop import Prop
from engine.core.models.scene import Scene
from engine.core.models.asset import Asset
from engine.store.commands.topic.topicexists import TopicExistsCommand


class SceneCommandsTest(unittest.TestCase):

    def setUp(self):
        self.database_path = '/home/brettk/Source/storytechnologies/story-engine/topics.db'

    def testSceneCommands(self):
        asset1 = Asset('/home/brettk/Videos/windmill1.gif', 'image')
        asset2 = Asset('/home/brettk/Videos/robot7.mp4', 'video')
        asset3 = Asset('/home/brettk/Source/blender/blend4web/robot-b4w5.html', 'html')

        scene1 = Scene('scene-001', 'Test Scene 001', 1)
        scene1.add_assets([asset1, asset2, asset3])
        PutSceneCommand(self.database_path, scene1).do()

        asset4 = Asset('/home/brettk/Source/blender/blend4web/church-b4w.html', 'html')
        scene2 = Scene('scene-002', 'Test Scene 002', 2)
        scene2.add_asset(asset4)
        PutSceneCommand(self.database_path, scene2).do()

        self.assertTrue(True, TopicExistsCommand(self.database_path, 'scene-001').do())
        self.assertTrue(True, TopicExistsCommand(self.database_path, 'scene-002').do())

        PutNavigationCommand(self.database_path, 'scene-001', 'scene-002', 'south', 'north').do()

        prop1 = Prop('prop-001', 'Test Prop 001')
        prop1.location = '(1.0, 2.0, 3.0)'
        prop1.scale = '2.0'
        asset5 = Asset('/home/brettk/Source/blender/blend4web/outback-windmill-b4w2.html', 'html')
        prop1.add_asset(asset5)
        PutPropCommand(self.database_path, prop1, 'scene-001').do()

        character1 = Character('character-001', 'Test Character 001')
        character1.location = '(4.0, 5.0, 6.0)'
        asset6 = Asset('/home/brettk/Source/blender/blend4web/robot-b4w4.html', 'html')
        character1.add_asset(asset6)
        PutCharacterCommand(self.database_path, character1, 'scene-001').do()

        character2 = Character('character-002', 'Test Character 002')
        character2.location = '(7.0, 8.0, 9.0)'
        asset7 = Asset('/home/brettk/Source/blender/blend4web/me-b4w4.html', 'html')
        character2.add_asset(asset7)
        PutCharacterCommand(self.database_path, character2, 'scene-001').do()

        scene3 = GetSceneCommand(self.database_path, 'scene-001').do()
        self.assertEqual('Test Scene 001', scene3.name)
        self.assertEqual('(0.0, 0.0, 0.0)', scene3.location)
        self.assertEqual('(0.0, 0.0, 0.0)', scene3.rotation)
        self.assertEqual('1.0', scene3.scale)
        self.assertEqual('scene', scene3.instance_of)
        self.assertEqual('1', scene3.ordinal)

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
