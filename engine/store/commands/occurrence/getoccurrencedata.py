"""
GetOccurrenceData class. Part of the StoryTechnologies Builder project.

July 04, 2016
Brett Alistair Kromkamp (brett.kromkamp@gmail.com)
"""

import sqlite3

from engine.store.topicstoreexception import TopicStoreException


class GetOccurrenceData:

    def __init__(self, database_path, identifier=''):
        self.database_path = database_path
        self.identifier = identifier

    def do(self):
        if self.identifier == '':
            raise TopicStoreException("Missing 'identifier' parameter")
        result = None

        connection = sqlite3.connect(self.database_path)
        connection.row_factory = sqlite3.Row

        cursor = connection.cursor()
        try:
            cursor.execute("SELECT resource_data FROM occurrence WHERE identifier = ?", (self.identifier,))
            record = cursor.fetchone()
            if record:
                result = record['resource_data']
        except sqlite3.Error as e:
            raise TopicStoreException(e)
        finally:
            if cursor:
                cursor.close()
            if connection:
                connection.close()
        return result
