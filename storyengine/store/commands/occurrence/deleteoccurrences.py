"""
DeleteOccurrences class. Part of the StoryTechnologies project.

July 13, 2016
Brett Alistair Kromkamp (brett.kromkamp@gmail.com)
"""

import sqlite3

from storyengine.store.topicstoreexception import TopicStoreException
from storyengine.store.commands.occurrence.deleteoccurrence import DeleteOccurrence


class DeleteOccurrences:

    def __init__(self, database_path, map_identifier, topic_identifier=''):
        self.database_path = database_path
        self.map_identifier = map_identifier
        self.topic_identifier = topic_identifier

    def do(self):
        if self.topic_identifier == '':
            raise TopicStoreException("Missing 'topic identifier' parameter")

        connection = sqlite3.connect(self.database_path)
        connection.row_factory = sqlite3.Row

        cursor = connection.cursor()
        try:
            connection.execute("SELECT identifier FROM occurrence WHERE topicmap_identifier = ? AND topic_identifier_fk = ?", (self.map_identifier, self.topic_identifier))
            records = cursor.fetchall()
            for record in records:
                # TODO: Optimize.
                DeleteOccurrence(self.database_path, self.map_identifier, record['identifier']).do()
        except sqlite3.Error as e:
            raise TopicStoreException(e)
        finally:
            if connection:
                connection.close()
