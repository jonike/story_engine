"""
PutTopicCommand class. Part of the StoryTechnologies Builder project.

July 12, 2016
Brett Alistair Kromkamp (brett.kromkamp@gmail.com)
"""

import sqlite3

from datetime import datetime

from engine.store.models.language import Language
from engine.store.models.datatype import DataType
from engine.store.models.metadatum import Metadatum
from engine.store.topicstoreexception import TopicStoreException
from engine.store.commands.metadatum.putmetadata import PutMetadataCommand


class PutTopicCommand:

    def __init__(self, database_path, topic=None, language=Language.en):
        self.database_path = database_path
        self.topic = topic
        self.language = language

    def do(self):
        if self.topic is None:
            raise TopicStoreException("Missing 'topic' parameter")

        connection = sqlite3.connect(self.database_path)

        try:
            with connection:  # https://docs.python.org/3/library/sqlite3.html#using-the-connection-as-a-context-manager
                connection.execute("INSERT INTO topic (identifier, instance_of) VALUES (?, ?)", (self.topic.identifier, self.topic.instance_of))
                for base_name in self.topic.base_names:
                    connection.execute("INSERT INTO basename (identifier, name, topic_identifier_fk, language) VALUES (?, ?, ?, ?)",
                                       (base_name.identifier,
                                        base_name.name,
                                        self.topic.identifier,
                                        str(base_name.language)))
            if not self.topic.get_metadatum_by_name('creation-timestamp'):
                timestamp = str(datetime.now())
                timestamp_metadatum = Metadatum('creation-timestamp', timestamp, self.topic.identifier,
                                                data_type=DataType.timestamp,
                                                scope='*',
                                                language=Language.en)
                self.topic.add_metadatum(timestamp_metadatum)
            PutMetadataCommand(self.database_path, self.topic.metadata).do()
            
        except sqlite3.Error as e:
            raise TopicStoreException(e)
        finally:
            if connection:
                connection.close()
