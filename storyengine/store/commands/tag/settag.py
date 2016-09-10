"""
SetTag class. Part of the StoryTechnologies Builder project.

August 29, 2016
Brett Alistair Kromkamp (brett.kromkamp@gmail.com)
"""

from storyengine.store.topicstoreexception import TopicStoreException
from storyengine.store.commands.association.setassociation import SetAssociation
from storyengine.store.commands.topic.topicexists import TopicExists
from storyengine.store.commands.topic.settopic import SetTopic
from storyengine.store.models.association import Association
from storyengine.store.models.topic import Topic


class SetTag:

    def __init__(self, database_path, identifier='', tag=''):
        self.database_path = database_path
        self.identifier = identifier
        self.tag = tag

    def do(self):
        if self.tag == '' or self.identifier == '':
            raise TopicStoreException("Missing 'tag' or 'identifier' parameter")

        if not TopicExists(self.database_path, self.identifier).do():
            identifier_topic = Topic(identifier=self.identifier, base_name=self.identifier.capitalize())
            SetTopic(self.database_path, identifier_topic).do()

        if not TopicExists(self.database_path, self.tag).do():
            tag_topic = Topic(identifier=self.tag, base_name=self.tag.capitalize())
            SetTopic(self.database_path, tag_topic).do()

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
        SetAssociation(self.database_path, tag_association1).do()
        SetAssociation(self.database_path, tag_association2).do()
