"""
Character class. Part of the StoryTechnologies Builder project.

July 19, 2016
Brett Alistair Kromkamp (brett.kromkamp@gmail.com)
"""

from engine.core.models.entity import Entity


class Character(Entity):

    def __init__(self, identifier: str, name: str) -> object:
        super().__init__(identifier, 'character', name)

