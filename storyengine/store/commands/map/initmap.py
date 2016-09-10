"""
InitMap class. Part of the StoryTechnologies Builder project.

July 16, 2016
Brett Alistair Kromkamp (brett.kromkamp@gmail.com)
"""

from storyengine.store.models.topic import Topic
from storyengine.store.commands.topic.settopic import SetTopic
from storyengine.store.commands.map.topicfield import TopicField


class InitMap:

    def __init__(self, database_path):
        self.database_path = database_path
        self.items = {
            ('entity', 'Entity'),
            ('topic', 'Topic'),
            ('association', 'Association'),
            ('occurrence', 'Occurrence'),
            ('*', 'Universal Scope'),
            ('genesis', 'Genesis'),
            ('navigation', 'Navigation'),
            ('member', 'Member'),
            ('category', 'Category'),
            ('categorization', 'Categorization'),
            ('tags', 'Tags'),
            ('broader', 'Broader'),
            ('narrower', 'Narrower'),
            ('related', 'Related'),
            ('parent', 'Parent'),
            ('child', 'Child'),
            ('previous', 'Previous'),
            ('next', 'Next'),
            ('includes', 'Includes'),
            ('included-in', 'Is Included In'),
            ('story', 'Story'),
            ('book', 'Book'),
            ('chapter', 'Chapter'),
            ('scene', 'Scene'),
            ('prop', 'Prop'),
            ('character', 'Character'),
            ('image', 'Image'),
            ('video', 'Video'),
            ('text', 'Text'),
            ('html', 'HTML'),
            ('dialogue', 'Dialogue'),
            ('up', 'Up'),
            ('down', 'Down'),
            ('north', 'North'),
            ('north-east', 'Northeast'),
            ('east', 'East'),
            ('south-east', 'Southeast'),
            ('south', 'South'),
            ('south-west', 'Southwest'),
            ('west', 'West'),
            ('north-west', 'Northwest')
        }

    def do(self):

        set_topic_command = SetTopic(self.database_path)
        for item in self.items:
            topic = Topic(identifier=item[TopicField.identifier.value], base_name=item[TopicField.base_name.value])
            set_topic_command.topic = topic
            set_topic_command.do()
