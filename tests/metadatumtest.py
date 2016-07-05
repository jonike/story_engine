"""
MetadatumTest class. Part of the StoryTechnologies Builder project.

July 03, 2016
Brett Alistair Kromkamp (brett.kromkamp@gmail.com)
"""

import unittest

from engine.store.models.metadatum import Metadatum
from engine.store.models.datatype import DataType
from engine.store.models.language import Language


class MetadatumTest(unittest.TestCase):

    def setUp(self):
        self.metadatum1 = Metadatum('name', 'value', 'identifier-1')

    def testInit(self):
        self.assertEqual('name', self.metadatum1.name)
        self.assertEqual('value', self.metadatum1.value)
        self.assertEqual('identifier-1', self.metadatum1.entity_identifier)
        self.assertEqual(DataType.string, self.metadatum1.data_type)
        self.assertEqual('*', self.metadatum1.scope)
        self.assertEqual(Language.en, self.metadatum1.language)

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()