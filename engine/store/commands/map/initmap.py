"""
InitMapCommand class. Part of the StoryTechnologies Builder project.

July 16, 2016
Brett Alistair Kromkamp (brett.kromkamp@gmail.com)
"""

import sqlite3

from engine.store.models.topic import Topic
from engine.store.topicstoreexception import TopicStoreException
from engine.store.commands.topic.puttopic import PutTopicCommand
from engine.store.commands.map.topicfield import TopicField


class InitMapCommand:

    def __init__(self, database_path):
        self.database_path = database_path
        self.items = {
            ('entity', 'Entity'),
            ('topic', 'Topic'),
            ('association', 'Association'),
            ('occurrence', 'Occurrence'),
            ('*', 'Universal Scope'),
            ('genesis', 'Genesis'),
            ('navigation', 'Navigation'),
            ('categorization', 'Categorization'),
            ('related', 'Related'),
            ('parent', 'Parent'),
            ('child', 'Child'),
            ('previous', 'Previous'),
            ('next', 'Next'),
            ('story', 'Story'),
            ('book', 'Book'),
            ('chapter', 'Chapter'),
            ('scene', 'Scene'),
            ('environment', 'Environment'),
            ('prop', 'Prop'),
            ('character', 'Character'),
            ('north', 'North'),
            ('north-east', 'Northeast'),
            ('east', 'East'),
            ('south-east', 'Southeast'),
            ('south', 'South'),
            ('south-west', 'Southwest'),
            ('west', 'West'),
            ('north-west', 'Northwest')
        }

    def do(self):

        put_topic_command = PutTopicCommand(self.database_path)
        for item in self.items:
            topic = Topic(identifier=item[TopicField.identifier.value], base_name=item[TopicField.base_name.value])
            put_topic_command.topic = topic
            put_topic_command.do()
