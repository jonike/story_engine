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
                 location='(0.0, 0.0, 0.0)',
                 rotation='(0.0, 0.0, 0.0)',
                 scale='1.0'):
        self.__identifier = slugify(str(identifier))
        self.__instance_of = slugify(str(instance_of))
        self.name = name
        self.location = location
        self.rotation = rotation
        self.scale = scale
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

    def add_asset(self, asset):
        if isinstance(asset, Asset):
            self.__assets.append(asset)

    def add_assets(self, assets):
        for asset in assets:
            if isinstance(asset, Asset):
                self.__assets.append(asset)
