"""
SetAttributes class. Part of the StoryTechnologies project.

July 13, 2016
Brett Alistair Kromkamp (brett.kromkamp@gmail.com)
"""

from storyengine.store.topicstoreexception import TopicStoreException
from storyengine.store.commands.attribute.setattribute import SetAttribute


class SetAttributes:

    def __init__(self, database_path, map_identifier, attributes=None):
        self.database_path = database_path
        self.map_identifier = map_identifier
        self.attributes = attributes

    def do(self):
        if self.attributes is None:
            raise TopicStoreException("Missing 'attributes' parameter")

        set_attribute_command = SetAttribute(self.database_path, self.map_identifier)
        for attribute in self.attributes:
            set_attribute_command.attribute = attribute
            set_attribute_command.do()
