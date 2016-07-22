"""
GetCharacterCommand class. Part of the StoryTechnologies Builder project.

July 22, 2016
Brett Alistair Kromkamp (brett.kromkamp@gmail.com)
"""

from engine.core.coreexception import CoreException
from engine.store.topicstoreexception import TopicStoreException


class GetCharacterCommand:
    def __init__(self, database_path, identifier=''):
        self.database_path = database_path
        self.identifier = identifier

    def do(self):
        if self.identifier == '':
            raise CoreException("Missing 'identifier' parameter")
        result = None
        try:
            pass
        except TopicStoreException as e:
            raise CoreException(e)
        return result
