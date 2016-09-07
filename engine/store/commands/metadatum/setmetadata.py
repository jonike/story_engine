"""
SetMetadata class. Part of the StoryTechnologies Builder project.

July 13, 2016
Brett Alistair Kromkamp (brett.kromkamp@gmail.com)
"""

from engine.store.topicstoreexception import TopicStoreException
from engine.store.commands.metadatum.setmetadatum import SetMetadatum


class SetMetadata:

    def __init__(self, database_path, metadata=None):
        self.database_path = database_path
        self.metadata = metadata

    def do(self):
        if self.metadata is None:
            raise TopicStoreException("Missing 'metadata' parameter")

        set_metadatum_command = SetMetadatum(self.database_path)
        for metadatum in self.metadata:
            set_metadatum_command.metadatum = metadatum
            set_metadatum_command.do()
