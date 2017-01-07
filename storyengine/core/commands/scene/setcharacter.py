"""
SetCharacter class. Part of the StoryTechnologies project.

July 16, 2016
Brett Alistair Kromkamp (brett.kromkamp@gmail.com)
"""

from topicdb.core.commands.occurrence.setoccurrencedata import SetOccurrenceData
from topicdb.core.commands.topic.settopic import SetTopic
from topicdb.core.commands.occurrence.setoccurrence import SetOccurrence
from topicdb.core.commands.association.setassociation import SetAssociation
from topicdb.core.commands.attribute.setattributes import SetAttributes
from topicdb.core.models.topic import Topic
from topicdb.core.models.occurrence import Occurrence
from topicdb.core.models.association import Association
from topicdb.core.models.attribute import Attribute

from storyengine.core.coreerror import CoreError


class SetCharacter:

    def __init__(self, database_path, topic_map_identifier,
                 character=None,
                 scene_identifier=''):
        self.database_path = database_path
        self.topic_map_identifier = topic_map_identifier
        self.scene_identifier = scene_identifier
        self.character = character

    def execute(self):
        if self.scene_identifier == '' or self.character is None:
            raise CoreError("Missing 'scene identifier' or 'character' parameter")

        topic = Topic(self.character.identifier, self.character.instance_of, self.character.name)
        SetTopic(self.database_path, self.topic_map_identifier, topic).execute()

        location_attribute = Attribute('location', self.character.location, topic.identifier)
        rotation_attribute = Attribute('rotation', self.character.rotation, topic.identifier)
        scale_attribute = Attribute('scale', self.character.scale, topic.identifier)

        SetAttributes(self.database_path, self.topic_map_identifier, [location_attribute, rotation_attribute, scale_attribute]).execute()

        for asset in self.character.assets:
            occurrence = Occurrence(
                instance_of=asset.instance_of,
                topic_identifier=topic.identifier,
                resource_ref=asset.reference)
            SetOccurrence(self.database_path, self.topic_map_identifier, occurrence).execute()
            if asset.data is not None:
                SetOccurrenceData(self.database_path, self.topic_map_identifier, occurrence.identifier, asset.data).execute()

        association = Association(
            instance_of='character',
            src_topic_ref=topic.identifier,  # The character's reference.
            dest_topic_ref=self.scene_identifier,
            src_role_spec='included-in',
            dest_role_spec='includes')
        SetAssociation(self.database_path, self.topic_map_identifier, association).execute()
