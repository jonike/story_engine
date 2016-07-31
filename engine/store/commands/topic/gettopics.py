"""
GetTopicsCommand class. Part of the StoryTechnologies Builder project.

July 31, 2016
Brett Alistair Kromkamp (brett.kromkamp@gmail.com)
"""

import sqlite3

from engine.store.commands.topic.gettopic import GetTopicCommand
from engine.store.topicstoreexception import TopicStoreException
from engine.store.retrievaloption import RetrievalOption
from engine.store.models.language import Language


class GetTopicsCommand:

    def __init__(self, database_path,
                 instance_of='',
                 resolve_metadata=RetrievalOption.dont_resolve_metadata,
                 language=Language.en,
                 offset=0,
                 limit=100):
        self.database_path = database_path
        self.instance_of = instance_of
        self.resolve_metadata = resolve_metadata
        self.language = language
        self.offset = offset
        self.limit = limit

    def do(self):
        result = []

        connection = sqlite3.connect(self.database_path)
        connection.row_factory = sqlite3.Row

        cursor = connection.cursor()
        try:
            if self.instance_of == '':
                sql = "SELECT identifier FROM topic WHERE scope IS NULL ORDER BY identifier LIMIT ? OFFSET ?"
                bind_variables = (self.limit, self.offset)
            else:
                sql = "SELECT identifier FROM topic WHERE instance_of = ? AND scope IS NULL ORDER BY identifier LIMIT ? OFFSET ?"
                bind_variables = (self.instance_of, self.limit, self.offset)

            cursor.execute(sql, bind_variables)
            records = cursor.fetchall()
            for record in records:
                result.append(GetTopicCommand(self.database_path, record['identifier'], self.resolve_metadata, self.language).do())
        except sqlite3.Error as e:
            raise TopicStoreException(e)
        finally:
            if cursor:
                cursor.close()
            if connection:
                connection.close()
        return result
