"""
GetProp class. Part of the StoryTechnologies project.

July 22, 2016
Brett Alistair Kromkamp (brett.kromkamp@gmail.com)
"""

from storyengine.core.coreexception import CoreException
from storyengine.core.models.asset import Asset
from storyengine.store.commands.occurrence.getoccurrences import GetOccurrences
from storyengine.store.topicstoreexception import TopicStoreException
from storyengine.store.commands.topic.gettopic import GetTopic
from storyengine.store.retrievaloption import RetrievalOption
from storyengine.core.models.prop import Prop


class GetProp:
    def __init__(self, database_path, map_identifier, identifier=''):
        self.database_path = database_path
        self.map_identifier = map_identifier
        self.identifier = identifier

    def do(self):
        if self.identifier == '':
            raise CoreException("Missing 'identifier' parameter")
        result = None
        try:
            topic = GetTopic(self.database_path, self.identifier, self.map_identifier, RetrievalOption.resolve_attributes).do()
            if topic:
                result = Prop(topic.identifier, topic.first_base_name.name)
                result.location = topic.get_attribute_by_name('location').value
                result.rotation = topic.get_attribute_by_name('rotation').value
                result.scale = topic.get_attribute_by_name('scale').value

                occurrences = GetOccurrences(self.database_path, self.map_identifier, self.identifier).do()
                for occurrence in occurrences:
                    result.add_asset(Asset(occurrence.instance_of, occurrence.resource_ref))

                attributes = [attribute for attribute in topic.attributes if
                              attribute.name not in ('location', 'rotation', 'scale')]
                result.add_attributes(attributes)
        except TopicStoreException as e:
            raise CoreException(e)
        return result
