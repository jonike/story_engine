"""
AddCharacterCommand class. Part of the StoryTechnologies Builder project.

July 16, 2016
Brett Alistair Kromkamp (brett.kromkamp@gmail.com)
"""

from engine.store.models.topic import Topic
from engine.store.models.occurrence import Occurrence
from engine.store.models.association import Association
from engine.store.models.metadatum import Metadatum
from engine.core.coreexception import CoreException
from engine.store.commands.topic.puttopic import PutTopicCommand
from engine.store.commands.occurrence.putoccurrence import PutOccurrenceCommand
from engine.store.commands.association.putassociation import PutAssociationCommand
from engine.store.commands.metadatum.putmetadata import PutMetadataCommand


class AddCharacterCommand:

    def __init__(self, database_path, character=None, scene_identifier=''):
        self.database_path = database_path
        self.scene_identifier = scene_identifier
        self.character = character

    def do(self):
        if self.scene_identifier == '' or self.character is None:
            raise CoreException("Missing 'scene identifier' or 'character' parameter")

        topic = Topic(self.character.identifier.self.character.instance_of, self.character.name)
        PutTopicCommand(self.database_path, topic).do()

        location_metadatum = Metadatum('location', self.character.location, topic.identifier)
        rotation_metadatum = Metadatum('rotation', self.character.rotation, topic.identifier)
        scale_metadatum = Metadatum('scale', self.character.scale, topic.identifier)

        PutMetadataCommand(self.database_path, [location_metadatum, rotation_metadatum, scale_metadatum])

        for resource in self.character.resources:
            occurrence = Occurrence(
                instance_of=resource.instance_of,
                topic_identifier=topic.identifier,
                resource_ref=resource.reference)
            PutOccurrenceCommand(self.database_path, occurrence).do()

        association = Association(
            instance_of='character',
            src_topic_ref=topic.identifier,
            dest_topic_ref=self.scene_identifier,
            src_role_spec='included-in',
            dest_role_spec='part-of')
        PutAssociationCommand(self.database_path, association)
