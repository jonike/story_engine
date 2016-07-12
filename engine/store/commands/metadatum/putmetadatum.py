"""
PutMetadatumCommand class. Part of the StoryTechnologies Builder project.

July 12, 2016
Brett Alistair Kromkamp (brett.kromkamp@gmail.com)
"""

import sqlite3

from engine.store.models.metadatum import Metadatum
from engine.store.topicstoreexception import TopicStoreException


class PutMetadatumCommand:

    def __init__(self, database_path, metadatum=None):
        self.database_path = database_path
        self.metadatum = metadatum

    def do(self):
        if self.metadatum is None:
            raise TopicStoreException("Missing 'metadatum' parameter")
        result = None

        connection = sqlite3.connect(self.database_path)
        connection.row_factory = sqlite3.Row

        try: 
            with connection:  # https://docs.python.org/3/library/sqlite3.html#using-the-connection-as-a-context-manager
                connection.execute("INSERT INTO metadatum (identifier, parent_identifier_fk, name, value, data_type, scope, language) VALUES (?, ?, ?, ?, ?, ?, ?)", (self.metadatum.identifier, self.metadatum.entity_identifier, self.metadatum.name, self.metadatum.value, str(self.metadatum.data_type), self.metadatum.scope, str(self.metadatum.language)))
        except sqlite3.Error as e:
            raise TopicStoreException(e)
        finally:
            if connection:
                connection.close()