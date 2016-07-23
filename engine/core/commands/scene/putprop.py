"""
PutPropCommand class. Part of the StoryTechnologies Builder project.

July 16, 2016
Brett Alistair Kromkamp (brett.kromkamp@gmail.com)
"""

from engine.store.models.topic import Topic
from engine.store.models.occurrence import Occurrence
from engine.store.models.metadatum import Metadatum
from engine.store.models.association import Association
from engine.core.coreexception import CoreException
from engine.store.commands.topic.puttopic import PutTopicCommand
from engine.store.commands.occurrence.putoccurrence import PutOccurrenceCommand
from engine.store.commands.association.putassociation import PutAssociationCommand
from engine.store.commands.metadatum.putmetadata import PutMetadataCommand


class PutPropCommand:

    def __init__(self, database_path,
                 prop=None,
                 scene_identifier=''):
        self.database_path = database_path
        self.scene_identifier = scene_identifier
        self.prop = prop

    def do(self):
        if self.scene_identifier == '' or self.prop is None:
            raise CoreException("Missing 'scene identifier' or 'property' parameter")

        topic = Topic(self.prop.identifier, self.prop.instance_of, self.prop.name)
        PutTopicCommand(self.database_path, topic).do()

        location_metadatum = Metadatum('location', self.prop.location, topic.identifier)
        rotation_metadatum = Metadatum('rotation', self.prop.rotation, topic.identifier)
        scale_metadatum = Metadatum('scale', self.prop.scale, topic.identifier)

        PutMetadataCommand(self.database_path, [location_metadatum, rotation_metadatum, scale_metadatum]).do()

        for asset in self.prop.assets:
            occurrence = Occurrence(
                instance_of=asset.instance_of,
                topic_identifier=topic.identifier,
                resource_ref=asset.reference)
            PutOccurrenceCommand(self.database_path, occurrence).do()

        association = Association(
            instance_of='prop',
            src_topic_ref=topic.identifier,
            dest_topic_ref=self.scene_identifier,
            src_role_spec='included-in',
            dest_role_spec='part-of')
        PutAssociationCommand(self.database_path, association).do()
