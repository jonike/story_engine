"""
Scene API functions. Part of the StoryTechnologies Builder project.

July 09, 2016
Brett Alistair Kromkamp (brett.kromkamp@gmail.com)
"""

import base64
import functools

from engine.core.models.character import Character
from engine.core.models.prop import Prop
from engine.store.commands.association.getassociation import GetAssociationCommand
from engine.store.commands.association.getassociationgroups import GetAssociationGroupsCommand
from engine.store.commands.metadatum.getmetadata import GetMetadataCommand
from engine.store.commands.metadatum.getmetadatum import GetMetadatumCommand
from engine.store.commands.occurrence.getoccurrence import GetOccurrenceCommand
from engine.store.commands.occurrence.getoccurrences import GetOccurrencesCommand
from engine.store.commands.topic.gettopic import GetTopicCommand
from engine.store.commands.topic.gettopicidentifiers import GetTopicIdentifiersCommand
from engine.store.commands.topic.gettopics import GetTopicsCommand
from engine.store.retrievaloption import RetrievalOption
from engine.core.commands.scene.getscene import GetSceneCommand
from engine.core.commands.scene.getprop import GetPropCommand
from engine.core.commands.scene.getcharacter import GetCharacterCommand


database_path = '/home/brettk/Source/storytechnologies/story-engine/topics.db'


def get_topic_identifiers(query, offset=0, limit=100, filter_entities=RetrievalOption.filter_entities):
    # TODO: Implement 'filter entities' switch.
    result = GetTopicIdentifiersCommand(database_path, query, filter_entities, offset, limit).do()
    if result:
        return result, 200
    else:
        return "Not found", 404


@functools.lru_cache(maxsize=64)
def get_topic(identifier):
    topic = GetTopicCommand(database_path, identifier, RetrievalOption.resolve_metadata).do()
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


def get_topics(instance_of='topic', offset=0, limit=100):
    topics = GetTopicsCommand(database_path, instance_of=instance_of, offset=offset, limit=limit).do()
    if topics:
        result = []
        for topic in topics:
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
            topic = {
                'topic': {
                    'identifier': topic.identifier,
                    'firstBaseName': topic.first_base_name.name,
                    'baseNames': base_names,
                    'instanceOf': topic.instance_of,
                    'metadata': metadata
                }
            }
            result.append(topic)
        return result, 200
    else:
        return "Not found", 404

    
@functools.lru_cache(maxsize=64)
def get_occurrence(identifier, inline_resource_data=RetrievalOption.dont_inline_resource_data):
    occurrence = GetOccurrenceCommand(database_path, identifier, inline_resource_data).do()
    if occurrence:
        # TODO: Implementation.
        return "Occurrence found", 200
    else:
        return "Not found", 404


def get_occurrences(identifier,
                    inline_resource_data=RetrievalOption.dont_inline_resource_data,
                    resolve_metadata=RetrievalOption.dont_resolve_metadata,
                    instance_of=''):
    occurrences = GetOccurrencesCommand(database_path, identifier, inline_resource_data, resolve_metadata, instance_of).do()
    if occurrences:
        result = []
        for occurrence in occurrences:
            metadata = []
            for metadatum in occurrence.metadata:
                metadata.append({
                    'identifier': metadatum.identifier,
                    'name': metadatum.name,
                    'value': metadatum.value,
                    'entityIdentifier': metadatum.entity_identifier,
                    'dataType': str(metadatum.data_type),
                    'scope': metadatum.scope,
                    'language': str(metadatum.language)
                })
            occurrence = {
                'occurrence': {
                    'identifier': occurrence.identifier,
                    'instanceOf': occurrence.instance_of,
                    'scope': occurrence.scope,
                    'resourceRef': occurrence.resource_ref,
                    'resourceData': base64.b64encode(occurrence.resource_data).decode('utf-8'),
                    'language': str(occurrence.language),
                    'metadata': metadata
                }
            }
            result.append(occurrence)
        return result, 200
    else:
        return "Not found", 404


@functools.lru_cache(maxsize=64)
def get_association(identifier):
    association = GetAssociationCommand(database_path, identifier).do()
    if association:
        # TODO: Implementation.
        return "Association found", 200
    else:
        return "Not found", 404


def get_associations(identifier):
    associations = GetAssociationGroupsCommand(database_path, identifier).do()
    if len(associations):
        level1 = []
        for instance_of in associations.dict:
            level2 = []
            for role in associations.dict[instance_of]:
                level3 = []
                for topic_ref in associations[instance_of, role]:
                    topic3 = GetTopicCommand(database_path, topic_ref).do()
                    level3.append({'text': topic3.first_base_name.name, 'href': topic_ref, 'instanceOf': instance_of})
                topic2 = GetTopicCommand(database_path, role).do()
                level2.append({'text': topic2.first_base_name.name, 'nodes': level3})
            topic1 = GetTopicCommand(database_path, instance_of).do()
            level1.append({'text': topic1.first_base_name.name, 'nodes': level2})
        return level1, 200
    else:
        return "Not found", 404


@functools.lru_cache(maxsize=64)
def get_metadatum(identifier):
    metadatum = GetMetadatumCommand(database_path, identifier).do()
    if metadatum:
        # TODO: Implementation.
        return "Metadatum found", 200
    else:
        return "Not found", 404


def get_metadata(identifier):
    metadata = GetMetadataCommand(database_path, identifier).do()
    if metadata:
        # TODO: Implementation.
        return "Metadata found", 200
    else:
        return "Not found", 404


@functools.lru_cache(maxsize=64)
def get_scene(identifier):
    scene = GetSceneCommand(database_path, identifier).do()
    if scene:
        assets = []
        props = []
        characters = []
        paths = []
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
        entities = {
            'props': props,
            'characters': characters
        }
        for asset in scene.assets:
            assets.append({
                'reference': asset.reference,
                'instanceOf': asset.instance_of
            })
        for path in scene.paths:
            paths.append({
                'direction': path.direction,
                'to': path.to
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
                'entities': entities,
                'paths': paths
            }
        }
        return result, 200
    else:
        return "Not found", 404


@functools.lru_cache(maxsize=64)
def get_prop(identifier):
    prop = GetPropCommand(database_path, identifier).do()
    if prop:
        assets = []
        for asset in prop.assets:
            assets.append({
                'reference': asset.reference,
                'instanceOf': asset.instance_of
            })
        result = {
            'prop': {
                'identifier': prop.identifier,
                'name': prop.name,
                'location': prop.location,
                'rotation': prop.rotation,
                'scale': prop.scale,
                'assets': assets
            }
        }
        return result, 200
    else:
        return "Not found", 404


@functools.lru_cache(maxsize=64)
def get_character(identifier):
    character = GetCharacterCommand(database_path, identifier).do()
    if character:
        assets = []
        for asset in character.assets:
            assets.append({
                'reference': asset.reference,
                'instanceOf': asset.instance_of
            })
        result = {
            'character': {
                'identifier': character.identifier,
                'name': character.name,
                'location': character.location,
                'rotation': character.rotation,
                'scale': character.scale,
                'assets': assets
            }
        }
        return result, 200
    else:
        return "Not found", 404
