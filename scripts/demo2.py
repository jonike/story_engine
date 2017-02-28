"""
Demo 2 procedural definition script. Part of the StoryTechnologies project.

November 11, 2016
Brett Alistair Kromkamp (brett.kromkamp@gmail.com)
"""

from topicdb.core.models.attribute import Attribute
from topicdb.core.models.topic import Topic

from storyengine.core.store.scenestore import SceneStore
from storyengine.core.models.scene import Scene
from storyengine.core.models.asset import Asset


TOPIC_MAP_IDENTIFIER = 2

# Instantiate and open the scene store.
scene_store = SceneStore("localhost", "storytech", "5t0ryt3ch!")
scene_store.open()


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
scene_store.set_scene(TOPIC_MAP_IDENTIFIER, scene1)
attribute11 = Attribute('type', 'exterior', 'cafeteria')
scene_store.set_attribute(TOPIC_MAP_IDENTIFIER, attribute11)


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
