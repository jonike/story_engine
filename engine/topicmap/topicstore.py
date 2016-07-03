"""
TopicStore class. Part of the StoryTechnologies Builder project.

June 15, 2016
Brett Alistair Kromkamp (brett.kromkamp@gmail.com)
"""


import sqlite3
import unittest

from engine.topicmap.models.topic import Topic
from engine.topicmap.models.occurrence import Occurrence
from engine.topicmap.models.association import Association
from engine.topicmap.models.metadatum import Metadatum
from engine.topicmap.models.language import Language

class TopicStore:

    # INITIALIZATION

    def __init__(self):
        self.__connection = None

    def open(self, path):
        self.__connection = sqlite3.connect(path)
        self.__connection.row_factory = sqlite3.Row  # TODO: Verify if necessary.

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

    def get_topic(self, identifier, occurrence_scope='*', language=Language.en):
        result = None
        with self.__connection:
            cursor = self.__connection.cursor()
            try:
                cursor.execute("SELECT identifier, instance_of FROM topic WHERE identifier = ?", (identifier,))
                record = cursor.fetchone()
                if record:
                    result = Topic(record[0], record[1])
                    result.clear_base_names()
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

    def topic_exists(self):
        pass

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

    def put_occurrence_data(self):
        pass

    def delete_occurrence(self):
        pass

    def delete_occurrences(self):
        pass

    def get_occurrence(self):
        pass

    def get_occurrence_data(self):
        pass

    def get_occurrences(self):
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

    def delete_metadatum(self):
        pass

    def delete_metadatum_by_id(self):
        pass

    def delete_metadata(self):
        pass

    def put_metadata(self):
        pass

    def get_metadatum(self):
        pass

    def get_metadata(self):
        pass

    def get_metadatum_by_id(self):
        pass
