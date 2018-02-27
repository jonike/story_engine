"""
Quest class. Part of the StoryTechnologies project.

February 21, 2018
Brett Alistair Kromkamp (brett.kromkamp@gmail.com)
"""

from slugify import slugify


class Quest:

    def __init__(self, identifier,
                 name='Undefined', 
                 description=None, 
                 required=True, 
                 points=1):
        self.__identifier = slugify(str(identifier))
        self.name = name
        self.description = description
        self.required = required
        self.points = points

        self.__instance_of = 'quest'
    
    @property
    def instance_of(self):
        return self.__instance_of
