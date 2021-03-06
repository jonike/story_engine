"""
Demo 2 procedural definition script. Part of the StoryTechnologies project.

November 11, 2016
Brett Alistair Kromkamp (brett.kromkamp@gmail.com)
"""

import os
import configparser

from topicdb.core.models.attribute import Attribute
from topicdb.core.models.occurrence import Occurrence
from topicdb.core.models.topic import Topic

from storyengine.core.store.scenestore import SceneStore
from storyengine.core.models.scene import Scene
from storyengine.core.models.asset import Asset


TOPIC_MAP_IDENTIFIER = 2
SETTINGS_FILE_PATH = os.path.join(os.path.dirname(__file__), '../settings.ini')

config = configparser.ConfigParser()
config.read(SETTINGS_FILE_PATH)

username = config['DATABASE']['Username']
password = config['DATABASE']['Password']

# Instantiate and open the scene store.
scene_store = SceneStore(username, password)
scene_store.open()


# Genesis topic.
attribute01 = Attribute('entry-scene', 'cafeteria', 'genesis')
scene_store.set_attribute(TOPIC_MAP_IDENTIFIER, attribute01)

story_text = """An unexpected or casual meeting with someone or something. She felt totally unnerved by the encounter. I told them of my encounter with the __cardinal__. What do we know about the people we encounter in our daily lives?

Unexpectedly be faced with or experience (something hostile or difficult). The guides will help if you encounter any problems.
"""
story_text_occurrence = Occurrence(topic_identifier='genesis', instance_of='text', resource_data=bytes(story_text, 'utf-8'))
scene_store.set_occurrence(TOPIC_MAP_IDENTIFIER, story_text_occurrence)

story_image_occurrence = Occurrence(topic_identifier='genesis', instance_of='image', resource_ref='town.png')
scene_store.set_occurrence(TOPIC_MAP_IDENTIFIER, story_image_occurrence)



# Scene 01 - Cafeteria.
asset11 = Asset('scene', 'scene-012.json')
scene1 = Scene('cafeteria', 'Cafeteria',
               description='A lunchroom or dining hall, as in a factory, office, or school, where food is served from counters or dispensed from vending machines.',
               ordinal=1)
scene1.add_asset(asset11)
scene1_text = """A cafeteria is a type of __food service location__ in which there is little or no waiting staff table
service, whether a restaurant or within an institution such as a large office building or school; a __school dining
location__ is also referred to as a dining hall or canteen (in British English). Cafeterias are different from
__coffeehouses__, despite being the Spanish translation of the English term.
"""
asset12 = Asset('text', data=scene1_text)
scene1.add_asset(asset12)
scene_store.set_scene(TOPIC_MAP_IDENTIFIER, scene1)
attribute11 = Attribute('type', 'exterior', 'cafeteria')
scene_store.set_attribute(TOPIC_MAP_IDENTIFIER, attribute11)

# # Prop - 'power-up'.
# prop11 = Prop('power-up', 'Power-Up')
# prop11.location = '[0.0, -6.0, 2.0]'  
# asset13 = Asset('scene', 'power-up-001.json')
# prop11.add_asset(asset13)
# prop11_text = """## Power-Up
#
# In video games, __power-ups__ are objects that instantly benefit or add extra abilities to the game character as a game
# mechanic. This is in contrast to an item, which may or may not have a benefit and can be used at a time chosen by
# the player. Although often collected directly through touch, power-ups can sometimes only be gained by collecting
# several related items, such as the floating letters of the word 'EXTEND' in _Bubble Bobble_. Well known examples of
# power-ups that have entered popular culture include the power pellets from _Pac-Man_ (regarded as the first power-up)
# and the Super Mushroom from _Super Mario Bros_., which ranked first in UGO Networks' Top 11 Video Game Powerups.
# """
# asset14 = Asset('text', data=prop11_text)
# prop11.add_asset(asset14)
# store.set_prop(TOPIC_MAP_IDENTIFIER, prop11, 'cafeteria')


# Scene 02 - House.


# Scene 01 - Living Room.


# Scene 01 - Bedroom.


# Annotations
annotation1 = Topic('palm-tree', 'annotation', 'Palm Tree')
scene_store.set_topic(TOPIC_MAP_IDENTIFIER, annotation1)

annotation2 = Topic('street-lamp', 'annotation', 'Street Lamp')
scene_store.set_topic(TOPIC_MAP_IDENTIFIER, annotation2)

annotation3 = Topic('trash-cans', 'annotation', 'Trash Cans')
scene_store.set_topic(TOPIC_MAP_IDENTIFIER, annotation3)

annotation4 = Topic('chimney', 'annotation', 'Chimney')
scene_store.set_topic(TOPIC_MAP_IDENTIFIER, annotation4)


# Clean-up.
scene_store.close()
