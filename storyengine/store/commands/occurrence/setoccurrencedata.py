"""
SetOccurrenceData class. Part of the StoryTechnologies Builder project.

July 04, 2016
Brett Alistair Kromkamp (brett.kromkamp@gmail.com)
"""

import sqlite3

from storyengine.store.topicstoreexception import TopicStoreException


class SetOccurrenceData:
    def __init__(self, database_path, identifier='', resource_data=None):
        self.database_path = database_path
        self.identifier = identifier
        self.resource_data = bytes(resource_data, 'utf-8')

    def do(self):
        if self.identifier == '' or self.resource_data is None:
            raise TopicStoreException("Missing 'identifier' and/or 'resource data' parameters")

        connection = sqlite3.connect(self.database_path)

        try:
            with connection:
                connection.execute("UPDATE occurrence SET resource_data = ? WHERE identifier = ?", (self.resource_data, self.identifier))
        except sqlite3.Error as e:
            raise TopicStoreException(e)
        finally:
            if connection:
                connection.close()
