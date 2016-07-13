"""
PutMetadataCommand class. Part of the StoryTechnologies Builder project.

July 13, 2016
Brett Alistair Kromkamp (brett.kromkamp@gmail.com)
"""

import sqlite3

from engine.store.topicstoreexception import TopicStoreException


class PutMetadataCommand:

    def __init__(self, database_path, metadata=None):
        self.database_path = database_path
        self.metadata = metadata

    def do(self):
        if self.metadata is None:
            raise TopicStoreException("Missing 'metadata' parameter")

        connection = sqlite3.connect(self.database_path)

        try:
            with connection:  # https://docs.python.org/3/library/sqlite3.html#using-the-connection-as-a-context-manager
                for metadatum in metadata:
                    connection.execute("INSERT INTO metadatum (identifier, parent_identifier_fk, name, value, data_type, scope, language) VALUES (?, ?, ?, ?, ?, ?, ?)",
                                       (self.metadatum.identifier,
                                        self.metadatum.entity_identifier,
                                        self.metadatum.name,
                                        self.metadatum.value,
                                        str(self.metadatum.data_type),
                                        self.metadatum.scope,
                                        str(self.metadatum.language)))
        except sqlite3.Error as e:
            raise TopicStoreException(e)
        finally:
            if connection:
                connection.close()