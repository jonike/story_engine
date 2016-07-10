"""
Metadatum class. Part of the StoryTechnologies Builder project.

June 12, 2016
Brett Alistair Kromkamp (brett.kromkamp@gmail.com)
"""

import uuid

from slugify import slugify

from engine.store.models.datatype import DataType
from engine.store.models.language import Language


class Metadatum:

    def __init__(self, name, value, entity_identifier,
                 identifier='',
                 data_type=DataType.string,
                 scope='*',
                 language=Language.en):
        self.__entity_identifier = slugify(entity_identifier)
        self.__identifier = (str(uuid.uuid1()) if identifier is '' else slugify(str(identifier)))
        self.__scope = scope if scope == '*' else slugify(scope)

        self.name = name
        self.data_type = data_type
        self.language = language
        self.value = value

    @property
    def entity_identifier(self):
        return self.__entity_identifier

    @entity_identifier.setter
    def entity_identifier(self, value):
        self.__entity_identifier = slugify(str(value))

    @property
    def identifier(self):
        return self.__identifier

    @property
    def scope(self):
        return self.__scope

    @scope.setter
    def scope(self, value):
        self.__scope = value if value == '*' else slugify(value)