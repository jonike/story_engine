"""
Scene class. Part of the StoryTechnologies Builder project.

July 19, 2016
Brett Alistair Kromkamp (brett.kromkamp@gmail.com)
"""

from engine.core.models.entity import Entity
from engine.store.commands.association.getassociationgroups import GetAssociationGroups


class Scene(Entity):

    def __init__(self, identifier: str, name: str, ordinal: int = -1) -> object:
        super().__init__(identifier, 'scene', name)
        self.__associations = []
        self.__entities = []  # Characters and props.

        self.ordinal = ordinal  # The ordinal indicates the scene's position in the sceneline.

    @property
    def associations(self):
        return self.__associations

    @property
    def association_groups(self):
        # TODO: Review. Should a model class rely on command-level functionality?
        return GetAssociationGroups(associations=self.__associations).do()

    @property
    def entities(self):
        return self.__entities

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
