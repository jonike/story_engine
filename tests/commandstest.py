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
from engine.store.commands.occurrence.getoccurrence import GetOccurrenceCommand
from engine.store.retrievaloption import RetrievalOption
from engine.store.models.language import Language


class CommandsTest(unittest.TestCase):

    def setUp(self):
        self.database_path = '/home/brettk/Source/storytechnologies/story-engine/topics.db'

    def testTopicExistsCommand(self):
        topic_exists_command = TopicExistsCommand(self.database_path)

        topic_exists_command.identifier = 'frontpage'
        existing_topic = topic_exists_command.do()

        topic_exists_command.identifier = 'non-existing-topic'
        non_existing_topic = topic_exists_command.do()

        self.assertEqual(True, existing_topic)
        self.assertEqual(False, non_existing_topic)

    def testGetTopicCommand(self):
        get_topic_command = GetTopicCommand(self.database_path, 'frontpage', RetrievalOption.resolve_metadata)

        topic1 = get_topic_command.do()

        self.assertEqual('Front Page', topic1.first_base_name.name)
        self.assertEqual('frontpage', topic1.identifier)
        self.assertEqual('topic', topic1.instance_of)

        self.assertLess(0, len(topic1.metadata))

    def testGetMetadatumCommand(self):
        metadatum1 = GetMetadatumCommand(self.database_path, '89d9bd44-b252-469d-b377-f07c73c24269').do()

        self.assertEqual('creation-timestamp', metadatum1.name)
        self.assertEqual('2015/02/21 09:21:00', metadatum1.value)
        self.assertEqual('89d9bd44-b252-469d-b377-f07c73c24269', metadatum1.identifier)

    def testGetOccurrenceCommand(self):
        occurrence1 = GetOccurrenceCommand(self.database_path,
                                           '59124c31-22ad-4f17-ba4b-1a03bb69cb2d',
                                           RetrievalOption.inline_resource_data,
                                           RetrievalOption.resolve_metadata).do()

        self.assertEqual('59124c31-22ad-4f17-ba4b-1a03bb69cb2d', occurrence1.identifier)
        self.assertEqual('note', occurrence1.instance_of)
        self.assertEqual('*', occurrence1.scope)
        self.assertEqual(Language.en, occurrence1.language)
        self.assertEqual(b"I'm a note for the test topic", occurrence1.resource_data)

    def testOccurrenceExistsCommand(self):
        occurrence_exists_command = OccurrenceExistsCommand(self.database_path)

        occurrence_exists_command.identifier = '59124c31-22ad-4f17-ba4b-1a03bb69cb2d'
        existing_occurrence = occurrence_exists_command.do()

        occurrence_exists_command.identifier = 'non-existing-occurrence'
        non_existing_occurrence = occurrence_exists_command.do()

        self.assertEqual(True, existing_occurrence)
        self.assertEqual(False, non_existing_occurrence)

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()