"""
StoreTest class. Part of the StoryTechnologies project.

July 03, 2016
Brett Alistair Kromkamp (brett.kromkamp@gmail.com)
"""

import unittest

from storyengine.store.commands.topic.gettopics import GetTopics
from storyengine.store.commands.topic.gettopicshierarchy import GetTopicsHierarchy
from storyengine.store.commands.topic.topicexists import TopicExists
from storyengine.store.commands.occurrence.occurrenceexists import OccurrenceExists
from storyengine.store.commands.topic.gettopic import GetTopic
from storyengine.store.commands.attribute.getattribute import GetAttribute
from storyengine.store.commands.attribute.setattribute import SetAttribute
from storyengine.store.commands.occurrence.getoccurrence import GetOccurrence
from storyengine.store.commands.topic.settopic import SetTopic
from storyengine.store.retrievaloption import RetrievalOption
from storyengine.store.models.language import Language
from storyengine.store.models.datatype import DataType
from storyengine.store.models.topic import Topic
from storyengine.store.models.attribute import Attribute


class StoreTest(unittest.TestCase):

    def setUp(self):
        self.database_path = '/home/brettk/Source/storytechnologies/story_engine/data/storytech.sqlite'
        self.map_identifier = 1

    def testTopicExists(self):
        topic_identifier = 'genesis'
        topic_exists = TopicExists(self.database_path, self.map_identifier, topic_identifier).execute()
        if not topic_exists:
            topic1 = Topic(topic_identifier, 'topic', 'Genesis')
            SetTopic(self.database_path, self.map_identifier, topic1).execute()

        topic_exists_command = TopicExists(self.database_path, self.map_identifier)

        topic_exists_command.identifier = 'genesis'
        existing_topic = topic_exists_command.execute()

        topic_exists_command.identifier = 'non-existing-topic'
        non_existing_topic = topic_exists_command.execute()

        self.assertEqual(True, existing_topic)
        self.assertEqual(False, non_existing_topic)

    def testGetTopic(self):
        topic_identifier = 'genesis'
        topic_exists = TopicExists(self.database_path, self.map_identifier, topic_identifier).execute()
        if not topic_exists:
            topic1 = Topic(topic_identifier, 'topic', 'Genesis')
            SetTopic(self.database_path, self.map_identifier, topic1).execute()

        get_topic_command = GetTopic(self.database_path, self.map_identifier, 'genesis', RetrievalOption.resolve_attributes)

        topic1 = get_topic_command.execute()

        self.assertEqual('Genesis', topic1.first_base_name.name)
        self.assertEqual('genesis', topic1.identifier)
        self.assertEqual('topic', topic1.instance_of)

        self.assertLess(0, len(topic1.attributes))

    def testGetTopicsHierarchy(self):
        tree = GetTopicsHierarchy(self.database_path, self.map_identifier, 'research-area').execute()
        tree.display('research-area')

    def testSetOccurrence(self):
        pass

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
