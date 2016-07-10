"""
GetAssociationCommand class. Part of the StoryTechnologies Builder project.

July 10, 2016
Brett Alistair Kromkamp (brett.kromkamp@gmail.com)
"""

import sqlite3

from engine.store.topicstoreexception import TopicStoreException


class GetAssociationCommand:

    def __init__(self, database_path, identifier=''):
        self.database_path = database_path
        self.identifier = identifier

    def do(self):
        if self.identifier is '':
            raise TopicStoreException("Missing 'identifier' parameter")
        result = False

        connection = sqlite3.connect(self.database_path)
        connection.row_factory = sqlite3.Row

        cursor = connection.cursor()
        try:
            # SELECT identifier, instance_of, scope FROM topic WHERE identifier = ? AND scope IS NOT NULL
            # SELECT name, language FROM basename WHERE topic_identifier_fk = ?
            # SELECT * FROM member WHERE association_identifier_fk = ?
            pass
        except sqlite3.Error as e:
            raise TopicStoreException(e)
        finally:
            if cursor:
                cursor.close()
            if connection:
                connection.close()
        return result
