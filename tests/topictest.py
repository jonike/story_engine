"""
TopicTest class. Part of the StoryTechnologies Builder project.

July 03, 2016
Brett Alistair Kromkamp (brett.kromkamp@gmail.com)
"""

import unittest

from engine.store.models.topic import Topic


class TopicTest(unittest.TestCase):

    def setUp(self):
        self.topic1 = Topic()

    def testInit(self):
        self.assertEqual('Undefined', self.topic1.first_base_name.name)
        self.assertEqual('topic', self.topic1.instance_of)

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
