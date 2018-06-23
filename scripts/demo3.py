"""
Demo 2 procedural definition script. Part of the StoryTechnologies project.

June 05, 2018
Brett Alistair Kromkamp (brett.kromkamp@gmail.com)
"""

import os
import configparser

from topicdb.core.models.attribute import Attribute
from topicdb.core.models.occurrence import Occurrence

from storyengine.core.store.scenestore import SceneStore
from storyengine.core.models.prop import Prop
from storyengine.core.models.scene import Scene
from storyengine.core.models.asset import Asset


TOPIC_MAP_IDENTIFIER = 3
SETTINGS_FILE_PATH = os.path.join(os.path.dirname(__file__), '../settings.ini')

config = configparser.ConfigParser()
config.read(SETTINGS_FILE_PATH)

username = config['DATABASE']['Username']
password = config['DATABASE']['Password']

# Instantiate and open the scene store.
scene_store = SceneStore(username, password)
scene_store.open()

# Genesis topic.
attribute01 = Attribute('entry-scene', 'environment', 'genesis')
scene_store.set_attribute(TOPIC_MAP_IDENTIFIER, attribute01)

story_text = """A test story.
"""
story_text_occurrence = Occurrence(topic_identifier='genesis', instance_of='text', resource_data=bytes(story_text, 'utf-8'))
scene_store.set_occurrence(TOPIC_MAP_IDENTIFIER, story_text_occurrence)

story_image_occurrence = Occurrence(topic_identifier='genesis', instance_of='image', resource_ref='locomotive.png')
scene_store.set_occurrence(TOPIC_MAP_IDENTIFIER, story_image_occurrence)



# Test scene.
asset0 = Asset('scene', 'environment.gltf')
scene1 = Scene('environment', 'Test Environment')
scene1.add_asset(asset0)
scene1_text = """An environment for testing purposes.
"""
scene_store.set_scene(TOPIC_MAP_IDENTIFIER, scene1)


# Prop 1 'Cone'.
prop1 = Prop('cone', 'Cone')
prop1.location = '[-4.04, 0.0, 3.14]'
prop1.scale = '[1.66, 1.66, 1.66]'
asset1 = Asset('scene', 'cone.gltf')
prop1.add_asset(asset1)
scene_store.set_prop(TOPIC_MAP_IDENTIFIER, prop1, 'environment')


# Prop 2 'Cylinder'.
prop2 = Prop('cylinder', 'Cylinder')
prop2.location = '[4.05, 0.0, -3.75]'
asset2 = Asset('scene', 'cylinder.gltf')
prop2.add_asset(asset2)
scene_store.set_prop(TOPIC_MAP_IDENTIFIER, prop2, 'environment')


# Prop 3 'Sphere'.
prop3 = Prop('sphere', 'Sphere')
prop3.location = '[3.93, 1.60, 3.19]'
prop3.scale = '[0.40, 0.40, 0.40]'
asset3 = Asset('scene', 'sphere.gltf')
prop3.add_asset(asset3)
scene_store.set_prop(TOPIC_MAP_IDENTIFIER, prop3, 'environment')


# Prop 4 'Cube'.
prop4 = Prop('cube', 'Cube')
prop4.location = '[-2.86, 0.0, -3.19]'
prop4.rotation = '[0.0, -53.04, 0.0]'
prop4.scale = '[1.63, 1.63, 1.63]'
asset4 = Asset('scene', 'cube.gltf')
prop4.add_asset(asset4)
scene_store.set_prop(TOPIC_MAP_IDENTIFIER, prop4, 'environment')


# Clean-up.
scene_store.close()
