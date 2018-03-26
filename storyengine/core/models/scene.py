"""
Scene class. Part of the StoryTechnologies project.

July 19, 2016
Brett Alistair Kromkamp (brett.kromkamp@gmail.com)
"""

from storyengine.core.models.entity import Entity


class Scene(Entity):

    def __init__(self, identifier, name='Undefined', description=None, ordinal=None):
        super().__init__(identifier, 'scene', name, description)
        self.__associations = []
        self.__entities = []  # Characters and props.
        self.__quests = []

        self.entities_tags = {}  # The tags for the entities (characters and props) in the scene.
        self.ordinal = ordinal  # The ordinal indicates the scene's position in the scene line.

    @property
    def associations(self):
        return self.__associations

    @property
    def entities(self):
        return self.__entities

    @property
    def quests(self):
        return self.__quests

    def add_association(self, association):
        self.__associations.append(association)

    def add_associations(self, associations):
        for association in associations:
            self.__associations.append(association)

    def add_entity(self, entity):
        self.__entities.append(entity)

    def add_entities(self, entities):
        for entity in entities:
            self.__entities.append(entity)

    def add_quest(self, quest):
        self.__quests.append(quest)
    
    def append_quests(self, quests):
        for quest in quests:
            self.__quests.append(quest)
