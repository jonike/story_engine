"""
Demo 2 procedural definition script. Part of the StoryTechnologies project.

November 11, 2016
Brett Alistair Kromkamp (brett.kromkamp@gmail.com)
"""

import os

from storyengine.core.commands.story.setstory import SetStory
from storyengine.core.models.story import Story
from topicdb.core.commands.attribute.setattribute import SetAttribute
from topicdb.core.commands.map.createmap import CreateMap
from topicdb.core.commands.map.initmap import InitMap
from topicdb.core.commands.topic.settopic import SetTopic
from topicdb.core.commands.topic.topicexists import TopicExists
from topicdb.core.models.attribute import Attribute
from storyengine.core.commands.scene.setscene import SetScene
from storyengine.core.models.scene import Scene
from storyengine.core.models.asset import Asset

from topicdb.core.models.topic import Topic

DATABASE_PATH = os.path.join(os.path.dirname(__file__), '../data/stories.db')
MAP_IDENTIFIER = 2

# Create and bootstrap topic map (ontology).
if not os.path.isfile(DATABASE_PATH):
    CreateMap(DATABASE_PATH).execute()

if not TopicExists(DATABASE_PATH, MAP_IDENTIFIER, 'genesis').execute():
    InitMap(DATABASE_PATH, MAP_IDENTIFIER).execute()

# Story.
story = Story("An Unexpected Meeting", MAP_IDENTIFIER, "cafeteria")
SetStory(DATABASE_PATH, story).execute()

# Scene 01 - Cafeteria.
asset11 = Asset('scene', 'scene-012.json')
scene1 = Scene('cafeteria', 'Cafeteria', 1)
scene1.add_asset(asset11)
scene1_text = """A cafeteria is a type of food service location in which there is little or no waiting staff table
service, whether a restaurant or within an institution such as a large office building or school; a school dining
location is also referred to as a dining hall or canteen (in British English). Cafeterias are different from
coffeehouses, despite being the Spanish translation of the English term.
"""
asset12 = Asset('text', data=scene1_text)
scene1.add_asset(asset12)
SetScene(DATABASE_PATH, MAP_IDENTIFIER, scene1).execute()
attribute11 = Attribute('type', 'exterior', 'cafeteria')
SetAttribute(DATABASE_PATH, MAP_IDENTIFIER, attribute11).execute()


# Scene 02 - House.


# Scene 01 - Living Room.


# Scene 01 - Bedroom.


# Annotations
annotation1 = Topic('palm-tree', 'annotation', 'Palm Tree')
SetTopic(DATABASE_PATH, MAP_IDENTIFIER, annotation1).execute()

annotation2 = Topic('street-lamp', 'annotation', 'Street Lamp')
SetTopic(DATABASE_PATH, MAP_IDENTIFIER, annotation2).execute()

annotation3 = Topic('trash-cans', 'annotation', 'Trash Cans')
SetTopic(DATABASE_PATH, MAP_IDENTIFIER, annotation3).execute()

annotation4 = Topic('chimney', 'annotation', 'Chimney')
SetTopic(DATABASE_PATH, MAP_IDENTIFIER, annotation4).execute()

