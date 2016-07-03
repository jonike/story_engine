"""
TopicStore class. Part of the StoryTechnologies Builder project.

June 15, 2016
Brett Alistair Kromkamp (brett.kromkamp@gmail.com)
"""

import sqlite3

from engine.topicmap.models.basename import BaseName
from engine.topicmap.models.language import Language
from engine.topicmap.models.metadatum import Metadatum
from engine.topicmap.models.topic import Topic
from engine.topicmap.retrievaloption import RetrievalOption
from engine.topicmap.topicstoreexception import TopicStoreException


class TopicStore:

    # INITIALIZATION

    def __init__(self):
        self.__connection = None

    def open(self, path):
        self.__connection = sqlite3.connect(path)
        self.__connection.row_factory = sqlite3.Row

    def close(self):
        self.__connection.close()

    # SUPPORT

    def bootstrap(self):
        pass

    # METRICS

    # TOPICS

    def create_topic(self):
        pass

    def put_topic(self):
        pass

    def put_base_names(self):
        pass

    def get_topic(self, identifier,
                  resolve_metadata=RetrievalOption.dont_resolve_metadata,
                  resolve_occurrences=RetrievalOption.dont_resolve_occurrences,
                  inline_resource_data=RetrievalOption.dont_inline_resource_data):
        result = None
        with self.__connection:
            cursor = self.__connection.cursor()
            try:
                cursor.execute("SELECT identifier, instance_of FROM topic WHERE identifier = ?", (identifier,))
                record = cursor.fetchone()
                if record:
                    result = Topic(record['identifier'], record['instance_of'])
                    result.clear_base_names()
                    cursor.execute("SELECT name, language, identifier FROM basename WHERE topic_identifier_fk = ?", (identifier,))
                    base_names = cursor.fetchall()
                    if base_names:
                        for base_name in base_names:
                            result.add_base_name(BaseName(base_name['name'], Language[base_name['language']], base_name['identifier']))
                    if resolve_metadata is RetrievalOption.resolve_metadata:
                        result.add_metadata(self.get_metadata(identifier))
                    if resolve_occurrences is RetrievalOption.resolve_occurrences:
                        if inline_resource_data is RetrievalOption.inline_resource_data:
                            pass
            except sqlite3.Error as e:
                raise TopicStoreException(e)
            finally:
                if cursor:
                    cursor.close()
        return result

    def get_topics(self):
        pass

    def get_topics_by_metadatum_name(self):
        pass

    def get_topics_by_instance_of(self):
        pass

    def get_next_topic(self):
        pass

    def get_previous_topic(self):
        pass

    def query_topic_identifiers(self):
        pass

    def query_topic_names(self):
        pass

    def get_topic_names(self):
        pass

    def topic_exists(self, identifier):
        result = False
        with self.__connection:
            cursor = self.__connection.cursor()
            try:
                cursor.execute("SELECT identifier FROM topics WHERE identifier = ?", (identifier,))
                record = cursor.fetchone()
                if record:
                    result = True
            except sqlite3.Error as e:
                raise TopicStoreException(e)
            finally:
                if cursor:
                    cursor.close()
        return result

    # ASSOCIATIONS

    def create_association(self):
        pass

    def put_association(self):
        pass

    def delete_association(self):
        pass

    def delete_associations(self):
        pass

    def get_association(self):
        pass

    def get_associations(self):
        pass

    def get_associations_by_instance_of(self):
        pass

    def get_related_topics(self):
        pass

    def get_association_groups(self):
        pass

    def resolve_topic_refs(self):
        pass

    # OCCURRENCES

    def create_occurrence(self):
        pass

    def put_occurrence(self):
        pass

    def put_occurrences(self):
        pass

    def put_occurrence_data(self, identifier, resource_data):
        with self.__connection:
            cursor = self.__connection.cursor()
            try:
                cursor.execute("UPDATE occurrence SET resource_data = ? WHERE identifier = ?", (resource_data, identifier))
            except sqlite3.Error as e:
                raise TopicStoreException(e)
            finally:
                if cursor:
                    cursor.close()

    def delete_occurrence(self, identifier):
        pass

    def delete_occurrences(self, topic_identifier):
        pass

    def get_occurrence(self, identifier,
                       inline_resource_data=RetrievalOption.dont_inline_resource_data):
        pass

    def get_occurrence_data(self, identifier):
        resource_data = None
        with self.__connection:
            cursor = self.__connection.cursor()
            try:
                cursor.execute("SELECT resource_data FROM occurrence WHERE identifier = ?", (identifier,))
                record = cursor.fetchone()
                if record:
                    resource_data = record['resource_data']
            except sqlite3.Error as e:
                raise TopicStoreException(e)
            finally:
                if cursor:
                    cursor.close()
        return resource_data

    def get_occurrences(self,
                        inline_resource_data=RetrievalOption.dont_inline_resource_data,
                        language=Language.en):
        pass

    def get_occurrences_by_instance_of(self):
        pass

    def occurrence_exists(self):
        pass

    # METADATA

    def create_metadatum(self):
        pass

    def put_metadatum(self):
        pass

    def put_metadata(self):
        pass

    def delete_metadatum(self):
        pass

    def delete_metadata(self):
        pass

    def get_metadatum(self, identifier):
        metadatum = None
        with self.__connection:
            cursor = self.__connection.cursor()
            try:
                cursor.execute("SELECT * FROM metadatum WHERE identifier = ?", (identifier,))
                record = cursor.fetchone()
                if record:
                    metadatum = Metadatum(
                        record['name'],
                        record['value'],
                        record['parent_identifier_fk'],
                        record['identifier'],
                        record['data_type'],
                        record['scope'],
                        Language[record['language']])
            except sqlite3.Error as e:
                raise TopicStoreException(e)
            finally:
                if cursor:
                    cursor.close()
        return metadatum

    def get_metadata(self, entity_identifier, language=Language.en):
        metadata = []
        with self.__connection:
            cursor = self.__connection.cursor()
            try:
                cursor.execute("SELECT * FROM metadatum WHERE parent_identifier_fk = ? AND language = ?", (entity_identifier, language.name))
                records = cursor.fetchall()
                for record in records:
                    metadatum = Metadatum(
                        record['name'],
                        record['value'],
                        record['parent_identifier_fk'],
                        record['identifier'],
                        record['data_type'],
                        record['scope'],
                        Language[record['language']])
                    metadata.append(metadatum)
            except sqlite3.Error as e:
                raise TopicStoreException(e)
            finally:
                if cursor:
                    cursor.close()
        return metadata
