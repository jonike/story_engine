"""
Scene API functions. Part of the StoryTechnologies Builder project.

July 09, 2016
Brett Alistair Kromkamp (brett.kromkamp@gmail.com)
"""
from engine.core.models.character import Character
from engine.core.models.prop import Prop
from engine.store.commands.topic.gettopic import GetTopicCommand
from engine.store.retrievaloption import RetrievalOption
from engine.core.commands.scene.getscene import GetSceneCommand
from engine.core.commands.scene.getprop import GetPropCommand
from engine.core.commands.scene.getcharacter import GetCharacterCommand


database_path = '/home/brettk/Source/storytechnologies/story-engine/topics.db'


def get_topic(topic_identifier):
    topic = GetTopicCommand(database_path, topic_identifier, RetrievalOption.resolve_metadata).do()
    if topic:
        metadata = []
        base_names = []
        for metadatum in topic.metadata:
            metadata.append({
                'identifier': metadatum.identifier,
                'name': metadatum.name,
                'value': metadatum.value,
                'entityIdentifier': metadatum.entity_identifier,
                'dataType': str(metadatum.data_type),
                'scope': metadatum.scope,
                'language': str(metadatum.language)
            })
        for base_name in topic.base_names:
            base_names.append({
                'identifier': base_name.identifier,
                'name': base_name.name,
                'language': str(base_name.language)
            })
        result = {
            'topic': {
                'identifier': topic.identifier,
                'firstBaseName': topic.first_base_name.name,
                'baseNames': base_names,
                'instanceOf': topic.instance_of,
                'metadata': metadata
            }
        }
        return result, 200
    else:
        return "Not found", 404


def get_scene(entity_identifier):
    scene = GetSceneCommand(database_path, entity_identifier).do()
    if scene:
        associations = []
        assets = []
        entities = []
        props = []
        characters = []
        for entity in scene.entities:
            if isinstance(entity, Prop):
                prop_assets = []
                for prop_asset in entity.assets:
                    prop_assets.append({
                        'reference': prop_asset.reference,
                        'instanceOf': prop_asset.instance_of
                    })
                props.append({
                    'identifier': entity.identifier,
                    'name': entity.name,
                    'location': entity.location,
                    'rotation': entity.rotation,
                    'scale': entity.scale,
                    'assets': prop_assets
                })
            elif isinstance(entity, Character):
                character_assets = []
                for character_asset in entity.assets:
                    character_assets.append({
                        'reference': character_asset.reference,
                        'instanceOf': character_asset.instance_of
                    })
                characters.append({
                    'identifier': entity.identifier,
                    'name': entity.name,
                    'location': entity.location,
                    'rotation': entity.rotation,
                    'scale': entity.scale,
                    'assets': character_assets
                })
        entities.append({
            'props': props
        })
        entities.append({
            'characters': characters
        })
        for asset in scene.assets:
            assets.append({
                'reference': asset.reference,
                'instanceOf': asset.instance_of
            })
        result = {
            'scene': {
                'identifier': scene.identifier,
                'name': scene.name,
                'location': scene.location,
                'rotation': scene.rotation,
                'scale': scene.scale,
                'ordinal': scene.ordinal,
                'assets': assets,
                'associations': associations,
                'entities': entities
            }
        }
        return result, 200
    else:
        return "Not found", 404


def get_prop(entity_identifier):
    prop = GetPropCommand(database_path, entity_identifier)
    if prop:
        return "Not implemented", 200
    else:
        return "Not found", 404


def get_character(entity_identifier):
    character = GetCharacterCommand(database_path, entity_identifier)
    if character:
        return "Not implemented", 200
    else:
        return "Not found", 404