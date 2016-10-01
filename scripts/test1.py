"""
Test 1 procedural definition script. Part of the StoryTechnologies Builder project.

July 24, 2016
Brett Alistair Kromkamp (brett.kromkamp@gmail.com)
"""

import os.path

from storyengine.store.models.attribute import Attribute
from storyengine.store.commands.map.createmap import CreateMap
from storyengine.store.commands.map.initmap import InitMap
from storyengine.store.commands.topic.topicexists import TopicExists
from storyengine.store.commands.attribute.setattribute import SetAttribute
from storyengine.core.commands.scene.setcharacter import SetCharacter
from storyengine.core.commands.scene.setprop import SetProp
from storyengine.core.commands.scene.setscene import SetScene
from storyengine.core.commands.scene.setnavigation import SetNavigation
from storyengine.core.models.character import Character
from storyengine.core.models.prop import Prop
from storyengine.core.models.scene import Scene
from storyengine.core.models.asset import Asset


database_path = '/home/brettk/Source/storytechnologies/story-engine/data/test1.sqlite'

# Create and bootstrap topic map (ontology).
if not os.path.isfile(database_path):
    CreateMap(database_path).do()

if not TopicExists(database_path, 'genesis').do():
    InitMap(database_path).do()


# Define and persist the first (robot) scene.
asset1 = Asset('scene', 'scene-001.json')
scene1 = Scene('scene-001', 'Scene One', 1)
scene1.add_asset(asset1)
scene1_text = """There can be no thought of finishing for *aiming for the stars*. Both figuratively and literally, it is
a task to occupy the generations. And no matter how much progress one makes, there is always the thrill of just
beginning.

Failure is not an option.

We are all connected; To each other, biologically. To the earth, chemically. To the rest of the universe atomically.

What was most significant about the lunar voyage was not that man set foot on the Moon but that they set eye on the
earth.

Problems look mighty small from 150 miles up.
"""
asset2 = Asset('text', data=scene1_text)
scene1.add_asset(asset2)
SetScene(database_path, scene1).do()
attribute_type1 = Attribute('type', 'interior', 'scene-001')
SetAttribute(database_path, attribute_type1).do()
attribute_camera_clamp1 = Attribute('camera-clamp', 'true', 'scene-001')
SetAttribute(database_path, attribute_camera_clamp1).do()

# Define and persist the second (crates) scene.
asset3 = Asset('scene', 'scene-002.json')
scene2 = Scene('scene-002', 'Scene Two', 2)
scene2.add_asset(asset3)
scene2_text = """The sky is the limit only for those who aren't afraid to fly!

Buy why, some say, the moon? Why choose this as our goal? And they may as well ask why climb the highest mountain?

Where ignorance lurks, so too do the frontiers of discovery and imagination.
"""
asset4 = Asset('text', data=scene2_text)
scene2.add_asset(asset4)
SetScene(database_path, scene2).do()
attribute_type2 = Attribute('type', 'interior', 'scene-002')
SetAttribute(database_path, attribute_type2).do()
attribute_camera_clamp2 = Attribute('camera-clamp', 'true', 'scene-002')
SetAttribute(database_path, attribute_camera_clamp2).do()

# Define and persist the third (empty) scene.
asset5 = Asset('scene', 'scene-003.json')
scene3 = Scene('scene-003', 'Scene Three', 3)
scene3.add_asset(asset5)
scene3_text = """As I stand out here in the wonders of the unknown at Hadley, I sort of realize there's a fundamental
truth to our nature, Man must explore ... and this is exploration at its greatest.

The Earth was small, light blue, and so touchingly alone, our home that must be defended like a holy relic. The Earth
was absolutely round. I believe I never knew what the word round meant until I saw Earth from space.

We want to explore. We're curious people. Look back over history, people have put their lives at stake to go out and
explore ... We believe in what we're doing. Now it's time to go.
"""
asset6 = Asset('text', data=scene3_text)
scene3.add_asset(asset6)
SetScene(database_path, scene3).do()
attribute_type3 = Attribute('type', 'interior', 'scene-003')
SetAttribute(database_path, attribute_type3).do()
attribute_camera_clamp3 = Attribute('camera-clamp', 'true', 'scene-003')
SetAttribute(database_path, attribute_camera_clamp3).do()

# Define and persist the fourth (outside windmill) scene.
asset7 = Asset('scene', 'scene-004.json')
scene4 = Scene('scene-004', 'Scene Four', 4)
scene4.add_asset(asset7)
scene4_text = """When I orbited the Earth in a spaceship, I saw for the first time how beautiful our planet is. Mankind,
let us preserve and increase this beauty, and not destroy it!

If you could see the earth illuminated when you were in a place as dark as night, it would look to you more splendid
than the moon.

As I stand out here in the wonders of the unknown at Hadley, I sort of realize there's a fundamental truth to our
nature, Man must explore ... and this is exploration at its greatest.
"""
asset8 = Asset('text', data=scene4_text)
scene4.add_asset(asset8)
SetScene(database_path, scene4).do()
#SetTags(database_path, 'scene-004', ['exterior', 'sci-fi', 'afternoon', 'summer']).do()
attribute_type4 = Attribute('type', 'exterior', 'scene-004')
SetAttribute(database_path, attribute_type4).do()
attribute_time1 = Attribute('time', '11.0', 'scene-004')  # 11:00
SetAttribute(database_path, attribute_time1).do()
attribute_camera_clamp4 = Attribute('camera-clamp', 'false', 'scene-004')
SetAttribute(database_path, attribute_camera_clamp4).do()

# Define navigation paths between scenes.
SetNavigation(database_path, 'scene-001', 'scene-002', 'south', 'north').do()
SetNavigation(database_path, 'scene-001', 'scene-003', 'east', 'west').do()
SetNavigation(database_path, 'scene-003', 'scene-004', 'north', 'south').do()

# Define and persist a character.
character1 = Character('robot-001', 'Robot One')
character1.location = '[3.0, 0.0, 0.0]'  # x ("width"), y ("depth"), z ("height")
asset9 = Asset('scene', 'robot-001.json')
character1.add_asset(asset9)
character1_text = """## Robot

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
asset10 = Asset('text', data=character1_text)
character1.add_asset(asset10)
SetCharacter(database_path, character1, 'scene-001').do()

# Define and persist a prop.
prop1 = Prop('prop-001', 'Crates One')
prop1.location = '[2.0, 2.0, 0.0]'  # x ("width"), y ("depth"), z ("height")
asset11 = Asset('scene', 'crates-001.json')
prop1.add_asset(asset11)
prop1_text = """## Crate

A **crate** is a large strong container, often made of wood or metal.
"""
asset12 = Asset('text', data=prop1_text)
prop1.add_asset(asset12)
SetProp(database_path, prop1, 'scene-002').do()
