"""
MapsTest class. Part of the StoryTechnologies Builder project.

July 03, 2016
Brett Alistair Kromkamp (brett.kromkamp@gmail.com)
"""

import unittest
import os.path

from storyengine.store.commands.map.createmap import CreateMap
from storyengine.store.commands.map.initmap import InitMap
from storyengine.store.commands.topic.topicexists import TopicExists


class MapsTest(unittest.TestCase):

    def setUp(self):
        self.database_path = '/home/brettk/Source/storytechnologies/story-storyengine/data/test1.sqlite'

    def testMaps(self):
        if not os.path.isfile(self.database_path):
            create_map_command = CreateMap(self.database_path)
            create_map_command.do()

        self.assertEqual(True, os.path.isfile(self.database_path))

        if not TopicExists(self.database_path, 'genesis').do():
            InitMap(self.database_path).do()

        self.assertEqual(True, TopicExists(self.database_path, 'genesis').do())

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
