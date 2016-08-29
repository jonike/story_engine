"""
GetTagsCommand class. Part of the StoryTechnologies Builder project.

August 29, 2016
Brett Alistair Kromkamp (brett.kromkamp@gmail.com)
"""

from engine.store.topicstoreexception import TopicStoreException
from engine.store.commands.association.getassociations import GetAssociationsCommand
from engine.store.commands.association.getassociationgroups import GetAssociationGroupsCommand


class GetTagsCommand:

    def __init__(self, database_path, identifier=''):
        self.database_path = database_path
        self.identifier = identifier

    def do(self):
        if self.identifier == '':
            raise TopicStoreException("Missing 'identifier' parameter")
        result = []

        associations = GetAssociationsCommand(self.database_path, self.identifier).do()
        if associations:
            groups = GetAssociationGroupsCommand(associations=associations).do()
            for instance_of in groups.dict:
                for role in groups.dict[instance_of]:
                    for topic_ref in groups[instance_of, role]:
                        if topic_ref == self.identifier:
                            continue
                        if instance_of == 'categorization':
                            result.append(topic_ref)
        return result
