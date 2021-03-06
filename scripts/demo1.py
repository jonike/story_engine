"""
Demo 1 procedural definition script. Part of the StoryTechnologies project.

September 04, 2016
Brett Alistair Kromkamp (brett.kromkamp@gmail.com)
"""

import os
import configparser

from topicdb.core.models.attribute import Attribute
from topicdb.core.models.occurrence import Occurrence

from storyengine.core.store.scenestore import SceneStore
from storyengine.core.models.character import Character
from storyengine.core.models.prop import Prop
from storyengine.core.models.scene import Scene
from storyengine.core.models.asset import Asset


TOPIC_MAP_IDENTIFIER = 1
SETTINGS_FILE_PATH = os.path.join(os.path.dirname(__file__), '../settings.ini')

config = configparser.ConfigParser()
config.read(SETTINGS_FILE_PATH)

username = config['DATABASE']['Username']
password = config['DATABASE']['Password']

# Instantiate and open the scene store.
scene_store = SceneStore(username, password)
scene_store.open()


# Genesis topic.
attribute01 = Attribute('entry-scene', 'outpost', 'genesis')
scene_store.set_attribute(TOPIC_MAP_IDENTIFIER, attribute01)

story_text = """The US is at an ever growing risk of cyber attacks, with energy infrastructure likely to be hackers' 
prime target. This was the stark warning made by General Keith Alexander, the retired general and former chief of the __National 
Security Agency__, earlier this year.

Now, the Pentagon says it has a plan to do something about the threat. Its research division, __DARPA__, has launched a 
new program to target security threats that have the potential to wipe out all of America's power systems. 
"""
story_text_occurrence = Occurrence(topic_identifier='genesis', instance_of='text', resource_data=bytes(story_text, 'utf-8'))
scene_store.set_occurrence(TOPIC_MAP_IDENTIFIER, story_text_occurrence)

story_image_occurrence = Occurrence(topic_identifier='genesis', instance_of='image', resource_ref='outpost.png')
scene_store.set_occurrence(TOPIC_MAP_IDENTIFIER, story_image_occurrence)


# Scene 01 - Outpost Alpha.
asset11 = Asset('scene', 'scene-005.json')
scene1 = Scene('outpost', 'Outpost Alpha',
               description='A station established at a distance from the main body of an army to protect it from surprise attack.',
               ordinal=1)
scene1.add_asset(asset11)
scene1_text = """A military __outpost__ is a detachment of troops stationed at a distance from the main force or
formation, usually at a station in a remote or sparsely populated location, positioned to stand guard against
unauthorized intrusions and surprise attacks; and the station occupied by such troops, usually a small military base or
settlement in an outlying frontier, limit, political boundary or in another country.
"""
asset12 = Asset('text', data=scene1_text)
scene1.add_asset(asset12)
scene_store.set_scene(TOPIC_MAP_IDENTIFIER, scene1)
attribute11 = Attribute('type', 'exterior', 'outpost')
scene_store.set_attribute(TOPIC_MAP_IDENTIFIER, attribute11)
attribute12 = Attribute('camera-rotation', '0.30', 'outpost')  # Camera rotation multiplier.
scene_store.set_attribute(TOPIC_MAP_IDENTIFIER, attribute12)

# Prop - 'ammunition'.
prop11 = Prop('ammunition', 'Ammunition')
prop11.location = '[0.74208, -0.42309, 1.06242]'  
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
scene_store.set_prop(TOPIC_MAP_IDENTIFIER, prop11, 'outpost')

# Prop - 'windmill'.
prop12 = Prop('windmill', 'Windmill')
prop12.location = '[7.22397, 7.44645, 5.5]'  
asset15 = Asset('scene', 'windmill-001.json')
prop12.add_asset(asset15)
prop12_text = """## Windmill

A __windmill__ is a mill that converts the energy of wind into rotational energy by means of vanes called sails or
blades. Centuries ago, windmills usually were used to mill grain, pump water, or both. Thus they often were
gristmills, windpumps, or both. The majority of modern windmills take the form of wind turbines used to
generate electricity, or windpumps used to pump water, either for land drainage or to extract groundwater.
"""
asset16 = Asset('text', data=prop12_text)
prop12.add_asset(asset16)
scene_store.set_prop(TOPIC_MAP_IDENTIFIER, prop12, 'outpost')


# Scene 3 - Weapon Factory.
asset31 = Asset('scene', 'scene-007.json')
scene3 = Scene('weapon-factory', 'Weapon Factory', ordinal=3)
scene3.add_asset(asset31)
scene3_text = """The arms industry, also known as the defense industry or the arms trade, is a global business
responsible for the manufacturing and sales of weapons and military technology and equipment. It consists of a
commercial industry involved in the research and development, engineering, production, and servicing of military
material, equipment, and facilities.
"""
asset32 = Asset('text', data=scene3_text)
scene3.add_asset(asset32)
scene_store.set_scene(TOPIC_MAP_IDENTIFIER, scene3)
attribute31 = Attribute('type', 'exterior', 'weapon-factory')
scene_store.set_attribute(TOPIC_MAP_IDENTIFIER, attribute31)
attribute32 = Attribute('mist-depth', '35', 'weapon-factory')
scene_store.set_attribute(TOPIC_MAP_IDENTIFIER, attribute32)

# Prop - 'Telecommunications Facility".
prop31 = Prop('telecommunications-facility', 'Telecommunications Facility')
prop31.location = '[4.09054, 6.29359, 6.07536]'  
asset33 = Asset('scene', 'telecommunications-facility-001.json')
prop31.add_asset(asset33)
prop31_text = """## Telecommunications Facility

In telecommunications, a facility is defined as:

1. A fixed, mobile, or transportable structure, including (a) all installed electrical and electronic wiring, cabling,
and equipment and (b) all supporting structures, such as utility, ground network, and electrical supporting structures.
2. A network-provided service to users or the network operating administration.
3. A transmission pathway and associated equipment.
4. In a protocol applicable to a data unit, such as a block or frame, an additional item of information or a constraint
encoded within the protocol to provide the required control.
5. A real property entity consisting of one or more of the following: a building, a structure, a utility system,
pavement, and underlying land.
"""
asset34 = Asset('text', data=prop31_text)
prop31.add_asset(asset34)
scene_store.set_prop(TOPIC_MAP_IDENTIFIER, prop31, 'weapon-factory')

# # Prop - 'Military Robot.
# prop32 = Prop('robot', 'Military Robot')
# prop32.location = '[1.37942, -3.62861, 0.63]'  
# asset35 = Asset('scene', 'robot-001.json')
# prop32.add_asset(asset35)
# prop32_text = """## Military Robot
#
# __Military robots__ are autonomous robots or remote-controlled mobile robots designed for military applications, from
# transport to search and rescue and attack. Some such systems are currently in use, and many are under development.
#
# Broadly defined, military robots date back to World War II and the Cold War in the form of the German Goliath tracked
# mines and the Soviet _teletanks_. The MQB-1 Predator drone was when CIA officers began to see the first practical
# returns on their decade-old fantasy of using aerial robots to collect intelligence.
# """
# asset36 = Asset('text', data=prop32_text)
# prop32.add_asset(asset36)
# store.set_prop(TOPIC_MAP_IDENTIFIER, prop32, 'weapon-factory')

# Character - 'Military Robot.
character31 = Character('robot', 'Military Robot')
character31.location = '[1.37942, -3.62861, 0.63]'  
asset35 = Asset('scene', 'robot-001.json')
character31.add_asset(asset35)
character31_text = """## Military Robot

__Military robots__ are autonomous robots or remote-controlled mobile robots designed for military applications, from
transport to search and rescue and attack. Some such systems are currently in use, and many are under development.

Broadly defined, military robots date back to World War II and the Cold War in the form of the German Goliath tracked
mines and the Soviet _teletanks_. The MQB-1 Predator drone was when CIA officers began to see the first practical
returns on their decade-old fantasy of using aerial robots to collect intelligence.
"""
asset36 = Asset('text', data=character31_text)
character31.add_asset(asset36)
asset37 = Asset('augmented-reality', reference='robot-001.json')
character31.add_asset(asset37)
scene_store.set_character(TOPIC_MAP_IDENTIFIER, character31, 'weapon-factory')

scene_store.set_tags(TOPIC_MAP_IDENTIFIER, 'robot', ['electronics'])


# Scene 5 - Research Area.
asset51 = Asset('scene', 'scene-009.json')
scene5 = Scene('research-area', 'Research Area',
               description='Diligent and systematic inquiry or investigation into a subject in order to discover or revise facts, theories, applications, etc.',
               ordinal=5)
scene5.add_asset(asset51)
scene5_text = """The __Defense Advanced Research Projects Agency (DARPA)__ is an agency of the U.S. Department of
Defense responsible for the development of emerging technologies for use by the military. DARPA was created in February
1958 as the __Advanced Research Projects Agency (ARPA)__ by President Dwight D. Eisenhower. Its purpose was to formulate
and execute research and development projects to expand the frontiers of technology and science, with the aim to reach
beyond immediate military requirements.
"""
asset52 = Asset('text', data=scene5_text)
scene5.add_asset(asset52)
scene_store.set_scene(TOPIC_MAP_IDENTIFIER, scene5)
attribute51 = Attribute('type', 'interior', 'research-area')
scene_store.set_attribute(TOPIC_MAP_IDENTIFIER, attribute51)
attribute52 = Attribute('camera-clamp', 'true', 'research-area')
scene_store.set_attribute(TOPIC_MAP_IDENTIFIER, attribute52)

# Prop - 'Computer research system'.
prop51 = Prop('computer', 'Research System')
prop51.location = '[-4.13449, 1.5, 2.40848]'  
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
scene_store.set_prop(TOPIC_MAP_IDENTIFIER, prop51, 'research-area')
scene_store.set_tags(TOPIC_MAP_IDENTIFIER, 'computer', ['electronics'])
tag51_text = """__Electronics__ is the science of controlling electrical energy electrically, in which the electrons
have a fundamental role. Electronics deals with electrical circuits that involve active electrical components such as
vacuum tubes, transistors, diodes, integrated circuits, associated passive electrical components, and interconnection
technologies.

Commonly, electronic devices contain circuitry consisting primarily or exclusively of active semiconductors supplemented
with passive elements; such a circuit is described as an electronic circuit.
"""
tag_occurrence51 = Occurrence(topic_identifier='electronics', instance_of='text', resource_data=bytes(tag51_text, 'utf-8'))
scene_store.set_occurrence(TOPIC_MAP_IDENTIFIER, tag_occurrence51)

# Prop - 'Desk'.
prop52 = Prop('desk', 'Desk')
prop52.location = '[-3.96111, 0.97235, 1.88772]'  
asset55 = Asset('scene', 'desk-001.json')
prop52.add_asset(asset55)
prop52_text = """## Desk

A __desk__ or __bureau__ is a piece of furniture used in a school, office, home or the like for academic, professional
or domestic activities such as reading, writing, or using equipment such as a computer. Desks often have one or more
drawers, compartments, or pigeonholes to store items such as office supplies and papers. Desks are usually made of wood
or metal, although materials such as tempered glass are sometimes seen.
"""
asset56 = Asset('text', data=prop52_text)
prop52.add_asset(asset56)
scene_store.set_prop(TOPIC_MAP_IDENTIFIER, prop52, 'research-area')
scene_store.set_tags(TOPIC_MAP_IDENTIFIER, 'desk', ['furniture'])

# Prop - 'Chair'.
prop53 = Prop('chair', 'Chair')
prop53.location = '[-3.03917, 1.45503, 1.71397]'  
asset57 = Asset('scene', 'chair-001.json')
prop53.add_asset(asset57)
prop53_text = """## Chair

A __chair__ is a piece of furniture with a raised surface, commonly used to seat a single person. Chairs are supported
most often by four legs and have a back; however, a chair can have three legs or can have a different shape. Chairs are
made of a wide variety of materials, ranging from wood to metal to synthetic material (e.g., plastic), and they may be
padded or upholstered in various colors and fabrics, either just on the seat (as with some dining room chairs) or on
the entire chair.
"""
asset58 = Asset('text', data=prop53_text)
prop53.add_asset(asset58)
scene_store.set_prop(TOPIC_MAP_IDENTIFIER, prop53, 'research-area')
scene_store.set_tags(TOPIC_MAP_IDENTIFIER, 'chair', ['furniture'])
tag52_text = """Furniture is movable objects intended to support various human activities such as seating (e.g., chairs,
stools, tables and sofas) and sleeping (e.g., beds). Furniture is also used to hold objects at a convenient height for
work (as horizontal surfaces above the ground, such as tables and desks), or to store things (e.g., cupboards and
shelves).

Furniture can be a product of design and is considered a form of decorative art. In addition to furniture's functional
role, ita can serve a symbolic or religious purpose. It can be made from many materials, including metal, plastic, and
wood. Furniture can be made using a variety of woodworking joints which often reflect the local culture.
"""
tag_occurrence52 = Occurrence(topic_identifier='furniture', instance_of='text', resource_data=bytes(tag52_text, 'utf-8'))
scene_store.set_occurrence(TOPIC_MAP_IDENTIFIER, tag_occurrence52)

# Prop - 'Bookshelf'.
prop54 = Prop('bookshelf', 'Bookshelf')
prop54.location = '[-2.00528, 3.53678, 2.21712]'  
asset59 = Asset('scene', 'bookshelf-001.json')
prop54.add_asset(asset59)
prop54_text = """## Bookshelf

A __bookcase__, or __bookshelf__, is a piece of furniture, almost always with horizontal shelves, used to store books.
Bookcases are used in private homes, public and university libraries, offices and bookstores. A bookcase may be fitted
with glass doors. A bookcase consists of a unit including two or more shelves which may not all be used to contain books
or other printed materials.
"""
asset510 = Asset('text', data=prop54_text)
prop54.add_asset(asset510)
scene_store.set_prop(TOPIC_MAP_IDENTIFIER, prop54, 'research-area')
scene_store.set_tags(TOPIC_MAP_IDENTIFIER, 'bookshelf', ['furniture'])

# # Prop - 'Utility Robot.
# prop55 = Prop('utility-robot', 'Utility Robot')
# prop55.location = '[4.07017, -0.00034, 1.42042]'  
# asset511 = Asset('scene', 'utility-robot-001.json')
# prop55.add_asset(asset511)
# prop55_text = """## Robot
#
# A **robot** is a mechanical or virtual artificial agent, usually an electromechanical machine that is guided by a
# computer program or electronic circuitry, and thus a type of an embedded system.
#
# Robots can be autonomous or semi-autonomous and range from humanoids such as Honda's *Advanced Step in Innovative
# Mobility* (ASIMO) and TOSY's *TOSY Ping Pong Playing Robot* (TOPIO) to industrial robots, medical operating robots,
# patent assist robots, dog therapy robots, collectively programmed swarm robots, UAV drones such as General Atomics MQ-1
# Predator, and even microscopic nano robots. By mimicking a lifelike appearance or automating movements, a robot may
# convey a sense of intelligence or thought of its own.
#
# The branch of technology that deals with the design, construction, operation, and application of robots, as well as
# computer systems for their control, sensory feedback, and information processing is robotics. These technologies deal
# with automated machines that can take the place of humans in dangerous environments or manufacturing processes, or
# resemble humans in appearance, behavior, and/or cognition. Many of today's robots are inspired by nature contributing to
# the field of bio-inspired robotics. These robots have also created a newer branch of robotics: soft robotics.
# """
# asset512 = Asset('text', data=prop55_text)
# prop55.add_asset(asset512)
# store.set_prop(TOPIC_MAP_IDENTIFIER, prop55, 'research-area')
#
# store.set_tags(TOPIC_MAP_IDENTIFIER, 'utility-robot', ['electronics'])

# Character - 'Utility Robot.
character51 = Character('utility-robot', 'Utility Robot')
character51.location = '[4.07017, -0.00034, 1.42042]'  
asset511 = Asset('scene', 'utility-robot-001.json')
character51.add_asset(asset511)
character51_text = """## Robot

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
asset512 = Asset('text', data=character51_text)
character51.add_asset(asset512)
asset513 = Asset('augmented-reality', reference='utility-robot-003.json')
character51.add_asset(asset513)
scene_store.set_character(TOPIC_MAP_IDENTIFIER, character51, 'research-area')

scene_store.set_tags(TOPIC_MAP_IDENTIFIER, 'utility-robot', ['electronics'])


# Scene 6 - Storage.
asset61 = Asset('scene', 'scene-010.json')
scene6 = Scene('storage-area', 'Storage Area', ordinal=6)
scene6.add_asset(asset61)
scene6_text = """A warehouse is a commercial building for storage of goods. Warehouses are used by manufacturers,
importers, exporters, wholesalers, transport businesses, customs, etc. They are usually large plain buildings in
industrial areas of cities, towns and villages.
"""
asset62 = Asset('text', data=scene6_text)
scene6.add_asset(asset62)
scene_store.set_scene(TOPIC_MAP_IDENTIFIER, scene6)
attribute61 = Attribute('type', 'interior', 'storage-area')
scene_store.set_attribute(TOPIC_MAP_IDENTIFIER, attribute61)
attribute62 = Attribute('camera-clamp', 'true', 'storage-area')
scene_store.set_attribute(TOPIC_MAP_IDENTIFIER, attribute62)

# Set up navigation.
scene_store.set_navigation(TOPIC_MAP_IDENTIFIER, 'outpost', 'weapon-factory', 'west', 'east')
scene_store.set_navigation(TOPIC_MAP_IDENTIFIER, 'weapon-factory', 'research-area', 'south', 'north')
scene_store.set_navigation(TOPIC_MAP_IDENTIFIER, 'research-area', 'storage-area', 'south', 'north')


# Clean-up.
scene_store.close()
