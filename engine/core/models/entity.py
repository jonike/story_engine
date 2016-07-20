"""
Entity class. Part of the StoryTechnologies Builder project.

July 19, 2016
Brett Alistair Kromkamp (brett.kromkamp@gmail.com)
"""

from slugify import slugify

from engine.core.models.asset import Asset


class Entity:

    def __init__(self, identifier, instance_of,
                 name='Undefined',
                 location=(0.0, 0.0, 0.0),
                 rotation=(0.0, 0.0, 0.0),
                 scale=1.0):
        self.__identifier = slugify(str(identifier))
        self.__instance_of = slugify(str(instance_of))
        self.__name = name
        self.__location = location
        self.__rotation = rotation
        self.__scale = scale
        self.__assets = []

    @property
    def identifier(self):
        return self.__identifier

    @property
    def instance_of(self):
        return self.__instance_of

    @property
    def assets(self):
        return self.__assets

    @property
    def location(self):
        return self.__location

    @location.setter
    def location(self, value):
        self.__location = value

    @property
    def rotation(self):
        return self.__rotation

    @rotation.setter
    def rotation(self, value):
        self.__rotation = value

    @property
    def scale(self):
        return self.__scale

    @scale.setter
    def scale(self, value):
        self.__scale = value

    def add_asset(self, asset):
        if isinstance(asset, Asset):
            self.__assets.append(asset)

    def add_assets(self, assets):
        for asset in assets:
            if isinstance(asset, Asset):
                self.__assets.append(asset)
