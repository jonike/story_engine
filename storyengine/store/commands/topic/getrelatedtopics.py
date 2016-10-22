"""
GetRelatedTopics class. Part of the StoryTechnologies project.

October 12, 2016
Brett Alistair Kromkamp (brett.kromkamp@gmail.com)
"""

from storyengine.store.commands.topic.gettopic import GetTopic
from storyengine.store.topicstoreexception import TopicStoreException
from storyengine.store.commands.association.getassociations import GetAssociations
from storyengine.store.commands.association.getassociationgroups import GetAssociationGroups


class GetRelatedTopics:

    def __init__(self, database_path, identifier=''):
        self.database_path = database_path
        self.identifier = identifier

    def do(self):
        if self.identifier == '':
            raise TopicStoreException("Missing 'identifier' parameter")
        result = []

        associations = GetAssociations(self.database_path, self.identifier).do()
        if associations:
            groups = GetAssociationGroups(associations=associations).do()
            for instance_of in groups.dict:
                for role in groups.dict[instance_of]:
                    for topic_ref in groups[instance_of, role]:
                        if topic_ref == self.identifier:
                            continue
                        result.append(GetTopic(self.database_path, topic_ref).do())
        return result
