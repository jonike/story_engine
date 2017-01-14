"""
GetTags class. Part of the StoryTechnologies project.

October 12, 2016
Brett Alistair Kromkamp (brett.kromkamp@gmail.com)
"""

from topicdb.core.commands.association.getassociationgroups import GetAssociationGroups
from topicdb.core.commands.tag.gettags import GetTags
from topicdb.core.commands.topicstoreerror import TopicStoreError


class GetEntitiesTags:

    def __init__(self, database_path, topic_map_identifier, identifier=''):
        self.database_path = database_path
        self.topic_map_identifier = topic_map_identifier
        self.identifier = identifier

    def execute(self):
        if self.identifier == '':
            raise TopicStoreError("Missing 'identifier' parameter")
        result = {}

        # Map from topics with tags to tags with topics. For example, the below topic -> tags mappings:
        # topic1 -> tag1, tag2, tag3
        # topic2 -> tag2, tag4
        # topic3 -> tag3, tag4, tag5
        # topic4 -> tag4, tag5, tag6, tag7
        # topic5 -> tag1, tag8
        #
        # Should become the following tag -> topics mappings:
        # tag1 -> topic1, topic5
        # tag2 -> topic1, topic2
        # tag3 -> topic1, topic3
        # tag4 -> topic2, topic3, topic4
        # tag5 -> topic3, topic4
        # tag6 -> topic4
        # tag7 -> topic4
        # tag8 -> topic5

        topic_tags = {}
        groups = GetAssociationGroups(self.database_path, self.topic_map_identifier, self.identifier).execute()
        for instance_of in groups.dict:
            for role in groups.dict[instance_of]:
                for topic_ref in groups[instance_of, role]:
                    if topic_ref == self.identifier:
                        continue
                    if instance_of == 'prop' or instance_of == 'character':
                        topic_tags[topic_ref] = GetTags(self.database_path, self.topic_map_identifier, topic_ref).execute()

        for topic, tags in topic_tags.items():
            for tag in tags:
                if tag not in result.keys():
                    result[tag] = {topic}  # Topics set. Will guarantee that topic identifiers are unique for each tag.
                else:
                    result[tag].add(topic)
        return result
