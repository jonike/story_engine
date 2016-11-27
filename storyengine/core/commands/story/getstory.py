"""
GetStory class. Part of the StoryTechnologies project.

November 26, 2016
Brett Alistair Kromkamp (brett.kromkamp@gmail.com)
"""

import sqlite3

from storyengine.core.coreexception import CoreException
from storyengine.core.models.story import Story


class GetStory:

    def __init__(self, database_path, identifier=''):
        self.database_path = database_path
        self.identifier = identifier

    def do(self):
        if self.identifier == '':
            raise CoreException("Missing 'identifier' parameter")
        result = None

        connection = sqlite3.connect(self.database_path)
        connection.row_factory = sqlite3.Row

        cursor = connection.cursor()
        try:
            cursor.execute("SELECT * FROM story WHERE identifier = ?", (self.identifier, ))
            record = cursor.fetchone()
            if record:
                result = Story(
                    record['title'],
                    record['topicmap_identifier_fk'],
                    record['scene_identifier_fk'],
                    record['description'])
                result.identifier = record['identifier']
        except CoreException as e:
            raise CoreException(e)
        return result
