"""
GetPropCommand class. Part of the StoryTechnologies Builder project.

July 22, 2016
Brett Alistair Kromkamp (brett.kromkamp@gmail.com)
"""

from engine.core.coreexception import CoreException
from engine.core.models.asset import Asset
from engine.store.commands.occurrence.getoccurrences import GetOccurrencesCommand
from engine.store.topicstoreexception import TopicStoreException
from engine.store.commands.topic.gettopic import GetTopicCommand
from engine.store.retrievaloption import RetrievalOption
from engine.core.models.prop import Prop


class GetPropCommand:
    def __init__(self, database_path, identifier=''):
        self.database_path = database_path
        self.identifier = identifier

    def do(self):
        if self.identifier == '':
            raise CoreException("Missing 'identifier' parameter")
        result = None
        try:
            topic = GetTopicCommand(self.database_path, self.identifier, RetrievalOption.resolve_metadata).do()
            if topic:
                result = Prop(topic.identifier, topic.first_base_name.name)
                result.location = topic.get_metadatum_by_name('location').value
                result.rotation = topic.get_metadatum_by_name('rotation').value
                result.scale = topic.get_metadatum_by_name('scale').value

                occurrences = GetOccurrencesCommand(self.database_path, self.identifier).do()
                for occurrence in occurrences:
                    result.add_asset(Asset(occurrence.resource_ref, occurrence.instance_of))
        except TopicStoreException as e:
            raise CoreException(e)
        return result
