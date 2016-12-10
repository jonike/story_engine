"""
SetProp class. Part of the StoryTechnologies project.

July 16, 2016
Brett Alistair Kromkamp (brett.kromkamp@gmail.com)
"""

from storyengine.store.commands.occurrence.setoccurrencedata import SetOccurrenceData
from storyengine.store.models.topic import Topic
from storyengine.store.models.occurrence import Occurrence
from storyengine.store.models.attribute import Attribute
from storyengine.store.models.association import Association
from storyengine.core.coreerror import CoreError
from storyengine.store.commands.topic.settopic import SetTopic
from storyengine.store.commands.occurrence.setoccurrence import SetOccurrence
from storyengine.store.commands.association.setassociation import SetAssociation
from storyengine.store.commands.attribute.setattributes import SetAttributes


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
