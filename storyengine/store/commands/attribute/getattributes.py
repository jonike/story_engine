"""
GetAttributes class. Part of the StoryTechnologies Builder project.

July 04, 2016
Brett Alistair Kromkamp (brett.kromkamp@gmail.com)
"""

import sqlite3

from storyengine.store.models.language import Language
from storyengine.store.models.datatype import DataType
from storyengine.store.models.attribute import Attribute
from storyengine.store.topicstoreexception import TopicStoreException


class GetAttributes:

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
            cursor.execute("SELECT * FROM attribute WHERE parent_identifier_fk = ? AND language = ?",
                           (self.entity_identifier, self.language.name))
            records = cursor.fetchall()
            for record in records:
                attribute = Attribute(
                    record['name'],
                    record['value'],
                    record['parent_identifier_fk'],
                    record['identifier'],
                    DataType[record['data_type']],
                    record['scope'],
                    Language[record['language']])
                result.append(attribute)
        except sqlite3.Error as e:
            raise TopicStoreException(e)
        finally:
            if cursor:
                cursor.close()
            if connection:
                connection.close()
        return result
