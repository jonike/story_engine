"""
SetTagCommand class. Part of the StoryTechnologies Builder project.

August 29, 2016
Brett Alistair Kromkamp (brett.kromkamp@gmail.com)
"""

from engine.store.topicstoreexception import TopicStoreException
from engine.store.commands.association.setassociation import SetAssociationCommand
from engine.store.commands.topic.topicexists import TopicExistsCommand
from engine.store.commands.topic.settopic import SetTopicCommand
from engine.store.models.association import Association
from engine.store.models.topic import Topic


class SetTagCommand:

    def __init__(self, database_path, identifier='', tag=''):
        self.database_path = database_path
        self.identifier = identifier
        self.tag = tag

    def do(self):
        if self.tag == '' or self.identifier == '':
            raise TopicStoreException("Missing 'tag' or 'identifier' parameter")

        if not TopicExistsCommand(self.database_path, self.identifier).do():
            identifier_topic = Topic(identifier=self.identifier, base_name=self.identifier.capitalize())
            SetTopicCommand(self.database_path, identifier_topic).do()

        if not TopicExistsCommand(self.database_path, self.tag).do():
            tag_topic = Topic(identifier=self.tag, base_name=self.tag.capitalize())
            SetTopicCommand(self.database_path, tag_topic).do()

        tag_association1 = Association(
            instance_of='categorization',
            src_topic_ref=self.identifier,
            dest_topic_ref=self.tag,
            src_role_spec='member',
            dest_role_spec='category')
        tag_association2 = Association(
            instance_of='categorization',
            src_topic_ref='tags',
            dest_topic_ref=self.tag,
            src_role_spec='broader',
            dest_role_spec='narrower')
        SetAssociationCommand(self.database_path, tag_association1).do()
        SetAssociationCommand(self.database_path, tag_association2).do()
