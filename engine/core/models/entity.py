"""
Entity class. Part of the StoryTechnologies Builder project.

July 19, 2016
Brett Alistair Kromkamp (brett.kromkamp@gmail.com)
"""

from slugify import slugify

from engine.core.models.asset import Asset
from engine.core.models.path import Path


class Entity:

    def __init__(self, identifier, instance_of,
                 name='Undefined',
                 location='[0.0, 0.0, 0.0]',  # The x ("width"), y ("height"), z ("depth") coordinates.
                 rotation='[0.0, 0.0, 0.0, 0.0]',  # The x, y, z, and w coordinates.
                 scale='1.0'):
        self.__identifier = slugify(str(identifier))
        self.__instance_of = slugify(str(instance_of))
        self.name = name
        self.location = location
        self.rotation = rotation
        self.scale = scale
        self.__assets = []
        self.__paths = []
        self.__tags = []

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

    @property
    def paths(self):
        return self.__paths

    def add_path(self, path):
        if isinstance(path, Path):
            self.__paths.append(path)

    def add_paths(self, paths):
        for path in paths:
            if isinstance(path, Path):
                self.__paths.append(path)

    @property
    def tags(self):
        return self.__tags

    def add_tag(self, tag):
        if isinstance(tag, str):
            self.__tags.append(tag)

    def add_tags(self, tags):
        for tag in tags:
            if isinstance(tag, str):
                self.__tags.append(tag)
