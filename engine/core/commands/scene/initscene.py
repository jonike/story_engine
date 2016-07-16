"""
InitSceneCommand class. Part of the StoryTechnologies Builder project.

July 16, 2016
Brett Alistair Kromkamp (brett.kromkamp@gmail.com)
"""

from engine.store.commands.topic.topicexists import TopicExistsCommand
from engine.store.commands.topic.puttopic import PutTopicCommand
from engine.store.models.topic import Topic
from engine.store.models.metadatum import Metadatum

from engine.core.commands.scene.sceneexception import SceneException


class InitSceneCommand:

    def __init__(self, database_path,
                 scene_identifier='',
                 location=None,
                 rotation=None,
                 scale=None):
        self.database_path = database_path
        self.scene_identifier = scene_identifier
        self.location = location
        self.rotation = rotation
        self.scale = scale

    def do(self):
        if self.scene_identifier == '':
            raise SceneException("Missing 'scene identifier' parameter")
