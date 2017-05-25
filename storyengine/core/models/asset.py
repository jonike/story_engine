"""
Asset class. Part of the StoryTechnologies project.

July 19, 2016
Brett Alistair Kromkamp (brett.kromkamp@gmail.com)
"""

from storyengine.core.coreerror import CoreError


class Asset:

    def __init__(self, instance_of, reference='', data=None):

        # The 'scene' asset is a Blender/Blend4Web scene exported as JSON.
        if instance_of not in {'image', 'video', 'sound', 'scene', 'html', 'text'}:
            raise CoreError("Unrecognized 'instance of' parameter")
        self.reference = reference
        self.instance_of = instance_of
        self.data = data
