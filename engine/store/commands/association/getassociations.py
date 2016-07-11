"""
GetAssociationsCommand class. Part of the StoryTechnologies Builder project.

July 10, 2016
Brett Alistair Kromkamp (brett.kromkamp@gmail.com)
"""

import sqlite3

from engine.store.topicstoreexception import TopicStoreException


class GetAssociationsCommand:

    def __init__(self, database_path, topic_identifier=''):
        self.database_path = database_path
        self.identifier = topic_identifier

    def do(self):
        if self.identifier == '':
            raise TopicStoreException("Missing 'topic identifier' parameter")
        result = False

        connection = sqlite3.connect(self.database_path)
        connection.row_factory = sqlite3.Row

        cursor = connection.cursor()
        try:
            pass
        except sqlite3.Error as e:
            raise TopicStoreException(e)
        finally:
            if cursor:
                cursor.close()
            if connection:
                connection.close()
        return result
