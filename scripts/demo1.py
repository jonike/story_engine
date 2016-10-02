"""
Demo 1 procedural definition script. Part of the StoryTechnologies Builder project.

September 04, 2016
Brett Alistair Kromkamp (brett.kromkamp@gmail.com)
"""

import os.path

from storyengine.store.commands.attribute.setattribute import SetAttribute
from storyengine.store.commands.map.createmap import CreateMap
from storyengine.store.commands.map.initmap import InitMap
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


database_path = '/home/brettk/Source/storytechnologies/story-engine/data/demo1.sqlite'

# Create and bootstrap topic map (ontology).
if not os.path.isfile(database_path):
    CreateMap(database_path).do()

if not TopicExists(database_path, 'genesis').do():
    InitMap(database_path).do()


# Scene 01 - Outpost.
asset11 = Asset('scene', 'scene-005.json')
scene1 = Scene('outpost', 'Outpost', 1)
scene1.add_asset(asset11)
scene1_text = """Outpost text
"""
asset12 = Asset('text', data=scene1_text)
scene1.add_asset(asset12)
SetScene(database_path, scene1).do()
attribute11 = Attribute('type', 'exterior', 'outpost')
SetAttribute(database_path, attribute11).do()


# Scene 2 - Military Base.
asset21 = Asset('scene', 'scene-006.json')
scene2 = Scene('military-base', 'Military Base', 2)
scene2.add_asset(asset21)
scene2_text = """Military base text
"""
asset22 = Asset('text', data=scene2_text)
scene2.add_asset(asset22)
SetScene(database_path, scene2).do()
attribute21 = Attribute('type', 'exterior', 'military-base')
SetAttribute(database_path, attribute21).do()


# Scene 3 - Weapon Factory.
asset31 = Asset('scene', 'scene-007.json')
scene3 = Scene('weapon-factory', 'Weapon Factory', 3)
scene3.add_asset(asset31)
scene3_text = """Weapon factory text
"""
asset32 = Asset('text', data=scene3_text)
scene3.add_asset(asset32)
SetScene(database_path, scene3).do()
attribute31 = Attribute('type', 'exterior', 'weapon-factory')
SetAttribute(database_path, attribute31).do()


# Scene 4 - Delivery Areas.
asset41 = Asset('scene', 'scene-008.json')
scene4 = Scene('delivery-area', 'Delivery Area', 4)
scene4.add_asset(asset41)
scene4_text = """Delivery area text
"""
asset42 = Asset('text', data=scene4_text)
scene4.add_asset(asset42)
SetScene(database_path, scene4).do()
attribute41 = Attribute('type', 'interior', 'delivery-area')
SetAttribute(database_path, attribute41).do()
attribute42 = Attribute('camera-clamp', 'true', 'delivery-area')
SetAttribute(database_path, attribute42).do()


# Scene 5 - Research Area.
asset51 = Asset('scene', 'scene-009.json')
scene5 = Scene('research-area', 'Research Area', 5)
scene5.add_asset(asset51)
scene5_text = """Research area text
"""
asset52 = Asset('text', data=scene5_text)
scene5.add_asset(asset52)
SetScene(database_path, scene5).do()
attribute51 = Attribute('type', 'interior', 'research-area')
SetAttribute(database_path, attribute51).do()
attribute52 = Attribute('camera-clamp', 'true', 'research-area')
SetAttribute(database_path, attribute52).do()

# Define and persist a prop.
prop51 = Prop('computer-001', 'Research System')
prop51.location = '[0.0, 0.0, 0.0]'  # x ("width"), y ("depth"), z ("height")
asset53 = Asset('scene', 'computer-001.json')
prop51.add_asset(asset53)
prop51_text = """## Computer Research System

Computational techniques are now a major innovation catalyst for all aspects of human endeavour. Our research aims to
develop tomorrow's information technology that supports innovative applications, from big data analytics to the
_Internet of Things_. It covers all aspects of information technology, including energy efficient and robust hardware
systems, _software defined networks_, secure _distributed systems_, _data science_, and _integrated circuits_ and power
electronics.
"""
asset54 = Asset('text', data=prop51_text)
prop51.add_asset(asset54)
SetProp(database_path, prop51, 'research-area').do()


# Scene 6 - Storage.
asset61 = Asset('scene', 'scene-010.json')
scene6 = Scene('storage', 'Storage', 6)
scene6.add_asset(asset61)
scene6_text = """Storage text
"""
asset62 = Asset('text', data=scene6_text)
scene6.add_asset(asset62)
SetScene(database_path, scene6).do()
attribute61 = Attribute('type', 'interior', 'storage')
SetAttribute(database_path, attribute61).do()
attribute62 = Attribute('camera-clamp', 'true', 'storage')
SetAttribute(database_path, attribute62).do()


# Define navigation paths between scenes.
SetNavigation(database_path, 'outpost', 'military-base', 'west', 'east').do()
SetNavigation(database_path, 'military-base', 'weapon-factory', 'west', 'east').do()
SetNavigation(database_path, 'weapon-factory', 'delivery-area', 'south', 'north').do()
SetNavigation(database_path, 'delivery-area', 'research-area', 'south', 'north').do()
SetNavigation(database_path, 'research-area', 'storage', 'south', 'north').do()
