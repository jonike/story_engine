"""
SetAttributes class. Part of the StoryTechnologies Builder project.

July 13, 2016
Brett Alistair Kromkamp (brett.kromkamp@gmail.com)
"""

from engine.store.topicstoreexception import TopicStoreException
from engine.store.commands.attribute.setattribute import SetAttribute


class SetAttributes:

    def __init__(self, database_path, attributes=None):
        self.database_path = database_path
        self.attributes = attributes

    def do(self):
        if self.attributes is None:
            raise TopicStoreException("Missing 'attributes' parameter")

        set_attribute_command = SetAttribute(self.database_path)
        for attribute in self.attributes:
            set_attribute_command.attribute = attribute
            set_attribute_command.do()
