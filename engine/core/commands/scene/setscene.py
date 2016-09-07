"""
SetScene class. Part of the StoryTechnologies Builder project.

July 16, 2016
Brett Alistair Kromkamp (brett.kromkamp@gmail.com)
"""
from engine.store.commands.occurrence.setoccurrencedata import SetOccurrenceData
from engine.store.models.topic import Topic
from engine.store.models.occurrence import Occurrence
from engine.store.models.metadatum import Metadatum
from engine.core.coreexception import CoreException
from engine.store.commands.topic.settopic import SetTopic
from engine.store.commands.occurrence.setoccurrence import SetOccurrence
from engine.store.commands.metadatum.setmetadata import SetMetadata


class SetScene:

    def __init__(self, database_path, scene):
        self.database_path = database_path
        self.scene = scene

    def do(self):
        if self.scene is None:
            raise CoreException("Missing 'scene' parameter")
        topic = Topic(self.scene.identifier, self.scene.instance_of, self.scene.name)
        SetTopic(self.database_path, topic).do()

        location_metadatum = Metadatum('location', self.scene.location, topic.identifier)
        rotation_metadatum = Metadatum('rotation', self.scene.rotation, topic.identifier)
        scale_metadatum = Metadatum('scale', self.scene.scale, topic.identifier)
        ordinal_metadatum = Metadatum('ordinal', self.scene.ordinal, topic.identifier)

        SetMetadata(self.database_path,
                           [location_metadatum,
                            rotation_metadatum,
                            scale_metadatum,
                            ordinal_metadatum]).do()

        for asset in self.scene.assets:
            occurrence = Occurrence(
                instance_of=asset.instance_of,
                topic_identifier=topic.identifier,
                resource_ref=asset.reference)
            SetOccurrence(self.database_path, occurrence).do()
            if asset.data is not None:
                SetOccurrenceData(self.database_path, occurrence.identifier, asset.data).do()
