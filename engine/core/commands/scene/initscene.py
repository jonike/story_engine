"""
InitSceneCommand class. Part of the StoryTechnologies Builder project.

July 16, 2016
Brett Alistair Kromkamp (brett.kromkamp@gmail.com)
"""

from engine.store.models.topic import Topic
from engine.store.models.occurrence import Occurrence
from engine.store.models.metadatum import Metadatum
from engine.core.coreexception import CoreException
from engine.store.commands.topic.puttopic import PutTopicCommand
from engine.store.commands.occurrence.putoccurrence import PutOccurrenceCommand
from engine.store.commands.metadatum.putmetadata import PutMetadataCommand


class InitSceneCommand:

    def __init__(self, database_path, scene):
        self.database_path = database_path
        self.scene = scene

    def do(self):
        if self.scene is None:
            raise CoreException("Missing 'scene' parameter")
        topic = Topic(self.scene.identifier. self.scene.instance_of, self.scene.name)
        PutTopicCommand(self.database_path, topic).do()

        location_metadatum = Metadatum('location', self.scene.location, topic.identifier)
        rotation_metadatum = Metadatum('rotation', self.scene.rotation, topic.identifier)
        scale_metadatum = Metadatum('scale', self.scene.scale, topic.identifier)

        PutMetadataCommand(self.database_path, [location_metadatum, rotation_metadatum, scale_metadatum])

        for resource in self.scene.resources:
            occurrence = Occurrence(
                instance_of=resource.instance_of,
                topic_identifier=topic.identifier,
                resource_ref=resource.reference)
            PutOccurrenceCommand(self.database_path, occurrence).do()
