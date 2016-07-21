"""
Topic class. Part of the StoryTechnologies Builder project.

June 12, 2016
Brett Alistair Kromkamp (brett.kromkamp@gmail.com)
"""

from engine.store.models.entity import Entity
from engine.store.models.basename import BaseName
from engine.store.models.language import Language


class Topic(Entity):

    def __init__(self,
                 identifier='',
                 instance_of='topic',
                 base_name='Undefined',
                 language=Language.en):
        super().__init__(identifier, instance_of)

        default_base_name = BaseName(base_name, language)

        self.__base_names = [default_base_name]
        self.__occurrences = []

        self.language = language

    @property
    def base_names(self):
        return self.__base_names

    @property
    def occurrences(self):
        return self.__occurrences

    @property
    def first_base_name(self, language=Language.en):
        result = None

        # Does the base name exist in the requested language?
        for base_name in self.__base_names:
            if base_name.language is language:
                result = base_name
                break

        # A base name for the requested language does not exist, fall back to the English base name.
        if result is None:
            for base_name in self.__base_names:
                if base_name.language is Language.en:
                    result = base_name
                    break

        # An English base name is not present either, hence return a base name of "Undefined" in the requested language.
        if result is None:
            if language is Language.es:
                result = BaseName("Sin Definir", Language.es)
            elif language is Language.de:
                result = BaseName("Undefiniert", Language.de)
            elif language is Language.it:
                result = BaseName("Indefinito", Language.it)
            elif language is Language.fr:
                result = BaseName("Indéfini", Language.fr)
            elif language is Language.nl:
                result = BaseName("Onbepaald", Language.nl)
            elif language is Language.nb:
                result = BaseName("Ikke Definert", Language.nb)  # Norwegian (Bokmål)
            else:
                result = BaseName("Undefined", Language.en)
        return result

    def get_base_name(self, identifier):
        result = None
        for base_name in self.__base_names:
            if base_name.identifier == identifier:
                result = base_name
                break
        return result

    def add_base_name(self, base_name):
        self.__base_names.append(base_name)

    def add_base_names(self, base_names):
        for base_name in base_names:
            self.__base_names.append(base_name)

    def remove_base_name(self, identifier):
        self.__base_names[:] = [x for x in self.__base_names if x.identifier != identifier]

    def clear_base_names(self):
        del self.__base_names[:]

    def add_occurrence(self, occurrence):
        occurrence.topic_identifier = self.identifier
        self.__occurrences.append(occurrence)

    def add_occurrences(self, occurrences):
        for occurrence in occurrences:
            occurrence.topic_identifier = self.identifier
            self.__occurrences.append(occurrence)

    def remove_occurrence(self, identifier):
        self.__occurrences[:] = [x for x in self.__occurrences if x.identifier != identifier]

    def get_occurrence(self, identifier):
        result = None
        for occurrence in self.__occurrences:
            if occurrence.identifier == identifier:
                result = occurrence
                break
        return result

    def clear_occurrences(self):
        del self.__occurrences[:]
