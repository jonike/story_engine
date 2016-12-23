"""
GetScene class. Part of the StoryTechnologies project.

July 19, 2016
Brett Alistair Kromkamp (brett.kromkamp@gmail.com)
"""

from storyengine.core.commands.scene.getcharacter import GetCharacter
from storyengine.core.commands.scene.getprop import GetProp
from storyengine.core.commands.scene.gettags import GetEntitiesTags
from storyengine.core.coreerror import CoreError
from storyengine.core.models.asset import Asset
from storyengine.core.models.path import Path
from topicdb.core.commands.occurrence.getoccurrences import GetOccurrences
from topicdb.core.topicstoreerror import TopicStoreError
from topicdb.core.commands.topic.gettopic import GetTopic
from topicdb.core.commands.association.getassociations import GetAssociations
from topicdb.core.retrievaloption import RetrievalOption
from storyengine.core.models.scene import Scene


class GetScene:
    def __init__(self, database_path, map_identifier, identifier=''):
        self.database_path = database_path
        self.map_identifier = map_identifier
        self.identifier = identifier
        self.result = None

    def execute(self):
        if self.identifier == '':
            raise CoreError("Missing 'scene identifier' parameter")
        try:
            topic = GetTopic(self.database_path, self.map_identifier, self.identifier, RetrievalOption.resolve_attributes).execute()
            if topic:
                self.result = Scene(topic.identifier, topic.first_base_name.name,
                                    topic.get_attribute_by_name('ordinal').value)
                self.result.location = topic.get_attribute_by_name('location').value
                self.result.rotation = topic.get_attribute_by_name('rotation').value
                self.result.scale = topic.get_attribute_by_name('scale').value

                self.result.add_associations(GetAssociations(self.database_path, self.map_identifier, self.identifier).execute())

                # Add scene's entities (props and characters).
                if self.result.associations:
                    groups = self.result.association_groups
                    for instance_of in groups.dict:
                        for role in groups.dict[instance_of]:
                            for topic_ref in groups[instance_of, role]:
                                if topic_ref == self.identifier:
                                    continue
                                if instance_of == 'navigation':
                                    path = Path(role, topic_ref)
                                    self.result.add_path(path)
                                elif instance_of == 'prop':
                                    self.result.add_entity(GetProp(self.database_path, self.map_identifier, topic_ref).execute())
                                elif instance_of == 'character':
                                    self.result.add_entity(GetCharacter(self.database_path, self.map_identifier, topic_ref).execute())
                                elif instance_of == 'categorization':  # Tags.
                                    self.result.add_tag(topic_ref)

                occurrences = GetOccurrences(self.database_path, self.map_identifier, self.identifier).execute()
                for occurrence in occurrences:
                    self.result.add_asset(Asset(occurrence.instance_of, occurrence.resource_ref))

                attributes = [attribute for attribute in topic.attributes
                              if attribute.name not in ('location', 'rotation', 'scale')]
                self.result.add_attributes(attributes)
                self.result.entities_tags = GetEntitiesTags(self.database_path, self.map_identifier, self.identifier).execute()
        except TopicStoreError as error:
            raise CoreError(error)
        return self.result
