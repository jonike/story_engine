"""
SetTags class. Part of the StoryTechnologies project.

August 29, 2016
Brett Alistair Kromkamp (brett.kromkamp@gmail.com)
"""

from storyengine.store.topicstoreexception import TopicStoreException
from storyengine.store.commands.tag.settag import SetTag


class SetTags:

    def __init__(self, database_path, map_identifier,
                 identifier='',
                 tags=None):
        self.database_path = database_path
        self.map_identifier = map_identifier
        self.identifier = identifier
        self.tags = tags

    def do(self):
        if self.tags is None or self.identifier == '':
            raise TopicStoreException("Missing 'tags' or 'identifier' parameter")

        for tag in self.tags:
            SetTag(self.database_path, self.map_identifier, self.identifier, tag).do()
