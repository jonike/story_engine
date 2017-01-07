"""
SetScene class. Part of the StoryTechnologies project.

July 16, 2016
Brett Alistair Kromkamp (brett.kromkamp@gmail.com)
"""

from topicdb.core.commands.occurrence.setoccurrencedata import SetOccurrenceData
from topicdb.core.commands.topic.settopic import SetTopic
from topicdb.core.commands.occurrence.setoccurrence import SetOccurrence
from topicdb.core.commands.attribute.setattributes import SetAttributes
from topicdb.core.models.topic import Topic
from topicdb.core.models.occurrence import Occurrence
from topicdb.core.models.attribute import Attribute

from storyengine.core.coreerror import CoreError


class SetScene:
    def __init__(self, database_path, topic_map_identifier, scene):
        self.database_path = database_path
        self.topic_map_identifier = topic_map_identifier
        self.scene = scene

    def execute(self):
        if self.scene is None:
            raise CoreError("Missing 'scene' parameter")
        topic = Topic(self.scene.identifier, self.scene.instance_of, self.scene.name)
        SetTopic(self.database_path, self.topic_map_identifier, topic).execute()

        location_attribute = Attribute('location', self.scene.location, topic.identifier)
        rotation_attribute = Attribute('rotation', self.scene.rotation, topic.identifier)
        scale_attribute = Attribute('scale', self.scene.scale, topic.identifier)
        ordinal_attribute = Attribute('ordinal', self.scene.ordinal, topic.identifier)

        SetAttributes(self.database_path, self.topic_map_identifier,
                      [location_attribute,
                       rotation_attribute,
                       scale_attribute,
                       ordinal_attribute]).execute()

        for asset in self.scene.assets:
            occurrence = Occurrence(
                instance_of=asset.instance_of,
                topic_identifier=topic.identifier,
                resource_ref=asset.reference)
            SetOccurrence(self.database_path, self.topic_map_identifier, occurrence).execute()
            if asset.data is not None:
                SetOccurrenceData(self.database_path, self.topic_map_identifier, occurrence.identifier, asset.data).execute()
