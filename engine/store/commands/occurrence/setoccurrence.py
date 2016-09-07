"""
SetOccurrence class. Part of the StoryTechnologies Builder project.

July 12, 2016
Brett Alistair Kromkamp (brett.kromkamp@gmail.com)
"""

import sqlite3

from datetime import datetime

from engine.store.models.language import Language
from engine.store.models.datatype import DataType
from engine.store.models.metadatum import Metadatum
from engine.store.commands.metadatum.setmetadata import SetMetadata
from engine.store.topicstoreexception import TopicStoreException


class SetOccurrence:

    def __init__(self, database_path, occurrence=None):
        self.database_path = database_path
        self.occurrence = occurrence

    def do(self):
        if self.occurrence is None:
            raise TopicStoreException("Missing 'occurrence' parameter")
        elif self.occurrence.topic_identifier == '':
            raise TopicStoreException("Occurrence has an empty 'topic identifier' property")

        connection = sqlite3.connect(self.database_path)

        try:
            with connection:  # https://docs.python.org/3/library/sqlite3.html#using-the-connection-as-a-context-manager
                connection.execute("INSERT INTO occurrence (identifier, instance_of, scope, resource_ref, resource_data, topic_identifier_fk, language) VALUES (?, ?, ?, ?, ?, ?, ?)",
                                   (self.occurrence.identifier,
                                    self.occurrence.instance_of,
                                    self.occurrence.scope,
                                    self.occurrence.resource_ref,
                                    self.occurrence.resource_data,
                                    self.occurrence.topic_identifier,
                                    self.occurrence.language.name))
            if not self.occurrence.get_metadatum_by_name('creation-timestamp'):
                timestamp = str(datetime.now())
                timestamp_metadatum = Metadatum('creation-timestamp', timestamp, self.occurrence.identifier,
                                                data_type=DataType.timestamp,
                                                scope='*',
                                                language=Language.en)
                self.occurrence.add_metadatum(timestamp_metadatum)
            SetMetadata(self.database_path, self.occurrence.metadata).do()
        except sqlite3.Error as e:
            raise TopicStoreException(e)
        finally:
            if connection:
                connection.close()
