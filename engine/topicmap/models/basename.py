"""
BaseName class. Part of the StoryTechnologies Builder project.

June 12, 2016
Brett Alistair Kromkamp (brett.kromkamp@gmail.com)
"""

import uuid
import unittest

from slugify import slugify

from engine.topicmap.models.language import Language


class BaseName:

    def __init__(self,
                 name,
                 language=Language.en,
                 identifier=None):
        self.__identifier = (str(uuid.uuid1()) if identifier is None else slugify(str(identifier)))

        self.name = name
        self.language = language

    @property
    def identifier(self):
        return self.__identifier

# ===============================================================================


class BasenameTest(unittest.TestCase):

    def setUp(self):
        pass

    def testInit(self):
        pass

    def tearDown(self):
        pass

# ===============================================================================

if __name__ == '__main__':
    unittest.main()