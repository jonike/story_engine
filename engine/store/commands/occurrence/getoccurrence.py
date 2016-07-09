"""
GetOccurrenceCommand class. Part of the StoryTechnologies Builder project.

July 05, 2016
Brett Alistair Kromkamp (brett.kromkamp@gmail.com)
"""

import sqlite3

from engine.store.topicstoreexception import TopicStoreException
from engine.store.retrievaloption import RetrievalOption


class GetOccurrenceCommand:

    def __init__(self, database_path,
                 identifier='',
                 inline_resource_data=RetrievalOption.dont_inline_resource_data):
        self.database_path = database_path
        self.identifier = identifier
        self.inline_resource_data = inline_resource_data

    def execute(self):
        pass
