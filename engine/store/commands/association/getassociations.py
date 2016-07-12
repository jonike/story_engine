"""
GetAssociationsCommand class. Part of the StoryTechnologies Builder project.

July 10, 2016
Brett Alistair Kromkamp (brett.kromkamp@gmail.com)
"""

import sqlite3

from engine.store.topicstoreexception import TopicStoreException
from engine.store.models.language import Language
from engine.store.retrievaloption import RetrievalOption
from engine.store.commands.association.getassociation import GetAssociationCommand


class GetAssociationsCommand:

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
            raise TopicStoreException("Missing 'topic identifier' parameter")
        result = []

        connection = sqlite3.connect(self.database_path)
        connection.row_factory = sqlite3.Row

        cursor = connection.cursor()
        try:
            cursor.execute("SELECT member_identifier_fk FROM topicref WHERE topic_ref = ?", (self.identifier,))
            topic_ref_records = cursor.fetchall()
            if topic_ref_records:
                for topic_ref_record in topic_ref_records:
                    cursor.execute("SELECT association_identifier_fk FROM member WHERE identifier = ?", (topic_ref_record['member_identifier_fk'],))
                    member_records = cursor.fetchall()
                    if member_records:
                        for member_record in member_records:
                            association = GetAssociationCommand(member_record['association_identifier_fk'], self.resolve_metadata, self.resolve_occurrences, self.language).do()
                            if association:
                                result.append(association)
        except sqlite3.Error as e:
            raise TopicStoreException(e)
        finally:
            if cursor:
                cursor.close()
            if connection:
                connection.close()
        return result
