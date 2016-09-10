"""
GetAssociation class. Part of the StoryTechnologies Builder project.

July 10, 2016
Brett Alistair Kromkamp (brett.kromkamp@gmail.com)
"""

import sqlite3

from storyengine.store.topicstoreexception import TopicStoreException
from storyengine.store.models.basename import BaseName
from storyengine.store.models.association import Association
from storyengine.store.models.language import Language
from storyengine.store.models.member import Member
from storyengine.store.retrievaloption import RetrievalOption
from storyengine.store.commands.attribute.getattributes import GetAttributes
from storyengine.store.commands.occurrence.getoccurrences import GetOccurrences


class GetAssociation:

    def __init__(self, database_path,
                 identifier='',
                 resolve_attributes=RetrievalOption.dont_resolve_attributes,
                 resolve_occurrences=RetrievalOption.dont_resolve_occurrences,
                 language=Language.en):
        self.database_path = database_path
        self.identifier = identifier
        self.resolve_attributes = resolve_attributes
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
            cursor.execute("SELECT identifier, instance_of, scope FROM topic WHERE identifier = ? AND scope IS NOT NULL", (self.identifier,))
            association_record = cursor.fetchone()
            if association_record:
                result = Association(
                    identifier=association_record['identifier'],
                    instance_of=association_record['instance_of'],
                    scope=association_record['scope'])
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
                cursor.execute("SELECT * FROM member WHERE association_identifier_fk = ?", (self.identifier,))
                member_records = cursor.fetchall()
                if member_records:
                    for member_record in member_records:
                        role_spec = member_record['role_spec']
                        cursor.execute("SELECT * FROM topicref WHERE member_identifier_fk = ?", (member_record['identifier'],))
                        topic_ref_records = cursor.fetchall()
                        if topic_ref_records:
                            member = Member(
                                role_spec=role_spec,
                                identifier=member_record['identifier'])
                            for topic_ref_record in topic_ref_records:
                                member.add_topic_ref(topic_ref_record['topic_ref'])
                            result.add_member(member)
                if self.resolve_attributes is RetrievalOption.resolve_attributes:
                    result.add_attributes(GetAttributes(self.database_path, self.identifier, self.language).do())
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
