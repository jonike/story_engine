"""
SetProp class. Part of the StoryTechnologies project.

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
from topicdb.core.models.attribute import Attribute
from topicdb.core.models.association import Association

from storyengine.core.coreerror import CoreError


class SetProp:

    def __init__(self, database_path, map_identifier,
                 prop=None,
                 scene_identifier=''):
        self.database_path = database_path
        self.map_identifier = map_identifier
        self.scene_identifier = scene_identifier
        self.prop = prop

    def execute(self):
        if self.scene_identifier == '' or self.prop is None:
            raise CoreError("Missing 'scene identifier' or 'property' parameter")

        topic = Topic(self.prop.identifier, self.prop.instance_of, self.prop.name)
        SetTopic(self.database_path, self.map_identifier, topic).execute()

        location_attribute = Attribute('location', self.prop.location, topic.identifier)
        rotation_attribute = Attribute('rotation', self.prop.rotation, topic.identifier)
        scale_attribute = Attribute('scale', self.prop.scale, topic.identifier)

        SetAttributes(self.database_path, self.map_identifier, [location_attribute, rotation_attribute, scale_attribute]).execute()

        for asset in self.prop.assets:
            occurrence = Occurrence(
                instance_of=asset.instance_of,
                topic_identifier=topic.identifier,
                resource_ref=asset.reference)
            SetOccurrence(self.database_path, self.map_identifier, occurrence).execute()
            if asset.data is not None:
                SetOccurrenceData(self.database_path, self.map_identifier, occurrence.identifier, asset.data).execute()

        association = Association(
            instance_of='prop',
            src_topic_ref=topic.identifier,  # The prop's reference.
            dest_topic_ref=self.scene_identifier,
            src_role_spec='included-in',
            dest_role_spec='includes')
        SetAssociation(self.database_path, self.map_identifier, association).execute()
