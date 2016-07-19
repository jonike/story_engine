"""
GetSceneCommand class. Part of the StoryTechnologies Builder project.

July 19, 2016
Brett Alistair Kromkamp (brett.kromkamp@gmail.com)
"""

from engine.core.coreexception import CoreException
from engine.store.topicstoreexception import TopicStoreException
from engine.store.commands.topic.gettopic import GetTopicCommand
from engine.store.commands.occurrence.getoccurrences import GetOccurrencesCommand
from engine.store.commands.metadatum.getmetadata import GetMetadataCommand
from engine.store.commands.association.getassociations import GetAssociationsCommand
from engine.store.commands.association.getassociationgroups import GetAssociationGroupsCommand
from engine.core.models.scene import Scene


class GetSceneCommand:
    def __init__(self, database_path, scene_identifier=''):
        self.database_path = database_path
        self.scene_identifier = scene_identifier
        self.result = None

    def do(self):
        if self.scene_identifier == '':
            raise CoreException("Missing 'scene identifier' parameter")
        try:
            topic = GetTopicCommand(self.database_path, self.scene_identifier).do()
            if topic:
                self.result = Scene(topic.identifier, topic.first_base_name)

                metadata = GetMetadataCommand(self.database_path, self.scene_identifier).do()
                occurrences = GetOccurrencesCommand(self.database_path, self.scene_identifier).do()
                associations = GetAssociationsCommand(self.database_path, self.scene_identifier)
                association_groups = GetAssociationGroupsCommand(self.database_path, associations=associations)

                # TODO: Implement.

        except TopicStoreException as e:
            raise CoreException(e)
        return self.result

    def view(self):
        if self.result:
            pass