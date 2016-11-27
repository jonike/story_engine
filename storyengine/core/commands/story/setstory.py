"""
SetStory class. Part of the StoryTechnologies project.

November 26, 2016
Brett Alistair Kromkamp (brett.kromkamp@gmail.com)
"""

import sqlite3

from storyengine.core.coreexception import CoreException


class SetStory:

    def __init__(self, database_path, story=None):
        self.database_path = database_path
        self.story = story

    def do(self):
        if self.story is None:
            raise CoreException("Missing 'story' parameter")

        connection = sqlite3.connect(self.database_path)

        try:
            with connection:  # https://docs.python.org/3/library/sqlite3.html#using-the-connection-as-a-context-manager
                connection.execute(
                    "INSERT INTO story (title, description, topicmap_identifier_fk, scene_identifier_fk) VALUES (?, ?, ?, ?)",
                    (self.story.title,
                     self.story.description,
                     self.story.topic_map_identifier,
                     self.story.start_scene_identifier))
        except sqlite3.Error as e:
            raise CoreException(e)
        finally:
            if connection:
                connection.close()
