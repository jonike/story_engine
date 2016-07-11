"""
BaseName class. Part of the StoryTechnologies Builder project.

June 12, 2016
Brett Alistair Kromkamp (brett.kromkamp@gmail.com)
"""

import uuid

from slugify import slugify

from engine.store.models.language import Language


class BaseName:

    def __init__(self,
                 name,
                 language=Language.en,
                 identifier=''):
        self.__identifier = (str(uuid.uuid1()) if identifier == '' else slugify(str(identifier)))

        self.name = name
        self.language = language

    @property
    def identifier(self):
        return self.__identifier

