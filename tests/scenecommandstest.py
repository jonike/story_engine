"""
ScenesTest class. Part of the StoryTechnologies Builder project.

July 16, 2016
Brett Alistair Kromkamp (brett.kromkamp@gmail.com)
"""

import unittest

from storyengine.core.commands.scene.setscene import SetScene
from storyengine.core.commands.scene.setnavigation import SetNavigation
from storyengine.core.commands.scene.setprop import SetProp
from storyengine.core.commands.scene.setcharacter import SetCharacter
from storyengine.core.commands.scene.getscene import GetScene
from storyengine.core.models.character import Character
from storyengine.core.models.prop import Prop
from storyengine.core.models.scene import Scene
from storyengine.core.models.asset import Asset
from storyengine.store.commands.topic.topicexists import TopicExists


class ScenesTest(unittest.TestCase):

    def setUp(self):
        self.database_path = '/home/brettk/Source/storytechnologies/story-engine/data/test1.sqlite'

    def testScenes(self):
        pass

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
