"""
Demo 2 procedural definition script. Part of the StoryTechnologies project.

November 11, 2016
Brett Alistair Kromkamp (brett.kromkamp@gmail.com)
"""

import os.path

from storyengine.store.commands.attribute.setattribute import SetAttribute
from storyengine.store.commands.map.createmap import CreateMap
from storyengine.store.commands.map.initmap import InitMap
from storyengine.store.commands.tag.settags import SetTags
from storyengine.store.commands.topic.topicexists import TopicExists
from storyengine.store.models.attribute import Attribute
from storyengine.core.commands.scene.setcharacter import SetCharacter
from storyengine.core.commands.scene.setprop import SetProp
from storyengine.core.commands.scene.setscene import SetScene
from storyengine.core.commands.scene.setnavigation import SetNavigation
from storyengine.core.models.character import Character
from storyengine.core.models.prop import Prop
from storyengine.core.models.scene import Scene
from storyengine.core.models.asset import Asset

from storyengine.store.models.occurrence import Occurrence
from storyengine.store.commands.occurrence.setoccurrence import SetOccurrence


database_path = '/home/brettk/Source/storytechnologies/story_engine/data/demo2.sqlite'

# Create and bootstrap topic map (ontology).
if not os.path.isfile(database_path):
    CreateMap(database_path).do()

if not TopicExists(database_path, 'genesis').do():
    InitMap(database_path).do()


# Scene 01 - Cafeteria.
asset11 = Asset('scene', 'scene-012.json')
scene1 = Scene('cafeteria', 'Cafeteria', 1)
scene1.add_asset(asset11)
scene1_text = """
"""
asset12 = Asset('text', data=scene1_text)
scene1.add_asset(asset12)
SetScene(database_path, scene1).do()
attribute11 = Attribute('type', 'exterior', 'outpost')
SetAttribute(database_path, attribute11).do()


# Scene 02 - House.


# Scene 01 - Living Room.


# Scene 01 - Bedroom.