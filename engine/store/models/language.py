"""
Language enumeration. Part of the StoryTechnologies Builder project.

June 12, 2016
Brett Alistair Kromkamp (brett.kromkamp@gmail.com)
"""

from enum import Enum


class Language(Enum):
    en = 1  # English
    es = 2  # Spanish
    de = 3  # German
    it = 4  # Italian
    fr = 5  # French
    nl = 6  # Dutch
    nb = 7  # Norwegian (Bokmål)

    def __str__(self):
        return self.name
