"""
Story class. Part of the StoryTechnologies project.

November 26, 2016
Brett Alistair Kromkamp (brett.kromkamp@gmail.com)
"""


class Story:

    def __init__(self, title, topic_map_identifier,
                 start_scene_identifier='genesis',
                 description=''):
        self.__identifier = None
        self.title = title
        self.topic_map_identifier = topic_map_identifier
        self.start_scene_identifier = start_scene_identifier
        self.description = description

    @property
    def identifier(self):
        return self.__identifier

    @identifier.setter
    def identifier(self, value):
        if self.__identifier is None:
            self.__identifier = value
