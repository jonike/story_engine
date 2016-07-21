"""
GetSceneCommand class. Part of the StoryTechnologies Builder project.

July 19, 2016
Brett Alistair Kromkamp (brett.kromkamp@gmail.com)
"""

from engine.core.coreexception import CoreException
from engine.store.topicstoreexception import TopicStoreException
from engine.store.commands.topic.gettopic import GetTopicCommand
from engine.store.commands.association.getassociations import GetAssociationsCommand
from engine.store.retrievaloption import RetrievalOption
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
            topic = GetTopicCommand(self.database_path, self.scene_identifier, RetrievalOption.resolve_metadata).do()
            if topic:
                self.result = Scene(topic.identifier, topic.first_base_name.name, topic.get_metadatum_by_name('ordinal').value)
                self.result.location = topic.get_metadatum_by_name('location').value
                self.result.rotation = topic.get_metadatum_by_name('rotation').value
                self.result.scale = topic.get_metadatum_by_name('scale').value

                self.result.add_associations(GetAssociationsCommand(self.database_path, self.scene_identifier).do())

                if self.result.associations:
                    groups = self.result.association_groups
                    for instance_of in groups.dict:
                        if instance_of == 'navigation':  # TODO: Test.
                            break
                        for role in groups.dict[instance_of]:
                            for topic_ref in groups[instance_of, role]:
                                self.result.add_entity(GetTopicCommand(self.database_path, topic_ref, RetrievalOption.resolve_metadata, RetrievalOption.resolve_occurrences).do())
        except TopicStoreException as e:
            raise CoreException(e)
        return self.result
