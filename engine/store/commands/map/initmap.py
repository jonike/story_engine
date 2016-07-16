"""
InitMapCommand class. Part of the StoryTechnologies Builder project.

July 16, 2016
Brett Alistair Kromkamp (brett.kromkamp@gmail.com)
"""

import sqlite3

from engine.store.topicstoreexception import TopicStoreException
from engine.store.commands.map.topicfield import TopicField


class InitMapCommand:

    def __init__(self, database_path):
        self.database_path = database_path
        self.items = {
            ('entity', 'Entity'),
            ('association', 'Association'),
            ('occurrence', 'Occurrence'),
            ('*', 'Universal Scope'),
            ('genesis', 'Genesis'),
            ('navigation', 'Navigation'),
            ('categorization', 'Categorization'),
            ('related', 'Related'),
            ('parent', 'Parent'),
            ('child', 'Child'),
            ('previous', 'Previous'),
            ('next', 'Next'),
            ('story', 'Story'),
            ('book', 'Book'),
            ('chapter', 'Chapter'),
            ('scene', 'Scene'),
            ('environment', 'Environment'),
            ('prop', 'Prop'),
            ('character', 'Character'),
            ('north', 'North'),
            ('north-east', 'Northeast'),
            ('east', 'East'),
            ('south-east', 'Southeast'),
            ('south', 'South'),
            ('south-west', 'Southwest'),
            ('west', 'West'),
            ('north-west', 'Northwest'),
            ('topic', 'Topic'),
        }

    def do(self):

        connection = sqlite3.connect(self.database_path)

        try:
            with connection:  # https://docs.python.org/3/library/sqlite3.html#using-the-connection-as-a-context-manager
                pass
        except sqlite3.Error as e:
            raise TopicStoreException(e)
        finally:
            if connection:
                connection.close()
