"""
Association class. Part of the StoryTechnologies Builder project.

July 03, 2016
Brett Alistair Kromkamp (brett.kromkamp@gmail.com)
"""

from engine.topicmap.models.topic import Topic


class Association(Topic):

    def __init__(self, identifier=None, instance_of='association'):
        super.__init__(identifier, instance_of)
