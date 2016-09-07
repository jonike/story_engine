"""
AttributeTest class. Part of the StoryTechnologies Builder project.

July 03, 2016
Brett Alistair Kromkamp (brett.kromkamp@gmail.com)
"""

import unittest

from engine.store.models.attribute import Attribute
from engine.store.models.datatype import DataType
from engine.store.models.language import Language


class AttributeTest(unittest.TestCase):

    def setUp(self):
        self.attribute1 = Attribute('name', 'value', 'identifier-1')

    def testInit(self):
        self.assertEqual('name', self.attribute1.name)
        self.assertEqual('value', self.attribute1.value)
        self.assertEqual('identifier-1', self.attribute1.entity_identifier)
        self.assertEqual(DataType.string, self.attribute1.data_type)
        self.assertEqual('*', self.attribute1.scope)
        self.assertEqual(Language.en, self.attribute1.language)

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()