"""
CoreException class. Part of the StoryTechnologies Builder project.

July 16, 2016
Brett Alistair Kromkamp (brett.kromkamp@gmail.com)
"""


class CoreException(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)
