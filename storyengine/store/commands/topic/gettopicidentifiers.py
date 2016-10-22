"""
GetTopicIdentifiers class. Part of the StoryTechnologies project.

August 03, 2016
Brett Alistair Kromkamp (brett.kromkamp@gmail.com)
"""

import sqlite3

from storyengine.store.commands.topic.gettopic import GetTopic
from storyengine.store.topicstoreexception import TopicStoreException
from storyengine.store.retrievaloption import RetrievalOption
from storyengine.store.models.language import Language


class GetTopicIdentifiers:

    def __init__(self, database_path,
                 query,
                 filter_entities=RetrievalOption.dont_filter_entities,
                 offset=0,
                 limit=100):
        self.database_path = database_path
        self.query = query
        self.filter_entities = filter_entities
        self.offset = offset
        self.limit = limit

    def do(self):
        result = []

        query_string = "{0}%".format(self.query)

        connection = sqlite3.connect(self.database_path)
        connection.row_factory = sqlite3.Row

        cursor = connection.cursor()
        try:
            if self.filter_entities == RetrievalOption.filter_entities:
                sql = "SELECT identifier FROM topic WHERE identifier LIKE ? AND scope IS NULL AND instance_of IN ('scene', 'prop', 'character') ORDER BY identifier LIMIT ? OFFSET ?"
            else:
                sql = "SELECT identifier FROM topic WHERE identifier LIKE ? AND scope IS NULL ORDER BY identifier LIMIT ? OFFSET ?"
            cursor.execute(sql, (query_string, self.limit, self.offset))
            records = cursor.fetchall()
            for record in records:
                result.append(record['identifier'])
        except sqlite3.Error as e:
            raise TopicStoreException(e)
        finally:
            if cursor:
                cursor.close()
            if connection:
                connection.close()
        return result
