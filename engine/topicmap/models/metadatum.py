"""
Metadatum class. Part of the StoryTechnologies Builder project.

June 12, 2016
Brett Alistair Kromkamp (brett.kromkamp@gmail.com)
"""

import uuid
import unittest

from slugify import slugify

from engine.topicmap.models.datatype import DataType
from engine.topicmap.models.language import Language


class Metadatum:

    def __init__(self, key, value, entity_identifier,
                 identifier=None,
                 data_type=DataType.string,
                 scope='*',
                 language=Language.en):
        self.__entity_identifier = slugify(entity_identifier)
        self.__identifier = (str(uuid.uuid1()) if identifier is None else slugify(str(identifier)))
        self.__scope = scope if scope == '*' else slugify(scope)

        self.key = key
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

# ===============================================================================


class MetadatumTest(unittest.TestCase):

    def setUp(self):
        self.metadatum1 = Metadatum('key', 'value', 'identifier-1')

    def testInit(self):
        self.assertEqual('key', self.metadatum1.key)
        self.assertEqual('value', self.metadatum1.value)
        self.assertEqual('identifier-1', self.metadatum1.entity_identifier)
        self.assertEqual(DataType.string, self.metadatum1.data_type)
        self.assertEqual('*', self.metadatum1.scope)
        self.assertEqual(Language.en, self.metadatum1.language)

    def tearDown(self):
        pass

# ===============================================================================

if __name__ == '__main__':
    unittest.main()