"""
DeleteOccurrencesCommand class. Part of the StoryTechnologies Builder project.

July 13, 2016
Brett Alistair Kromkamp (brett.kromkamp@gmail.com)
"""

import sqlite3

from engine.store.topicstoreexception import TopicStoreException


class DeleteOccurrencesCommand:

    def __init__(self, database_path, topic_identifier=''):
        self.database_path = database_path
        self.topic_identifier = topic_identifier

    def do(self):
        if self.topic_identifier == '':
            raise TopicStoreException("Missing 'topic identifier' parameter")

        connection = sqlite3.connect(self.database_path)

        try:
            with connection:  # https://docs.python.org/3/library/sqlite3.html#using-the-connection-as-a-context-manager
                connection.execute("DELETE FROM occurrence WHERE topic_identifier_fk = ?", (self.topic_identifier,))
        except sqlite3.Error as e:
            raise TopicStoreException(e)
        finally:
            if connection:
                connection.close()