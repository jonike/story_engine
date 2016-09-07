"""
GetTopic class. Part of the StoryTechnologies Builder project.

July 04, 2016
Brett Alistair Kromkamp (brett.kromkamp@gmail.com)
"""

import sqlite3

from engine.store.models.basename import BaseName
from engine.store.models.language import Language
from engine.store.models.topic import Topic
from engine.store.retrievaloption import RetrievalOption
from engine.store.topicstoreexception import TopicStoreException
from engine.store.commands.metadatum.getmetadata import GetMetadata
from engine.store.commands.occurrence.getoccurrences import GetOccurrences


class GetTopic:

    def __init__(self, database_path,
                 identifier='',
                 resolve_metadata=RetrievalOption.dont_resolve_metadata,
                 resolve_occurrences=RetrievalOption.dont_resolve_occurrences,
                 language=Language.en):
        self.database_path = database_path
        self.identifier = identifier
        self.resolve_metadata = resolve_metadata
        self.resolve_occurrences = resolve_occurrences
        self.language = language

    def do(self):
        if self.identifier == '':
            raise TopicStoreException("Missing 'identifier' parameter")
        result = None

        connection = sqlite3.connect(self.database_path)
        connection.row_factory = sqlite3.Row

        cursor = connection.cursor()
        try:
            cursor.execute("SELECT identifier, instance_of FROM topic WHERE identifier = ? AND scope IS NULL", (self.identifier,))
            topic_record = cursor.fetchone()
            if topic_record:
                result = Topic(topic_record['identifier'], topic_record['instance_of'])
                result.clear_base_names()
                cursor.execute("SELECT name, language, identifier FROM basename WHERE topic_identifier_fk = ?",
                               (self.identifier,))
                base_name_records = cursor.fetchall()
                if base_name_records:
                    for base_name_record in base_name_records:
                        result.add_base_name(
                            BaseName(base_name_record['name'],
                                     Language[base_name_record['language']],
                                     base_name_record['identifier']))
                if self.resolve_metadata is RetrievalOption.resolve_metadata:
                    result.add_metadata(GetMetadata(self.database_path, self.identifier, self.language).do())
                if self.resolve_occurrences is RetrievalOption.resolve_occurrences:
                    result.add_occurrences(GetOccurrences(self.database_path, self.identifier).do())
        except sqlite3.Error as e:
            raise TopicStoreException(e)
        finally:
            if cursor:
                cursor.close()
            if connection:
                connection.close()
        return result
