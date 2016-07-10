"""
PutOccurrenceDataCommand class. Part of the StoryTechnologies Builder project.

July 04, 2016
Brett Alistair Kromkamp (brett.kromkamp@gmail.com)
"""

import sqlite3

from engine.store.topicstoreexception import TopicStoreException


class PutOccurrenceDataCommand:
    def __init__(self, database_path, identifier='', resource_data=None):
        self.database_path = database_path
        self.identifier = identifier
        self.resource_data = resource_data

    def do(self):
        if self.identifier is '' or self.resource_data is None:
            raise TopicStoreException("Missing 'identifier' and/or 'resource data' parameters")

        connection = sqlite3.connect(self.database_path)
        connection.row_factory = sqlite3.Row

        cursor = connection.cursor()
        try:
            cursor.execute("UPDATE occurrence SET resource_data = ? WHERE identifier = ?", (self.resource_data, self.identifier))
        except sqlite3.Error as e:
            raise TopicStoreException(e)
        finally:
            if cursor:
                cursor.close()
            if connection:
                connection.close()
