"""
Scene class. Part of the StoryTechnologies Builder project.

July 19, 2016
Brett Alistair Kromkamp (brett.kromkamp@gmail.com)
"""

from engine.core.models.entity import Entity
from engine.store.commands.association.getassociationgroups import GetAssociationGroupsCommand


class Scene(Entity):

    def __init__(self, identifier, name, ordinal=-1):
        super().__init__(identifier, 'scene', name)
        self.__associations = []
        self.__topics = []

        self.ordinal = ordinal

    @property
    def associations(self):
        return self.__associations

    @property
    def association_groups(self):
        return GetAssociationGroupsCommand(associations=self.__associations).do()

    @property
    def topics(self):
        return self.__topics

    def add_association(self, association):
        pass

    def add_associations(self, associations):
        pass

    def add_topic(self, topic):
        pass

    def add_topics(self, topics):
        pass
