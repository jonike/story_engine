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


database_path = '/home/brettk/Source/storytechnologies/story-engine/topics.db'


# Define and persist the first scene.
asset1 = Asset('scene-001.json', 'scene')
scene1 = Scene('scene-001', 'Scene 001', 1)
scene1.add_asset(asset1)
SetSceneCommand(database_path, scene1).do()

# Define and persist the second scene.
asset2 = Asset('scene-002.json', 'scene')
scene2 = Scene('scene-002', 'Scene 002', 2)
scene2.add_asset(asset2)
SetSceneCommand(database_path, scene2).do()

# Define and persist the third scene.
asset3 = Asset('scene-003.json', 'scene')
scene3 = Scene('scene-003', 'Scene 003', 3)
scene3.add_asset(asset3)
SetSceneCommand(database_path, scene3).do()

# Define navigation paths between scenes.
SetNavigationCommand(database_path, 'scene-001', 'scene-002', 'south', 'north').do()
SetNavigationCommand(database_path, 'scene-001', 'scene-003', 'east', 'west').do()

# Define and persist a character.
character1 = Character('robot-001', 'Robot 001')
character1.location = '[1.0, 1.0, 1.0]'  # x, y, z = 1m
asset4 = Asset('robot-001.json', 'scene')
character1.add_asset(asset4)
SetCharacterCommand(database_path, character1, 'scene-001').do()

# Define and persist a prop.
prop1 = Prop('prop-001', 'Crates 001')
prop1.location = '[2.0, 2.0, 2.0]'  # x, y, z = 2m
asset5 = Asset('crates-001.json', 'scene')
prop1.add_asset(asset5)
SetPropCommand(database_path, prop1, 'scene-002').do()
