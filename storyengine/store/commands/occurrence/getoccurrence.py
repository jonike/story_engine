"""
GetOccurrence class. Part of the StoryTechnologies Builder project.

July 05, 2016
Brett Alistair Kromkamp (brett.kromkamp@gmail.com)
"""

import sqlite3

from storyengine.store.topicstoreexception import TopicStoreException
from storyengine.store.retrievaloption import RetrievalOption
from storyengine.store.commands.occurrence.getoccurrencedata import GetOccurrenceData
from storyengine.store.commands.attribute.getattributes import GetAttributes
from storyengine.store.models.occurrence import Occurrence
from storyengine.store.models.language import Language


class GetOccurrence:

    def __init__(self, database_path,
                 identifier='',
                 inline_resource_data=RetrievalOption.dont_inline_resource_data,
                 resolve_attributes=RetrievalOption.dont_resolve_attributes,
                 language=Language.en):
        self.database_path = database_path
        self.identifier = identifier
        self.inline_resource_data = inline_resource_data
        self.resolve_attributes = resolve_attributes
        self.language = language

    def do(self):
        if self.identifier == '':
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
                    resource_data = GetOccurrenceData(self.database_path, self.identifier).do()
                result = Occurrence(
                        record['identifier'],
                        record['instance_of'],
                        record['topic_identifier_fk'],
                        record['scope'],
                        record['resource_ref'],
                        resource_data,
                        Language[record['language']])
                if self.resolve_attributes is RetrievalOption.resolve_attributes:
                    # TODO: Optimize.
                    result.add_attributes(GetAttributes(self.database_path, self.identifier, self.language).do())
        except sqlite3.Error as e:
            raise TopicStoreException(e)
        finally:
            if cursor:
                cursor.close()
            if connection:
                connection.close()
        return result
