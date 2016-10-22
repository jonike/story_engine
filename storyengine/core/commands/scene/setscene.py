"""
SetScene class. Part of the StoryTechnologies project.

July 16, 2016
Brett Alistair Kromkamp (brett.kromkamp@gmail.com)
"""
from storyengine.store.commands.occurrence.setoccurrencedata import SetOccurrenceData
from storyengine.store.models.topic import Topic
from storyengine.store.models.occurrence import Occurrence
from storyengine.store.models.attribute import Attribute
from storyengine.core.coreexception import CoreException
from storyengine.store.commands.topic.settopic import SetTopic
from storyengine.store.commands.occurrence.setoccurrence import SetOccurrence
from storyengine.store.commands.attribute.setattributes import SetAttributes


class SetScene:
    def __init__(self, database_path, scene):
        self.database_path = database_path
        self.scene = scene

    def do(self):
        if self.scene is None:
            raise CoreException("Missing 'scene' parameter")
        topic = Topic(self.scene.identifier, self.scene.instance_of, self.scene.name)
        SetTopic(self.database_path, topic).do()

        location_attribute = Attribute('location', self.scene.location, topic.identifier)
        rotation_attribute = Attribute('rotation', self.scene.rotation, topic.identifier)
        scale_attribute = Attribute('scale', self.scene.scale, topic.identifier)
        ordinal_attribute = Attribute('ordinal', self.scene.ordinal, topic.identifier)

        SetAttributes(self.database_path,
                      [location_attribute,
                       rotation_attribute,
                       scale_attribute,
                       ordinal_attribute]).do()

        for asset in self.scene.assets:
            occurrence = Occurrence(
                instance_of=asset.instance_of,
                topic_identifier=topic.identifier,
                resource_ref=asset.reference)
            SetOccurrence(self.database_path, occurrence).do()
            if asset.data is not None:
                SetOccurrenceData(self.database_path, occurrence.identifier, asset.data).do()
