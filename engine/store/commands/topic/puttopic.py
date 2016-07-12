"""
PutTopicCommand class. Part of the StoryTechnologies Builder project.

July 12, 2016
Brett Alistair Kromkamp (brett.kromkamp@gmail.com)
"""

import sqlite3

from datetime import datetime

from engine.store.models.basename import BaseName
from engine.store.models.language import Language
from engine.store.models.topic import Topic
from engine.store.topicstoreexception import TopicStoreException


class PutTopicCommand:

    def __init__(self, database_path, topic=None, language=Language.en):
        self.database_path = database_path
        self.topic = topic
        self.language = language

    def do(self):
        if self.topic is None:
            raise TopicStoreException("Missing 'topic' parameter")
        result = None

        connection = sqlite3.connect(self.database_path)
        connection.row_factory = sqlite3.Row

        try:
            with connection:  # https://docs.python.org/3/library/sqlite3.html#using-the-connection-as-a-context-manager
                connection.execute("INSERT INTO topic (identifier, instance_of) VALUES (?, ?)", (self.topic.identifier, self.topic.instance_of))
                for base_name in self.topic.base_names:
                    connection.execute("INSERT INTO basename (identifier, name, topic_identifier_fk, language) VALUES (?, ?, ?, ?)", (base_name.identifier, base_name.name, self.topic.identifier, base_name.language))
        except sqlite3.Error as e:
            raise TopicStoreException(e)
        finally:
            if connection:
                connection.close()