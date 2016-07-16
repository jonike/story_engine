"""
PutMetadataCommand class. Part of the StoryTechnologies Builder project.

July 13, 2016
Brett Alistair Kromkamp (brett.kromkamp@gmail.com)
"""

from engine.store.topicstoreexception import TopicStoreException
from engine.store.commands.metadatum.putmetadatum import PutMetadatumCommand


class PutMetadataCommand:

    def __init__(self, database_path, metadata=None):
        self.database_path = database_path
        self.metadata = metadata

    def do(self):
        if self.metadata is None:
            raise TopicStoreException("Missing 'metadata' parameter")

        put_metadatum_command = PutMetadatumCommand(self.database_path)
        for metadatum in self.metadata:
            put_metadatum_command.metadatum = metadatum
            put_metadatum_command.do()
