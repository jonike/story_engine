"""
DeleteAttributes class. Part of the StoryTechnologies project.

July 13, 2016
Brett Alistair Kromkamp (brett.kromkamp@gmail.com)
"""

import sqlite3

from storyengine.store.topicstoreexception import TopicStoreException


class DeleteAttributes:

    def __init__(self, database_path, map_identifier, entity_identifier=''):
        self.database_path = database_path
        self.map_identifier = map_identifier
        self.entity_identifier = entity_identifier

    def do(self):
        if self.entity_identifier == '':
            raise TopicStoreException("Missing 'entity identifier' parameter")

        connection = sqlite3.connect(self.database_path)

        try:
            with connection:  # https://docs.python.org/3/library/sqlite3.html#using-the-connection-as-a-context-manager
                connection.execute("DELETE FROM attribute WHERE topicmap_identifier = ? AND parent_identifier_fk = ?", (self.map_identifier, self.entity_identifier))
        except sqlite3.Error as e:
            raise TopicStoreException(e)
        finally:
            if connection:
                connection.close()
