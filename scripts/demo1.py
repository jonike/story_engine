"""
Demo 1 procedural definition script. Part of the StoryTechnologies Builder project.

September 04, 2016
Brett Alistair Kromkamp (brett.kromkamp@gmail.com)
"""

from engine.store.commands.metadatum.setmetadatum import SetMetadatum
from engine.store.models.metadatum import Metadatum
from engine.core.commands.scene.setcharacter import SetCharacter
from engine.core.commands.scene.setprop import SetProp
from engine.core.commands.scene.setscene import SetScene
from engine.core.commands.scene.setnavigation import SetNavigation
from engine.core.models.character import Character
from engine.core.models.prop import Prop
from engine.core.models.scene import Scene
from engine.core.models.asset import Asset


repo_path = '/home/brettk/Source/storytechnologies/story-engine/data/demo1.sqlite'

# Define and persist the first scene.
asset1 = Asset('scene', 'scene-001.json')
scene1 = Scene('scene-001', 'Scene One', 1)  # TODO: Change name of the scene.
scene1.add_asset(asset1)
scene1_text = """Scene One text
"""
asset2 = Asset('text', data=scene1_text)
scene1.add_asset(asset2)
SetScene(repo_path, scene1).do()
metadatum1 = Metadatum('type', 'interior', 'scene-001')
SetMetadatum(repo_path, metadatum1).do()