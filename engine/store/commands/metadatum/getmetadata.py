"""
GetMetadataCommand class. Part of the StoryTechnologies Builder project.

July 04, 2016
Brett Alistair Kromkamp (brett.kromkamp@gmail.com)
"""

import sqlite3

from engine.store.models.language import Language
from engine.store.models.metadatum import Metadatum
from engine.store.topicstoreexception import TopicStoreException


class GetMetadataCommand:

    def __init__(self, database_path, entity_identifier='', language=Language.en):
        self.database_path = database_path
        self.entity_identifier = entity_identifier
        self.language = language

    def do(self):
        if self.entity_identifier == '':
            raise TopicStoreException("Missing 'entity identifier' parameter")
        result = []

        connection = sqlite3.connect(self.database_path)
        connection.row_factory = sqlite3.Row

        cursor = connection.cursor()
        try:
            cursor.execute("SELECT * FROM metadatum WHERE parent_identifier_fk = ? AND language = ?",
                           (self.entity_identifier, self.language.name))
            records = cursor.fetchall()
            for record in records:
                metadatum = Metadatum(
                    record['name'],
                    record['value'],
                    record['parent_identifier_fk'],
                    record['identifier'],
                    record['data_type'],
                    record['scope'],
                    Language[record['language']])
                result.append(metadatum)
        except sqlite3.Error as e:
            raise TopicStoreException(e)
        finally:
            if cursor:
                cursor.close()
            if connection:
                connection.close()
        return result
