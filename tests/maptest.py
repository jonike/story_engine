"""
MapTest class. Part of the StoryTechnologies project.

July 03, 2016
Brett Alistair Kromkamp (brett.kromkamp@gmail.com)
"""

import unittest
import os.path

from storyengine.store.commands.map.createmap import CreateMap
from storyengine.store.commands.map.initmap import InitMap
from storyengine.store.commands.topic.topicexists import TopicExists


class MapTest(unittest.TestCase):

    def setUp(self):
        self.database_path = '/home/brettk/Source/storytechnologies/story_engine/data/storytech.sqlite'
        self.map_identifier = 1

    def testMaps(self):
        if not os.path.isfile(self.database_path):
            create_map_command = CreateMap(self.database_path)
            create_map_command.execute()

        self.assertEqual(True, os.path.isfile(self.database_path))

        if not TopicExists(self.database_path, self.map_identifier, 'genesis').execute():
            InitMap(self.database_path, self.map_identifier).execute()

        self.assertEqual(True, TopicExists(self.database_path, self.map_identifier, 'genesis').execute())

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
