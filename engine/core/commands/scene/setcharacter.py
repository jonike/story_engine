"""
SetCharacter class. Part of the StoryTechnologies Builder project.

July 16, 2016
Brett Alistair Kromkamp (brett.kromkamp@gmail.com)
"""
from engine.store.commands.occurrence.setoccurrencedata import SetOccurrenceData
from engine.store.models.topic import Topic
from engine.store.models.occurrence import Occurrence
from engine.store.models.association import Association
from engine.store.models.attribute import Attribute
from engine.core.coreexception import CoreException
from engine.store.commands.topic.settopic import SetTopic
from engine.store.commands.occurrence.setoccurrence import SetOccurrence
from engine.store.commands.association.setassociation import SetAssociation
from engine.store.commands.attribute.setattributes import SetAttributes


class SetCharacter:

    def __init__(self, database_path,
                 character=None,
                 scene_identifier=''):
        self.database_path = database_path
        self.scene_identifier = scene_identifier
        self.character = character

    def do(self):
        if self.scene_identifier == '' or self.character is None:
            raise CoreException("Missing 'scene identifier' or 'character' parameter")

        topic = Topic(self.character.identifier, self.character.instance_of, self.character.name)
        SetTopic(self.database_path, topic).do()

        location_attribute = Attribute('location', self.character.location, topic.identifier)
        rotation_attribute = Attribute('rotation', self.character.rotation, topic.identifier)
        scale_attribute = Attribute('scale', self.character.scale, topic.identifier)

        SetAttributes(self.database_path, [location_attribute, rotation_attribute, scale_attribute]).do()

        for asset in self.character.assets:
            occurrence = Occurrence(
                instance_of=asset.instance_of,
                topic_identifier=topic.identifier,
                resource_ref=asset.reference)
            SetOccurrence(self.database_path, occurrence).do()
            if asset.data is not None:
                SetOccurrenceData(self.database_path, occurrence.identifier, asset.data).do()

        association = Association(
            instance_of='character',
            src_topic_ref=topic.identifier,  # The character's reference.
            dest_topic_ref=self.scene_identifier,
            src_role_spec='included-in',
            dest_role_spec='includes')
        SetAssociation(self.database_path, association).do()
