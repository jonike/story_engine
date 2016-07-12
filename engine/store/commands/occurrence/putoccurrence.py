"""
PutOccurrenceCommand class. Part of the StoryTechnologies Builder project.

July 12, 2016
Brett Alistair Kromkamp (brett.kromkamp@gmail.com)
"""

import sqlite3

from engine.store.models.occurrence import Occurrence
from engine.store.topicstoreexception import TopicStoreException


class PutOccurrenceCommand:

    def __init__(self, database_path, occurrence=None):
        self.database_path = database_path
        self.occurrence = occurrence

    def do(self):
        if self.occurrence is None:
            raise TopicStoreException("Missing 'occurrence' parameter")
        result = None

        connection = sqlite3.connect(self.database_path)
        connection.row_factory = sqlite3.Row

        try:
            with connection:  # https://docs.python.org/3/library/sqlite3.html#using-the-connection-as-a-context-manager
                connection.execute("INSERT INTO occurrence (identifier, instance_of, scope, resource_ref, resource_data, topic_identifier_fk, language) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (self.occurrence.identifier, self.occurrence.instance_of, self.occurrence.scope, self.occurrence.resource_ref, self.occurrence.resource_data, self.occurrence.topic_identifier, str(self.occurrence.language)))
        except sqlite3.Error as e:
            raise TopicStoreException(e)
        finally:
            if connection:
                connection.close()