"""
TopicStoreTest class. Part of the StoryTechnologies Builder project.

July 03, 2016
Brett Alistair Kromkamp (brett.kromkamp@gmail.com)
"""

import unittest

from engine.topicmap.topicstore import TopicStore


class TopicStoreTest(unittest.TestCase):

    def setUp(self):
        self.topic_store = TopicStore()
        self.topic_store.open('/home/brettk/Source/storytechnologies/story-engine/topics.db')

    def testInit(self):
        topic1 = self.topic_store.get_topic('frontpage')

        self.assertEqual('Front Page', topic1.first_base_name.name)
        self.assertEqual('frontpage', topic1.identifier)
        self.assertEqual('topic', topic1.instance_of)

        metadata1 = self.topic_store.get_metadata('frontpage')

        self.assertLess(0, len(metadata1))

        for metadatum in metadata1:
            print("Name: {0}, Value: {1}".format(metadatum.name, metadatum.value))

    def tearDown(self):
        self.topic_store.close()

if __name__ == '__main__':
    unittest.main()