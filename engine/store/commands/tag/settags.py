"""
SetTagsCommand class. Part of the StoryTechnologies Builder project.

August 29, 2016
Brett Alistair Kromkamp (brett.kromkamp@gmail.com)
"""

from engine.store.topicstoreexception import TopicStoreException
from engine.store.commands.tag.settag import SetTagCommand


class SetTagsCommand:

    def __init__(self, database_path, identifier='', tags=None):
        self.database_path = database_path
        self.identifier = identifier
        self.tags = tags

    def do(self):
        if self.tags is None or self.identifier == '':
            raise TopicStoreException("Missing 'tags' or 'identifier' parameter")

        for tag in self.tags:
            SetTagCommand(self.database_path, self.identifier, tag).do()
