"""
Demo 1 procedural definition script. Part of the StoryTechnologies Builder project.

September 04, 2016
Brett Alistair Kromkamp (brett.kromkamp@gmail.com)
"""

from engine.store.commands.metadatum.setmetadatum import SetMetadatumCommand
from engine.store.models.metadatum import Metadatum
from engine.core.commands.scene.setcharacter import SetCharacterCommand
from engine.core.commands.scene.setprop import SetPropCommand
from engine.core.commands.scene.setscene import SetSceneCommand
from engine.core.commands.scene.setnavigation import SetNavigationCommand
from engine.core.models.character import Character
from engine.core.models.prop import Prop
from engine.core.models.scene import Scene
from engine.core.models.asset import Asset


repo_path = '/home/brettk/Source/storytechnologies/story-engine/data/demo1.sqlite'
