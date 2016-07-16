"""
CommandsTest class. Part of the StoryTechnologies Builder project.

July 03, 2016
Brett Alistair Kromkamp (brett.kromkamp@gmail.com)
"""

import unittest

from engine.store.commands.topic.topicexists import TopicExistsCommand
from engine.store.commands.occurrence.occurrenceexists import OccurrenceExistsCommand
from engine.store.commands.topic.gettopic import GetTopicCommand
from engine.store.commands.metadatum.getmetadatum import GetMetadatumCommand
from engine.store.commands.metadatum.putmetadatum import PutMetadatumCommand
from engine.store.commands.occurrence.getoccurrence import GetOccurrenceCommand
from engine.store.commands.topic.puttopic import PutTopicCommand
from engine.store.retrievaloption import RetrievalOption
from engine.store.models.language import Language
from engine.store.models.datatype import DataType
from engine.store.models.topic import Topic
from engine.store.models.metadatum import Metadatum


class StoreCommandsTest(unittest.TestCase):

    def setUp(self):
        self.database_path = '/home/brettk/Source/storytechnologies/story-engine/topics.db'

    def testTopicExistsCommand(self):
        topic_identifier = 'genesis'
        topic_exists = TopicExistsCommand(self.database_path, topic_identifier).do()
        if not topic_exists:
            topic1 = Topic(topic_identifier, 'topic', 'Genesis')
            PutTopicCommand(self.database_path, topic1).do()

        topic_exists_command = TopicExistsCommand(self.database_path)

        topic_exists_command.identifier = 'genesis'
        existing_topic = topic_exists_command.do()

        topic_exists_command.identifier = 'non-existing-topic'
        non_existing_topic = topic_exists_command.do()

        self.assertEqual(True, existing_topic)
        self.assertEqual(False, non_existing_topic)

    def testGetTopicCommand(self):
        topic_identifier = 'genesis'
        topic_exists = TopicExistsCommand(self.database_path, topic_identifier).do()
        if not topic_exists:
            topic1 = Topic(topic_identifier, 'topic', 'Genesis')
            PutTopicCommand(self.database_path, topic1).do()

        get_topic_command = GetTopicCommand(self.database_path, 'genesis', RetrievalOption.resolve_metadata)

        topic1 = get_topic_command.do()

        self.assertEqual('Genesis', topic1.first_base_name.name)
        self.assertEqual('genesis', topic1.identifier)
        self.assertEqual('topic', topic1.instance_of)

        self.assertLess(0, len(topic1.metadata))

    # def testGetMetadatumCommand(self):
    #     metadatum1 = GetMetadatumCommand(self.database_path, '89d9bd44-b252-469d-b377-f07c73c24269').do()
    #
    #     self.assertEqual('creation-timestamp', metadatum1.name)
    #     self.assertEqual('2015/02/21 09:21:00', metadatum1.value)
    #     self.assertEqual('89d9bd44-b252-469d-b377-f07c73c24269', metadatum1.identifier)
    #
    # def testGetOccurrenceCommand(self):
    #     occurrence1 = GetOccurrenceCommand(self.database_path,
    #                                        '59124c31-22ad-4f17-ba4b-1a03bb69cb2d',
    #                                        RetrievalOption.inline_resource_data,
    #                                        RetrievalOption.resolve_metadata).do()
    #
    #     self.assertEqual('59124c31-22ad-4f17-ba4b-1a03bb69cb2d', occurrence1.identifier)
    #     self.assertEqual('note', occurrence1.instance_of)
    #     self.assertEqual('*', occurrence1.scope)
    #     self.assertEqual(Language.en, occurrence1.language)
    #     self.assertEqual(b"I'm a note for the test topic", occurrence1.resource_data)
    #
    # def testOccurrenceExistsCommand(self):
    #     occurrence_exists_command = OccurrenceExistsCommand(self.database_path)
    #
    #     occurrence_exists_command.identifier = '59124c31-22ad-4f17-ba4b-1a03bb69cb2d'
    #     existing_occurrence = occurrence_exists_command.do()
    #
    #     occurrence_exists_command.identifier = 'non-existing-occurrence'
    #     non_existing_occurrence = occurrence_exists_command.do()
    #
    #     self.assertEqual(True, existing_occurrence)
    #     self.assertEqual(False, non_existing_occurrence)

    def testPutTopicCommand(self):
        topic_identifier = 'test-topic2'
        topic_exists = TopicExistsCommand(self.database_path, topic_identifier).do()
        if not topic_exists:
            topic1 = Topic(topic_identifier, 'topic', 'Test Topic')
            PutTopicCommand(self.database_path, topic1).do()

        topic2 = GetTopicCommand(self.database_path, topic_identifier, RetrievalOption.resolve_metadata).do()

        self.assertEqual('Test Topic', topic2.first_base_name.name)
        self.assertEqual(topic_identifier, topic2.identifier)
        self.assertEqual('topic', topic2.instance_of)

    def testPutMetadatum(self):
        metadatum_name = 'metadatum-name'
        metadatum1 = Metadatum(metadatum_name, 'metadatum-value', 'genesis', data_type=DataType.string, scope='test', language=Language.es)
        PutMetadatumCommand(self.database_path, metadatum1).do()

        metadatum2 = GetMetadatumCommand(self.database_path, metadatum1.identifier).do()

        self.assertEqual('metadatum-name', metadatum2.name)
        self.assertEqual('metadatum-value', metadatum2.value)
        self.assertEqual(metadatum2.identifier, metadatum1.identifier)

    def testPutOccurrence(self):
        pass

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
