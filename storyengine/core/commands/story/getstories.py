"""
GetStories class. Part of the StoryTechnologies project.

November 26, 2016
Brett Alistair Kromkamp (brett.kromkamp@gmail.com)
"""

import sqlite3

from storyengine.core.coreerror import CoreError
from storyengine.core.models.story import Story


class GetStories:

    def __init__(self, database_path):
        self.database_path = database_path

    def execute(self):
        result = []

        connection = sqlite3.connect(self.database_path)
        connection.row_factory = sqlite3.Row

        cursor = connection.cursor()
        try:
            cursor.execute("SELECT * FROM story")
            records = cursor.fetchall()
            for record in records:
                story = Story(
                    record['title'],
                    record['topicmap_identifier_fk'],
                    record['scene_identifier_fk'],
                    record['description'])
                story.identifier = record['identifier']
                result.append(story)
        except sqlite3.Error as error:
            raise CoreError(error)
        finally:
            if cursor:
                cursor.close()
            if connection:
                connection.close()
        return result
