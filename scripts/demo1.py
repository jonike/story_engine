"""
Demo 1 procedural definition script. Part of the StoryTechnologies project.

September 04, 2016
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


database_path = '/home/brettk/Source/storytechnologies/story-engine/data/demo1.sqlite'

# Create and bootstrap topic map (ontology).
if not os.path.isfile(database_path):
    CreateMap(database_path).do()

if not TopicExists(database_path, 'genesis').do():
    InitMap(database_path).do()


# Scene 01 - Outpost Alpha.
asset11 = Asset('scene', 'scene-005.json')
scene1 = Scene('outpost', 'Outpost Alpha', 1)
scene1.add_asset(asset11)
scene1_text = """A military __outpost__ is a detachment of troops stationed at a distance from the main force or formation,
usually at a station in a remote or sparsely populated location, positioned to stand guard against unauthorized
intrusions and surprise attacks; and the station occupied by such troops, usually a small military base or settlement in
an outlying frontier, limit, political boundary or in another country.
"""
asset12 = Asset('text', data=scene1_text)
scene1.add_asset(asset12)
SetScene(database_path, scene1).do()
attribute11 = Attribute('type', 'exterior', 'outpost')
SetAttribute(database_path, attribute11).do()

# Prop - 'ammunition'.
prop11 = Prop('ammunition', 'Ammunition')
prop11.location = '[0.74208, -0.42309, 1.06242]'  # x ("width"), y ("depth"), z ("height")
asset13 = Asset('scene', 'ammunition-001.json')
prop11.add_asset(asset13)
prop11_text = """## Ammunition

Ammunition (commonly shortened to ammo) is propellant and projectile, or broadly anything that can be used in combat
including bombs, missiles, warheads, land mines, naval mines, and anti-personnel mines. The word comes from the French
la munition which is all material used for war. The collective term for all types of ammunition is munitions.

The purpose of ammunition is to project force against a selected target. However, the nature of ammunition use also
includes delivery or combat supporting munitions such as pyrotechnic or incendiary compounds. Since the design of the
cartridge, the meaning has been transferred to the assembly of a projectile and its propellant in a single package.

Ammunition involves the application of fire to targets, general use of weapons by personnel, explosives and propellants,
cartridge systems, high explosive projectiles (HE), warheads, shaped charge forms of attack on armour and aircraft,
carrier projectiles, fuzes, mortar ammunition, small arms ammunition, grenades, mines, pyrotechnics, improved
conventional munitions, and terminally precision-guided munition.
"""
asset14 = Asset('text', data=prop11_text)
prop11.add_asset(asset14)
SetProp(database_path, prop11, 'outpost').do()


# Scene 2 - Military Base.
# asset21 = Asset('scene', 'scene-006.json')
# scene2 = Scene('military-base', 'Military Base', 2)
# scene2.add_asset(asset21)
# scene2_text = """Military base text
# """
# asset22 = Asset('text', data=scene2_text)
# scene2.add_asset(asset22)
# SetScene(database_path, scene2).do()
# attribute21 = Attribute('type', 'exterior', 'military-base')
# SetAttribute(database_path, attribute21).do()


# Scene 3 - Weapon Factory.
asset31 = Asset('scene', 'scene-007.json')
scene3 = Scene('weapon-factory', 'Weapon Factory', 3)
scene3.add_asset(asset31)
scene3_text = """The arms industry, also known as the defense industry or the arms trade, is a global business
responsible for the manufacturing and sales of weapons and military technology and equipment. It consists of a
commercial industry involved in the research and development, engineering, production, and servicing of military
material, equipment, and facilities.
"""
asset32 = Asset('text', data=scene3_text)
scene3.add_asset(asset32)
SetScene(database_path, scene3).do()
attribute31 = Attribute('type', 'exterior', 'weapon-factory')
SetAttribute(database_path, attribute31).do()
attribute32 = Attribute('mist', '0.0', 'weapon-factory')
SetAttribute(database_path, attribute32).do()

# Scene 4 - Delivery Area.
# asset41 = Asset('scene', 'scene-008.json')
# scene4 = Scene('delivery-area', 'Delivery Area', 4)
# scene4.add_asset(asset41)
# scene4_text = """Delivery area text
# """
# asset42 = Asset('text', data=scene4_text)
# scene4.add_asset(asset42)
# SetScene(database_path, scene4).do()
# attribute41 = Attribute('type', 'interior', 'delivery-area')
# SetAttribute(database_path, attribute41).do()
# attribute42 = Attribute('camera-clamp', 'true', 'delivery-area')
# SetAttribute(database_path, attribute42).do()


# Scene 5 - Research Area.
asset51 = Asset('scene', 'scene-009.json')
scene5 = Scene('research-area', 'Research Area', 5)
scene5.add_asset(asset51)
scene5_text = """The __Defense Advanced Research Projects Agency (DARPA)__ is an agency of the U.S. Department of Defense
responsible for the development of emerging technologies for use by the military. DARPA was created in February 1958 as
the __Advanced Research Projects Agency (ARPA)__ by President Dwight D. Eisenhower. Its purpose was to formulate and
execute research and development projects to expand the frontiers of technology and science, with the aim to reach
beyond immediate military requirements.
"""
asset52 = Asset('text', data=scene5_text)
scene5.add_asset(asset52)
SetScene(database_path, scene5).do()
attribute51 = Attribute('type', 'interior', 'research-area')
SetAttribute(database_path, attribute51).do()
attribute52 = Attribute('camera-clamp', 'true', 'research-area')
SetAttribute(database_path, attribute52).do()

# Prop - 'Computer research system'.
prop51 = Prop('computer', 'Research System')
prop51.location = '[-4.13449, 1.5, 2.40848]'  # x ("width"), y ("depth"), z ("height")
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
SetTags(database_path, 'computer', ['electronics']).do()

# Prop - 'Desk'.
prop52 = Prop('desk', 'Desk')
prop52.location = '[-3.96111, 0.97235, 1.88772]'  # x ("width"), y ("depth"), z ("height")
asset55 = Asset('scene', 'desk-001.json')
prop52.add_asset(asset55)
prop52_text = """## Desk
"""
asset56 = Asset('text', data=prop52_text)
prop52.add_asset(asset56)
SetProp(database_path, prop52, 'research-area').do()
SetTags(database_path, 'desk', ['furniture']).do()

# Prop - 'Chair'.
prop53 = Prop('chair', 'Chair')
prop53.location = '[-3.03917, 1.45503, 1.71397]'  # x ("width"), y ("depth"), z ("height")
asset57 = Asset('scene', 'chair-001.json')
prop53.add_asset(asset57)
prop53_text = """## Chair
"""
asset58 = Asset('text', data=prop53_text)
prop53.add_asset(asset58)
SetProp(database_path, prop53, 'research-area').do()
SetTags(database_path, 'chair', ['furniture']).do()

# Prop - 'Bookshelf'.
prop54 = Prop('bookshelf', 'Bookshelf')
prop54.location = '[-2.00528, 3.53678, 2.21712]'  # x ("width"), y ("depth"), z ("height")
asset59 = Asset('scene', 'bookshelf-001.json')
prop54.add_asset(asset59)
prop54_text = """## Bookshelf
"""
asset510 = Asset('text', data=prop54_text)
prop54.add_asset(asset510)
SetProp(database_path, prop54, 'research-area').do()
SetTags(database_path, 'bookshelf', ['furniture']).do()


# Scene 6 - Storage.
asset61 = Asset('scene', 'scene-010.json')
scene6 = Scene('storage', 'Storage', 6)
scene6.add_asset(asset61)
scene6_text = """A warehouse is a commercial building for storage of goods. Warehouses are used by manufacturers,
importers, exporters, wholesalers, transport businesses, customs, etc. They are usually large plain buildings in
industrial areas of cities, towns and villages.
"""
asset62 = Asset('text', data=scene6_text)
scene6.add_asset(asset62)
SetScene(database_path, scene6).do()
attribute61 = Attribute('type', 'interior', 'storage')
SetAttribute(database_path, attribute61).do()
attribute62 = Attribute('camera-clamp', 'true', 'storage')
SetAttribute(database_path, attribute62).do()

# Define and persist a character.
character61 = Character('robot', 'Robot')
character61.location = '[2.05589, -0.00046, 1.91936]'  # x ("width"), y ("depth"), z ("height")
asset63 = Asset('scene', 'robot-001.json')
character61.add_asset(asset63)
character61_text = """## Robot

A **robot** is a mechanical or virtual artificial agent, usually an electromechanical machine that is guided by a
computer program or electronic circuitry, and thus a type of an embedded system.

Robots can be autonomous or semi-autonomous and range from humanoids such as Honda's *Advanced Step in Innovative
Mobility* (ASIMO) and TOSY's *TOSY Ping Pong Playing Robot* (TOPIO) to industrial robots, medical operating robots,
patent assist robots, dog therapy robots, collectively programmed swarm robots, UAV drones such as General Atomics MQ-1
Predator, and even microscopic nano robots. By mimicking a lifelike appearance or automating movements, a robot may
convey a sense of intelligence or thought of its own.

The branch of technology that deals with the design, construction, operation, and application of robots, as well as
computer systems for their control, sensory feedback, and information processing is robotics. These technologies deal
with automated machines that can take the place of humans in dangerous environments or manufacturing processes, or
resemble humans in appearance, behavior, and/or cognition. Many of today's robots are inspired by nature contributing to
the field of bio-inspired robotics. These robots have also created a newer branch of robotics: soft robotics.
"""
asset64 = Asset('text', data=character61_text)
character61.add_asset(asset64)
SetCharacter(database_path, character61, 'storage').do()


# Define navigation paths between scenes.
# SetNavigation(database_path, 'outpost', 'military-base', 'west', 'east').do()
# SetNavigation(database_path, 'military-base', 'weapon-factory', 'west', 'east').do()
# SetNavigation(database_path, 'weapon-factory', 'delivery-area', 'south', 'north').do()
# SetNavigation(database_path, 'delivery-area', 'research-area', 'south', 'north').do()
# SetNavigation(database_path, 'research-area', 'storage', 'south', 'north').do()

SetNavigation(database_path, 'outpost', 'weapon-factory', 'west', 'east').do()
SetNavigation(database_path, 'weapon-factory', 'research-area', 'south', 'north').do()
SetNavigation(database_path, 'research-area', 'storage', 'south', 'north').do()


