"""
Scene class. Part of the StoryTechnologies Builder project.

July 19, 2016
Brett Alistair Kromkamp (brett.kromkamp@gmail.com)
"""

from engine.core.models.entity import Entity


class Scene(Entity):

    def __init__(self, identifier, name):
        super().__init__(identifier, 'scene', name)
