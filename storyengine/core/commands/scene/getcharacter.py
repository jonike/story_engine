"""
GetCharacter class. Part of the StoryTechnologies project.

July 22, 2016
Brett Alistair Kromkamp (brett.kromkamp@gmail.com)
"""

from storyengine.core.coreerror import CoreError
from storyengine.core.models.asset import Asset
from storyengine.core.models.character import Character
from topicdb.core.commands.occurrence.getoccurrences import GetOccurrences
from topicdb.core.topicstoreerror import TopicStoreError
from topicdb.core.commands.topic.gettopic import GetTopic
from topicdb.core.retrievaloption import RetrievalOption


class GetCharacter:
    def __init__(self, database_path, map_identifier, identifier=''):
        self.database_path = database_path
        self.map_identifier = map_identifier
        self.identifier = identifier

    def execute(self):
        if self.identifier == '':
            raise CoreError("Missing 'identifier' parameter")
        result = None
        try:
            topic = GetTopic(self.database_path, self.map_identifier, self.identifier, RetrievalOption.resolve_attributes).execute()
            if topic:
                result = Character(topic.identifier, topic.first_base_name.name)
                result.location = topic.get_attribute_by_name('location').value
                result.rotation = topic.get_attribute_by_name('rotation').value
                result.scale = topic.get_attribute_by_name('scale').value

                occurrences = GetOccurrences(self.database_path, self.map_identifier, self.identifier).execute()
                for occurrence in occurrences:
                    result.add_asset(Asset(occurrence.instance_of, occurrence.resource_ref))

                attributes = [attribute for attribute in topic.attributes if
                              attribute.name not in ('location', 'rotation', 'scale')]
                result.add_attributes(attributes)
        except TopicStoreError as error:
            raise CoreError(error)
        return result
