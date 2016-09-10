"""
Demo 1 procedural definition script. Part of the StoryTechnologies Builder project.

September 04, 2016
Brett Alistair Kromkamp (brett.kromkamp@gmail.com)
"""

from storyengine.store.commands.attribute.setattribute import SetAttribute
from storyengine.store.models.attribute import Attribute
from storyengine.core.commands.scene.setcharacter import SetCharacter
from storyengine.core.commands.scene.setprop import SetProp
from storyengine.core.commands.scene.setscene import SetScene
from storyengine.core.commands.scene.setnavigation import SetNavigation
from storyengine.core.models.character import Character
from storyengine.core.models.prop import Prop
from storyengine.core.models.scene import Scene
from storyengine.core.models.asset import Asset


repo_path = '/home/brettk/Source/storytechnologies/story-storyengine/data/demo1.sqlite'

# Define and persist the first scene.
asset1 = Asset('scene', 'scene-001.json')
scene1 = Scene('scene-001', 'Scene One', 1)  # TODO: Change name of the scene.
scene1.add_asset(asset1)
scene1_text = """Scene One text
"""
asset2 = Asset('text', data=scene1_text)
scene1.add_asset(asset2)
SetScene(repo_path, scene1).do()
attribute1 = Attribute('type', 'interior', 'scene-001')
SetAttribute(repo_path, attribute1).do()
