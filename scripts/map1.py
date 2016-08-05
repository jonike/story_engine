"""
Map 1 procedural definition script. Part of the StoryTechnologies Builder project.

July 24, 2016
Brett Alistair Kromkamp (brett.kromkamp@gmail.com)
"""

from engine.core.commands.scene.setcharacter import SetCharacterCommand
from engine.core.commands.scene.setprop import SetPropCommand
from engine.core.commands.scene.setscene import SetSceneCommand
from engine.core.commands.scene.setnavigation import SetNavigationCommand
from engine.core.models.character import Character
from engine.core.models.prop import Prop
from engine.core.models.scene import Scene
from engine.core.models.asset import Asset


repo_path = '/home/brettk/Source/storytechnologies/story-engine/topics.db'


# Define and persist the first (robot) scene.
asset1 = Asset('scene', 'scene-001.json')
scene1 = Scene('scene-001', 'Scene 001', 1)
scene1.add_asset(asset1)
SetSceneCommand(repo_path, scene1).do()

# Define and persist the second (crates) scene.
asset2 = Asset('scene', 'scene-002.json')
scene2 = Scene('scene-002', 'Scene 002', 2)
scene2.add_asset(asset2)
SetSceneCommand(repo_path, scene2).do()

# Define and persist the third (empty) scene.
asset3 = Asset('scene', 'scene-003.json')
scene3 = Scene('scene-003', 'Scene 003', 3)
scene3.add_asset(asset3)
SetSceneCommand(repo_path, scene3).do()

# Define and persist the fourth (outside windmill) scene.
asset4 = Asset('scene', 'scene-004.json')
scene4 = Scene('scene-004', 'Scene 004', 4)
scene4.add_asset(asset4)
SetSceneCommand(repo_path, scene4).do()

# Define navigation paths between scenes.
SetNavigationCommand(repo_path, 'scene-001', 'scene-002', 'south', 'north').do()
SetNavigationCommand(repo_path, 'scene-001', 'scene-003', 'east', 'west').do()
SetNavigationCommand(repo_path, 'scene-003', 'scene-004', 'north', 'south').do()

# Define and persist a character.
character1 = Character('robot-001', 'Robot 001')
character1.location = '[3.0, 0.0, 0.0]'  # x ("width"), y ("height"), z ("depth")
asset4 = Asset('scene', 'robot-001.json')
character1.add_asset(asset4)
character1_text = """## Robot

A **robot** is a mechanical or virtual artificial agent, usually an electromechanical machine that is guided by a computer
program or electronic circuitry, and thus a type of an embedded system.

Robots can be autonomous or semi-autonomous and range from humanoids such as Honda's *Advanced Step in Innovative
Mobility* (ASIMO) and TOSY's *TOSY Ping Pong Playing Robot* (TOPIO) to industrial robots, medical operating robots, patent
assist robots, dog therapy robots, collectively programmed swarm robots, UAV drones such as General Atomics MQ-1
Predator, and even microscopic nano robots. By mimicking a lifelike appearance or automating movements, a robot may
convey a sense of intelligence or thought of its own.

The branch of technology that deals with the design, construction, operation, and application of robots, as well as
computer systems for their control, sensory feedback, and information processing is robotics. These technologies deal
with automated machines that can take the place of humans in dangerous environments or manufacturing processes, or
resemble humans in appearance, behavior, and/or cognition. Many of today's robots are inspired by nature contributing to
the field of bio-inspired robotics. These robots have also created a newer branch of robotics: soft robotics.
"""
asset5 = Asset('text', data=character1_text)
character1.add_asset(asset5)
SetCharacterCommand(repo_path, character1, 'scene-001').do()

# Define and persist a prop.
prop1 = Prop('prop-001', 'Crates 001')
prop1.location = '[2.0, 0.0, 2.0]'  # x ("width"), y ("height"), z ("depth")
asset6 = Asset('scene', 'crates-001.json')
prop1.add_asset(asset6)
prop1_text = """## Crate

A **crate** is a large strong container, often made of wood or metal.
"""
asset7 = Asset('text', data=prop1_text)
prop1.add_asset(asset7)
SetPropCommand(repo_path, prop1, 'scene-002').do()
