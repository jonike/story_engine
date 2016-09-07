"""
GetCharacter class. Part of the StoryTechnologies Builder project.

July 22, 2016
Brett Alistair Kromkamp (brett.kromkamp@gmail.com)
"""

from engine.core.coreexception import CoreException
from engine.core.models.asset import Asset
from engine.core.models.character import Character
from engine.store.commands.occurrence.getoccurrences import GetOccurrences
from engine.store.topicstoreexception import TopicStoreException
from engine.store.commands.topic.gettopic import GetTopic
from engine.store.retrievaloption import RetrievalOption


class GetCharacter:
    def __init__(self, database_path, identifier=''):
        self.database_path = database_path
        self.identifier = identifier

    def do(self):
        if self.identifier == '':
            raise CoreException("Missing 'identifier' parameter")
        result = None
        try:
            topic = GetTopic(self.database_path, self.identifier, RetrievalOption.resolve_attributes).do()
            if topic:
                result = Character(topic.identifier, topic.first_base_name.name)
                result.location = topic.get_attribute_by_name('location').value
                result.rotation = topic.get_attribute_by_name('rotation').value
                result.scale = topic.get_attribute_by_name('scale').value

                occurrences = GetOccurrences(self.database_path, self.identifier).do()
                for occurrence in occurrences:
                    result.add_asset(Asset(occurrence.instance_of, occurrence.resource_ref))

                attributes = [attribute for attribute in topic.attributes if
                              attribute.name not in ('location', 'rotation', 'scale')]
                result.add_attributes(attributes)
        except TopicStoreException as e:
            raise CoreException(e)
        return result
