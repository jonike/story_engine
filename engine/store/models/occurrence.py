"""
Occurrence class. Part of the StoryTechnologies Builder project.

June 12, 2016
Brett Alistair Kromkamp (brett.kromkamp@gmail.com)
"""

import uuid

from slugify import slugify

from engine.store.models.entity import Entity
from engine.store.models.language import Language


class Occurrence(Entity):

    def __init__(self,
                 identifier='',
                 instance_of='occurrence',
                 topic_identifier='',
                 scope='*',  # Universal scope
                 resource_ref='',
                 resource_data=None,
                 language=Language.en):
        super().__init__(identifier, instance_of)

        self.__topic_identifier = (str(uuid.uuid1()) if topic_identifier is '' else slugify(str(topic_identifier)))
        self.__scope = scope if scope == '*' else slugify(scope)

        self.resource_ref = resource_ref
        self.resource_data = resource_data
        self.language = language

    @property
    def scope(self):
        return self.__scope

    @scope.setter
    def scope(self, value):
        self.__scope = slugify(str(value))

    @property
    def topic_identifier(self):
        return self.__topic_identifier

    @topic_identifier.setter
    def topic_identifier(self, value):
        self.__topic_identifier = slugify(str(value))

    def has_data(self):
        return self.resource_data is not None
