"""
ScenesTest class. Part of the StoryTechnologies Builder project.

July 16, 2016
Brett Alistair Kromkamp (brett.kromkamp@gmail.com)
"""

import unittest

from engine.core.commands.scene.setscene import SetScene
from engine.core.commands.scene.setnavigation import SetNavigation
from engine.core.commands.scene.setprop import SetProp
from engine.core.commands.scene.setcharacter import SetCharacter
from engine.core.commands.scene.getscene import GetScene
from engine.core.models.character import Character
from engine.core.models.prop import Prop
from engine.core.models.scene import Scene
from engine.core.models.asset import Asset
from engine.store.commands.topic.topicexists import TopicExists


class ScenesTest(unittest.TestCase):

    def setUp(self):
        self.database_path = '/home/brettk/Source/storytechnologies/story-engine/data/test1.sqlite'

    def testScenes(self):
        pass

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
