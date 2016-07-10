"""
GetOccurrenceCommand class. Part of the StoryTechnologies Builder project.

July 05, 2016
Brett Alistair Kromkamp (brett.kromkamp@gmail.com)
"""

import sqlite3

from engine.store.topicstoreexception import TopicStoreException
from engine.store.retrievaloption import RetrievalOption
from engine.store.commands.occurrence.getoccurrencedata import GetOccurrenceDataCommand
from engine.store.commands.metadatum.getmetadata import GetMetadataCommand
from engine.store.models.occurrence import Occurrence
from engine.store.models.language import Language

class GetOccurrenceCommand:

    def __init__(self, database_path,
                 identifier='',
                 inline_resource_data=RetrievalOption.dont_inline_resource_data,
                 resolve_metadata=RetrievalOption.dont_resolve_metadata,
                 language=Language.en):
        self.database_path = database_path
        self.identifier = identifier
        self.inline_resource_data = inline_resource_data
        self.resolve_metadata = resolve_metadata
        self.language = language

    def do(self):
        if self.identifier is '':
            raise TopicStoreException("Missing 'identifier' parameter")
        result = None

        connection = sqlite3.connect(self.database_path)
        connection.row_factory = sqlite3.Row

        cursor = connection.cursor()
        try:
            cursor.execute("SELECT identifier, instance_of, scope, resource_ref, topic_identifier_fk, language FROM occurrence WHERE identifier = ?", (self.identifier,))
            record = cursor.fetchone()
            if record:
                resource_data = None
                if self.inline_resource_data:
                    resource_data = GetOccurrenceDataCommand(self.database_path, self.identifier).do()
                result = Occurrence(
                        record['identifier'],
                        record['instance_of'],
                        record['topic_identifier_fk'],
                        record['scope'],
                        record['resource_ref'],
                        resource_data,
                        Language[record['language']])
                if self.resolve_metadata is RetrievalOption.resolve_metadata:
                    result.add_metadata(GetMetadataCommand(self.database_path, self.identifier, self.language).do())
        except sqlite3.Error as e:
            raise TopicStoreException(e)
        finally:
            if cursor:
                cursor.close()
            if connection:
                connection.close()
        return result
