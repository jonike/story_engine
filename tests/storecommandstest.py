"""
sTest class. Part of the StoryTechnologies Builder project.

July 03, 2016
Brett Alistair Kromkamp (brett.kromkamp@gmail.com)
"""

import unittest

from engine.store.commands.topic.gettopics import GetTopics
from engine.store.commands.topic.topicexists import TopicExists
from engine.store.commands.occurrence.occurrenceexists import OccurrenceExists
from engine.store.commands.topic.gettopic import GetTopic
from engine.store.commands.metadatum.getmetadatum import GetMetadatum
from engine.store.commands.metadatum.setmetadatum import SetMetadatum
from engine.store.commands.occurrence.getoccurrence import GetOccurrence
from engine.store.commands.topic.settopic import SetTopic
from engine.store.retrievaloption import RetrievalOption
from engine.store.models.language import Language
from engine.store.models.datatype import DataType
from engine.store.models.topic import Topic
from engine.store.models.metadatum import Metadatum


class StoresTest(unittest.TestCase):

    def setUp(self):
        self.database_path = '/home/brettk/Source/storytechnologies/story-engine/data/test1.sqlite'

    def testTopicExists(self):
        topic_identifier = 'genesis'
        topic_exists = TopicExists(self.database_path, topic_identifier).do()
        if not topic_exists:
            topic1 = Topic(topic_identifier, 'topic', 'Genesis')
            SetTopic(self.database_path, topic1).do()

        topic_exists_command = TopicExists(self.database_path)

        topic_exists_command.identifier = 'genesis'
        existing_topic = topic_exists_command.do()

        topic_exists_command.identifier = 'non-existing-topic'
        non_existing_topic = topic_exists_command.do()

        self.assertEqual(True, existing_topic)
        self.assertEqual(False, non_existing_topic)

    def testGetTopic(self):
        topic_identifier = 'genesis'
        topic_exists = TopicExists(self.database_path, topic_identifier).do()
        if not topic_exists:
            topic1 = Topic(topic_identifier, 'topic', 'Genesis')
            SetTopic(self.database_path, topic1).do()

        get_topic_command = GetTopic(self.database_path, 'genesis', RetrievalOption.resolve_metadata)

        topic1 = get_topic_command.do()

        self.assertEqual('Genesis', topic1.first_base_name.name)
        self.assertEqual('genesis', topic1.identifier)
        self.assertEqual('topic', topic1.instance_of)

        self.assertLess(0, len(topic1.metadata))

    # def testSetTopic(self):
    #     topic_identifier = 'test-topic2'
    #     topic_exists = TopicExists(self.database_path, topic_identifier).do()
    #     if not topic_exists:
    #         topic1 = Topic(topic_identifier, 'topic', 'Test Topic')
    #         SetTopic(self.database_path, topic1).do()
    #
    #     topic2 = GetTopic(self.database_path, topic_identifier, RetrievalOption.resolve_metadata).do()
    #
    #     self.assertEqual('Test Topic', topic2.first_base_name.name)
    #     self.assertEqual(topic_identifier, topic2.identifier)
    #     self.assertEqual('topic', topic2.instance_of)
    #
    # def testSetMetadatum(self):
    #     metadatum_name = 'metadatum-name'
    #     metadatum1 = Metadatum(metadatum_name, 'metadatum-value', 'genesis', data_type=DataType.string, scope='test', language=Language.es)
    #     SetMetadatum(self.database_path, metadatum1).do()
    #
    #     metadatum2 = GetMetadatum(self.database_path, metadatum1.identifier).do()
    #
    #     self.assertEqual('metadatum-name', metadatum2.name)
    #     self.assertEqual('metadatum-value', metadatum2.value)
    #     self.assertEqual(metadatum2.identifier, metadatum1.identifier)

    def testGetTopics(self):
        topics = GetTopics(self.database_path).do()

        self.assertEqual(40, len(topics))

    def testSetOccurrence(self):
        pass

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
