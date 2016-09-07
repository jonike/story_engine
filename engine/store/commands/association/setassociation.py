"""
SetAssociation class. Part of the StoryTechnologies Builder project.

July 12, 2016
Brett Alistair Kromkamp (brett.kromkamp@gmail.com)
"""

import sqlite3

from datetime import datetime

from engine.store.models.language import Language
from engine.store.models.datatype import DataType
from engine.store.models.attribute import Attribute
from engine.store.topicstoreexception import TopicStoreException
from engine.store.commands.attribute.setattributes import SetAttributes


class SetAssociation:

    def __init__(self, database_path, association=None):
        self.database_path = database_path
        self.association = association

    def do(self):
        if self.association is None:
            raise TopicStoreException("Missing 'association' parameter")

        connection = sqlite3.connect(self.database_path)

        try:
            with connection:  # https://docs.python.org/3/library/sqlite3.html#using-the-connection-as-a-context-manager
                connection.execute("INSERT INTO topic (identifier, instance_of, scope) VALUES (?, ?, ?)", (self.association.identifier, self.association.instance_of, self.association.scope))
                for base_name in self.association.base_names:
                    connection.execute("INSERT INTO basename (identifier, name, topic_identifier_fk, language) VALUES (?, ?, ?, ?)",
                                       (base_name.identifier,
                                        base_name.name,
                                        self.association.identifier,
                                        base_name.language.name))
                for member in self.association.members:
                    connection.execute("INSERT INTO member (identifier, role_spec, association_identifier_fk) VALUES (?, ?, ?)", (member.identifier, member.role_spec, self.association.identifier))
                    for topic_ref in member.topic_refs:
                        connection.execute("INSERT INTO topicref (topic_ref, member_identifier_fk) VALUES (?, ?)", (topic_ref, member.identifier))

            if not self.association.get_attribute_by_name('creation-timestamp'):
                timestamp = str(datetime.now())
                timestamp_attribute = Attribute('creation-timestamp', timestamp, self.association.identifier,
                                                data_type=DataType.timestamp,
                                                scope='*',
                                                language=Language.en)
                self.association.add_attribute(timestamp_attribute)
            SetAttributes(self.database_path, self.association.attributes).do()
        except sqlite3.Error as e:
            raise TopicStoreException(e)
        finally:
            if connection:
                connection.close()
