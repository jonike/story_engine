"""
Resource class. Part of the StoryTechnologies Builder project.

July 19, 2016
Brett Alistair Kromkamp (brett.kromkamp@gmail.com)
"""

from engine.core.models.entity import Entity
from engine.core.coreexception import CoreException


class Asset(Entity):

    def __init__(self, reference, instance_of):
        if instance_of not in {'image', 'video', 'scene'}:
            raise CoreException("Unrecognized 'instance of' parameter")
        self.reference = reference
        self.instance_of = instance_of
