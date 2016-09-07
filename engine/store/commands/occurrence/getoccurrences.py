"""
GetOccurrences class. Part of the StoryTechnologies Builder project.

July 05, 2016
Brett Alistair Kromkamp (brett.kromkamp@gmail.com)
"""

import sqlite3

from engine.store.topicstoreexception import TopicStoreException
from engine.store.retrievaloption import RetrievalOption
from engine.store.commands.occurrence.getoccurrencedata import GetOccurrenceData
from engine.store.commands.metadatum.getmetadata import GetMetadata
from engine.store.models.occurrence import Occurrence
from engine.store.models.language import Language


class GetOccurrences:

    def __init__(self, database_path,
                 topic_identifier='',
                 inline_resource_data=RetrievalOption.dont_inline_resource_data,
                 resolve_metadata=RetrievalOption.dont_resolve_metadata,
                 instance_of='',
                 scope='*',
                 language=Language.en):
        self.database_path = database_path
        self.topic_identifier = topic_identifier
        self.inline_resource_data = inline_resource_data
        self.resolve_metadata = resolve_metadata
        self.instance_of = instance_of
        self.scope = scope
        self.language = language

    def do(self):
        if self.topic_identifier == '':
            raise TopicStoreException("Missing 'topic identifier' parameter")
        result = []

        connection = sqlite3.connect(self.database_path)
        connection.row_factory = sqlite3.Row

        cursor = connection.cursor()
        try:
            if self.instance_of == '':
                sql = "SELECT identifier, instance_of, scope, resource_ref, topic_identifier_fk, language FROM occurrence WHERE topic_identifier_fk = ? AND scope = ? AND language = ?"
                bind_variables = (self.topic_identifier, self.scope, self.language.name)
            else:
                sql = "SELECT identifier, instance_of, scope, resource_ref, topic_identifier_fk, language FROM occurrence WHERE topic_identifier_fk = ? AND instance_of = ? AND scope = ? AND language = ?"
                bind_variables = (self.topic_identifier, self.instance_of, self.scope, self.language.name)

            cursor.execute(sql, bind_variables)
            records = cursor.fetchall()
            for record in records:
                resource_data = None
                if self.inline_resource_data:
                    # TODO: Optimize.
                    resource_data = GetOccurrenceData(self.database_path, record['identifier']).do()
                occurrence = Occurrence(
                    record['identifier'],
                    record['instance_of'],
                    record['topic_identifier_fk'],
                    record['scope'],
                    record['resource_ref'],
                    resource_data,
                    Language[record['language']])
                if self.resolve_metadata is RetrievalOption.resolve_metadata:
                    # TODO: Optimize.
                    occurrence.add_metadata(
                        GetMetadata(self.database_path, self.identifier, self.language).do())
                result.append(occurrence)
        except sqlite3.Error as e:
            raise TopicStoreException(e)
        finally:
            if cursor:
                cursor.close()
            if connection:
                connection.close()
        return result
