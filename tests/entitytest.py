"""
EntityTest class. Part of the StoryTechnologies Builder project.

July 03, 2016
Brett Alistair Kromkamp (brett.kromkamp@gmail.com)
"""

import unittest

from engine.store.models.entity import Entity


class EntityTest(unittest.TestCase):

    def setUp(self):
        self.entity1 = Entity('identifier-1')

    def testInit(self):
        self.assertEqual('identifier-1', self.entity1.identifier)
        self.assertEqual('entity', self.entity1.instance_of)

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
