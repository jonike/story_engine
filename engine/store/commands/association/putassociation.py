"""
PutAssociationCommand class. Part of the StoryTechnologies Builder project.

July 12, 2016
Brett Alistair Kromkamp (brett.kromkamp@gmail.com)
"""

import sqlite3

from datetime import datetime

from engine.store.models.language import Language
from engine.store.models.datatype import DataType
from engine.store.models.metadatum import Metadatum
from engine.store.topicstoreexception import TopicStoreException
from engine.store.commands.metadatum.putmetadatum import PutMetadatumCommand


class PutAssociationCommand:

    def __init__(self, database_path, association=None, language=Language.en):
        self.database_path = database_path
        self.association = association
        self.language = language

    def do(self):
        if self.association is None:
            raise TopicStoreException("Missing 'association' parameter")

        connection = sqlite3.connect(self.database_path)
        connection.row_factory = sqlite3.Row

        try:
            with connection:  # https://docs.python.org/3/library/sqlite3.html#using-the-connection-as-a-context-manager
                connection.execute("INSERT INTO topic (identifier, instance_of, scope) VALUES (?, ?, ?)", (self.association.identifier, self.association.instance_of, self.association.scope))
                for base_name in self.association.base_names:
                    connection.execute("INSERT INTO basename (identifier, name, topic_identifier_fk, language) VALUES (?, ?, ?, ?)",
                                       (base_name.identifier,
                                        base_name.name,
                                        self.association.identifier,
                                        str(base_name.language)))
                for member in association.members:
                    connection.execute("INSERT INTO member (identifier, role_spec, association_identifier_fk) VALUES (?, ?, ?)", (member.identifier, member.role_spec, association.identifier))
                    for topic_ref in members.topic_refs:
                        connection.execute("INSERT INTO topicref (topic_ref, member_identifier_fk) VALUES (?, ?)", (topic_ref, member.identifier))

            timestamp = str(datetime.now())
            metadatum = Metadatum('creation-timestamp', timestamp, self.association.identifier,
                                  data_type=DataType.timestamp,
                                  scope='*',
                                  language=Language.en)
            PutMetadatumCommand(self.database_path, metadatum).do()
        except sqlite3.Error as e:
            raise TopicStoreException(e)
        finally:
            if connection:
                connection.close()