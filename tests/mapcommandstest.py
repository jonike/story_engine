"""
MapCommandsTest class. Part of the StoryTechnologies Builder project.

July 03, 2016
Brett Alistair Kromkamp (brett.kromkamp@gmail.com)
"""

import unittest
import os.path

from engine.store.commands.map.createmap import CreateMapCommand


class MapCommandsTest(unittest.TestCase):

    def setUp(self):
        self.database_path = '/home/brettk/Source/storytechnologies/story-engine/topics.db'

    def testCreateMapCommand(self):
        create_map_command = CreateMapCommand(self.database_path)
        create_map_command.do()

        self.assertEqual(True, os.path.isfile(self.database_path))

    def testInitMapCommand(self):
        pass

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
