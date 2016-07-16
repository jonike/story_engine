"""
Entity class. Part of the StoryTechnologies Builder project.

June 12, 2016
Brett Alistair Kromkamp (brett.kromkamp@gmail.com)
"""

import uuid

from slugify import slugify

from engine.store.topicstoreexception import TopicStoreException


class Entity:

    def __init__(self,
                 identifier='',
                 instance_of='entity'):
        if instance_of == '':
            raise TopicStoreException("Empty 'instance of' parameter")

        if identifier == '':
            self.__identifier = str(uuid.uuid1())
        elif identifier == '*':  # Universal Scope.
            self.__identifier = '*'
        else:
            self.__identifier = slugify(str(identifier))

        self.__instance_of = slugify(str(instance_of))
        self.__metadata = []

    @property
    def identifier(self):
        return self.__identifier

    @property
    def instance_of(self):
        return self.__instance_of

    @instance_of.setter
    def instance_of(self, value):
        if value == '':
            raise TopicStoreException("Empty 'value' parameter")
        self.__instance_of = slugify(str(value))

    @property
    def metadata(self):
        return self.__metadata

    def add_metadatum(self, metadatum):
        self.__metadata.append(metadatum)

    def add_metadata(self, metadata):
        for metadatum in metadata:
            self.__metadata.append(metadatum)

    def remove_metadatum(self, identifier):
        self.__metadata[:] = [x for x in self.__metadata if x.identifier != identifier]  # TODO: Verify correctness.

    def get_metadatum(self, identifier):
        result = None
        for metadatum in self.__metadata:
            if metadatum.identifier == identifier:
                result = metadatum
                break
        return result

    def get_metadatum_by_key(self, key):
        result = None
        for metadatum in self.__metadata:
            if metadatum.key == key:
                result = metadatum
                break
        return result

    def clear_metadata(self):
        del self.__metadata[:]
