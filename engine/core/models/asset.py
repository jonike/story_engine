"""
Resource class. Part of the StoryTechnologies Builder project.

July 19, 2016
Brett Alistair Kromkamp (brett.kromkamp@gmail.com)
"""

from engine.core.coreexception import CoreException


class Asset:
    """
    An asset is either a character or a prop to be placed within a scene.
    """

    def __init__(self, reference, instance_of):
        if instance_of not in {'image', 'video', 'scene', 'html'}:
            raise CoreException("Unrecognized 'instance of' parameter")
        self.reference = reference
        self.instance_of = instance_of
