"""
GetTopicCommand class. Part of the StoryTechnologies Builder project.

July 04, 2016
Brett Alistair Kromkamp (brett.kromkamp@gmail.com)
"""

import sqlite3

from engine.store.models.basename import BaseName
from engine.store.models.language import Language
from engine.store.models.topic import Topic
from engine.store.retrievaloption import RetrievalOption
from engine.store.topicstoreexception import TopicStoreException
from engine.store.commands.metadatum.getmetadata import GetMetadataCommand
from engine.store.commands.occurrence.getoccurrences import GetOccurrencesCommand


class GetTopicCommand:

    def __init__(self, database_path,
                 identifier='',
                 resolve_metadata=RetrievalOption.dont_resolve_metadata,
                 resolve_occurrences=RetrievalOption.dont_resolve_occurrences,
                 inline_resource_data=RetrievalOption.dont_inline_resource_data,
                 language=Language.en):
        self.database_path = database_path
        self.identifier = identifier
        self.resolve_metadata = resolve_metadata
        self.resolve_occurrences = resolve_occurrences
        self.inline_resource_data = inline_resource_data
        self.language = language

    def do(self):
        if self.identifier == '':
            raise TopicStoreException("Missing 'identifier' parameter")
        result = None

        connection = sqlite3.connect(self.database_path)
        connection.row_factory = sqlite3.Row

        cursor = connection.cursor()
        try:
            cursor.execute("SELECT identifier, instance_of FROM topic WHERE identifier = ?", (self.identifier,))
            record = cursor.fetchone()
            if record:
                result = Topic(record['identifier'], record['instance_of'])
                result.clear_base_names()
                cursor.execute("SELECT name, language, identifier FROM basename WHERE topic_identifier_fk = ?",
                               (self.identifier,))
                base_names = cursor.fetchall()
                if base_names:
                    for base_name in base_names:
                        result.add_base_name(
                            BaseName(base_name['name'], Language[base_name['language']], base_name['identifier']))
                if self.resolve_metadata is RetrievalOption.resolve_metadata:
                    result.add_metadata(GetMetadataCommand(self.database_path, self.identifier, self.language).do())
                if self.resolve_occurrences is RetrievalOption.resolve_occurrences:
                    result.add_occurrences(GetOccurrencesCommand(self.database_path, self.identifier).do())
        except sqlite3.Error as e:
            raise TopicStoreException(e)
        finally:
            if cursor:
                cursor.close()
            if connection:
                connection.close()
        return result
