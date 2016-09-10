"""
Prop class. Part of the StoryTechnologies Builder project.

July 19, 2016
Brett Alistair Kromkamp (brett.kromkamp@gmail.com)
"""

from storyengine.core.models.entity import Entity


class Prop(Entity):

    def __init__(self, identifier: str, name: str) -> object:
        super().__init__(identifier, 'prop', name)

