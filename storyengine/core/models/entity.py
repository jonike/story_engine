"""
Entity class. Part of the StoryTechnologies project.

July 19, 2016
Brett Alistair Kromkamp (brett.kromkamp@gmail.com)
"""

from slugify import slugify

from topicdb.core.models.attribute import Attribute

from storyengine.core.models.asset import Asset
from storyengine.core.models.path import Path


class Entity:

    def __init__(self, identifier, instance_of,
                 name='Undefined',
                 description=None,
                 location=None,
                 rotation=None,
                 scale=None):
        self.__identifier = slugify(str(identifier))
        self.__instance_of = slugify(str(instance_of))
        self.name = name
        self.description = description

        if location is None:
            self.location = '[0.0, 0.0, 0.0]'  # Vector3, with x, y and z values.
        if rotation is None:
            self.rotation = '[0.0, 0.0, 0.0]'
        if scale is None:
            self.scale = '[1.0, 1.0, 1.0]'

        self.__assets = []
        self.__paths = []
        self.__tags = []
        self.__attributes = []

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

    @property
    def attributes(self):
        return self.__attributes

    def add_attribute(self, attribute):
        if isinstance(attribute, Attribute):
            self.__attributes.append(attribute)

    def add_attributes(self, attributes):
        for attribute in attributes:
            if isinstance(attribute, Attribute):
                self.__attributes.append(attribute)
