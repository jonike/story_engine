"""
TopicStoreTest class. Part of the StoryTechnologies Builder project.

July 03, 2016
Brett Alistair Kromkamp (brett.kromkamp@gmail.com)
"""

import unittest

from engine.store.commands.topic.topicexists import TopicExistsCommand
from engine.store.commands.topic.gettopic import GetTopicCommand
from engine.store.commands.metadatum.getmetadatum import GetMetadatumCommand
from engine.store.retrievaloption import RetrievalOption


class TopicStoreTest(unittest.TestCase):

    def setUp(self):
        self.database_path = '/home/brettk/Source/storytechnologies/story-engine/topics.db'

    def testTopicExistsCommand(self):
        topic_exists_command = self.topic_exists_command = TopicExistsCommand(self.database_path)

        topic_exists_command.identifier = 'frontpage'
        existing_topic = topic_exists_command.execute()

        topic_exists_command.identifier = 'non-existing-topic'
        non_existing_topic = topic_exists_command.execute()

        self.assertEqual(True, existing_topic)
        self.assertEqual(False, non_existing_topic)

    def testGetTopicCommand(self):
        get_topic_command = GetTopicCommand(self.database_path, 'frontpage', RetrievalOption.resolve_metadata)

        topic1 = get_topic_command.execute()

        self.assertEqual('Front Page', topic1.first_base_name.name)
        self.assertEqual('frontpage', topic1.identifier)
        self.assertEqual('topic', topic1.instance_of)

        self.assertLess(0, len(topic1.metadata))

        for metadatum in topic1.metadata:
            print("Name: {0}, Value: {1}, Identifier: {2}".format(metadatum.name, metadatum.value, metadatum.identifier))

    def testGetMetadatumCommand(self):
        metadatum1 = GetMetadatumCommand(self.database_path, '89d9bd44-b252-469d-b377-f07c73c24269').execute()

        self.assertEqual('creation-timestamp', metadatum1.name)
        self.assertEqual('2015/02/21 09:21:00', metadatum1.value)
        self.assertEqual('89d9bd44-b252-469d-b377-f07c73c24269', metadatum1.identifier)

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
