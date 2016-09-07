"""
SetAttribute class. Part of the StoryTechnologies Builder project.

July 12, 2016
Brett Alistair Kromkamp (brett.kromkamp@gmail.com)
"""

import sqlite3

from engine.store.topicstoreexception import TopicStoreException


class SetAttribute:

    def __init__(self, database_path, attribute=None):
        self.database_path = database_path
        self.attribute = attribute

    def do(self):
        if self.attribute is None:
            raise TopicStoreException("Missing 'attribute' parameter")
        elif self.attribute.entity_identifier == '':
            raise TopicStoreException("Attribute has an empty 'entity identifier' property")

        connection = sqlite3.connect(self.database_path)

        try: 
            with connection:  # https://docs.python.org/3/library/sqlite3.html#using-the-connection-as-a-context-manager
                connection.execute("INSERT INTO attribute (identifier, parent_identifier_fk, name, value, data_type, scope, language) VALUES (?, ?, ?, ?, ?, ?, ?)",
                                   (self.attribute.identifier,
                                    self.attribute.entity_identifier,
                                    self.attribute.name,
                                    self.attribute.value,
                                    self.attribute.data_type.name,
                                    self.attribute.scope,
                                    self.attribute.language.name))
        except sqlite3.Error as e:
            raise TopicStoreException(e)
        finally:
            if connection:
                connection.close()
