"""
StoryTechnologies API functions. Part of the StoryTechnologies Builder project.

July 09, 2016
Brett Alistair Kromkamp (brett.kromkamp@gmail.com)
"""

import base64
import functools

from storyengine.core.models.character import Character
from storyengine.core.models.prop import Prop
from storyengine.store.commands.association.getassociation import GetAssociation
from storyengine.store.commands.association.getassociationgroups import GetAssociationGroups
from storyengine.store.commands.attribute.getattributes import GetAttributes
from storyengine.store.commands.attribute.getattribute import GetAttribute
from storyengine.store.commands.occurrence.getoccurrence import GetOccurrence
from storyengine.store.commands.occurrence.getoccurrences import GetOccurrences
from storyengine.store.commands.topic.gettopic import GetTopic
from storyengine.store.commands.topic.gettopicidentifiers import GetTopicIdentifiers
from storyengine.store.commands.topic.gettopics import GetTopics
from storyengine.store.retrievaloption import RetrievalOption
from storyengine.core.commands.scene.getscene import GetScene
from storyengine.core.commands.scene.getprop import GetProp
from storyengine.core.commands.scene.getcharacter import GetCharacter


database_path = '/home/brettk/Source/storytechnologies/story-engine/data/demo1.sqlite'


def get_topic_identifiers(query, offset=0, limit=100, filter_entities=RetrievalOption.filter_entities):
    # TODO: Implement 'filter entities' switch.
    result = GetTopicIdentifiers(database_path, query, filter_entities, offset, limit).do()
    if result:
        return result, 200
    else:
        return "Not found", 404


@functools.lru_cache(maxsize=64)
def get_topic(identifier):
    topic = GetTopic(database_path, identifier, RetrievalOption.resolve_attributes).do()
    if topic:
        attributes = []
        base_names = []
        for attribute in topic.attributes:
            attributes.append({
                'identifier': attribute.identifier,
                'name': attribute.name,
                'value': attribute.value,
                'dataType': attribute.data_type.name,
                'scope': attribute.scope,
                'language': attribute.language.name
            })
        for base_name in topic.base_names:
            base_names.append({
                'identifier': base_name.identifier,
                'name': base_name.name,
                'language': base_name.language.name
            })
        result = {
            'topic': {
                'identifier': topic.identifier,
                'firstBaseName': topic.first_base_name.name,
                'baseNames': base_names,
                'instanceOf': topic.instance_of,
                'attributes': attributes
            }
        }
        return result, 200
    else:
        return "Not found", 404


def get_topics(instance_of='topic', offset=0, limit=100):
    topics = GetTopics(database_path, instance_of=instance_of, offset=offset, limit=limit).do()
    if topics:
        result = []
        for topic in topics:
            attributes = []
            base_names = []
            for attribute in topic.attributes:
                attributes.append({
                    'identifier': attribute.identifier,
                    'name': attribute.name,
                    'value': attribute.value,
                    'dataType': attribute.data_type.name,
                    'scope': attribute.scope,
                    'language': attribute.language.name
                })
            for base_name in topic.base_names:
                base_names.append({
                    'identifier': base_name.identifier,
                    'name': base_name.name,
                    'language': base_name.language.name
                })
            topic = {
                'topic': {
                    'identifier': topic.identifier,
                    'firstBaseName': topic.first_base_name.name,
                    'baseNames': base_names,
                    'instanceOf': topic.instance_of,
                    'attributes': attributes
                }
            }
            result.append(topic)
        return result, 200
    else:
        return "Not found", 404

    
@functools.lru_cache(maxsize=64)
def get_occurrence(identifier, inline_resource_data=RetrievalOption.dont_inline_resource_data):
    occurrence = GetOccurrence(database_path, identifier, inline_resource_data).do()
    if occurrence:
        # TODO: Implementation.
        return "Occurrence found", 200
    else:
        return "Not found", 404


def get_occurrences(identifier,
                    inline_resource_data=RetrievalOption.dont_inline_resource_data,
                    resolve_attributes=RetrievalOption.dont_resolve_attributes,
                    instance_of=''):
    occurrences = GetOccurrences(database_path, identifier, inline_resource_data, resolve_attributes, instance_of).do()
    if occurrences:
        result = []
        for occurrence in occurrences:
            attributes = []
            for attribute in occurrence.attributes:
                attributes.append({
                    'identifier': attribute.identifier,
                    'name': attribute.name,
                    'value': attribute.value,
                    'dataType': attribute.data_type.name,
                    'scope': attribute.scope,
                    'language': attribute.language.name
                })
            if occurrence.resource_data is None:
                resource_data = None
            else:
                resource_data = base64.b64encode(occurrence.resource_data).decode('utf-8')
            occurrence = {
                'occurrence': {
                    'identifier': occurrence.identifier,
                    'instanceOf': occurrence.instance_of,
                    'scope': occurrence.scope,
                    'resourceRef': occurrence.resource_ref,
                    'resourceData': resource_data,
                    'language': occurrence.language.name,
                    'attributes': attributes
                }
            }
            result.append(occurrence)
        return result, 200
    else:
        return "Not found", 404


@functools.lru_cache(maxsize=64)
def get_association(identifier):
    association = GetAssociation(database_path, identifier).do()
    if association:
        # TODO: Implementation.
        return "Association found", 200
    else:
        return "Not found", 404


def get_associations(identifier):
    associations = GetAssociationGroups(database_path, identifier).do()
    if len(associations):
        level1 = []
        for instance_of in associations.dict:
            level2 = []
            for role in associations.dict[instance_of]:
                level3 = []
                for topic_ref in associations[instance_of, role]:
                    topic3 = GetTopic(database_path, topic_ref).do()
                    level3.append({'text': topic3.first_base_name.name, 'href': topic_ref, 'instanceOf': instance_of})
                topic2 = GetTopic(database_path, role).do()
                level2.append({'text': topic2.first_base_name.name, 'nodes': level3})
            topic1 = GetTopic(database_path, instance_of).do()
            level1.append({'text': topic1.first_base_name.name, 'nodes': level2})
        return level1, 200
    else:
        return "Not found", 404


@functools.lru_cache(maxsize=64)
def get_attribute(identifier):
    attribute = GetAttribute(database_path, identifier).do()
    if attribute:
        # TODO: Implementation.
        return "Attribute found", 200
    else:
        return "Not found", 404


def get_attributes(identifier):
    attributes = GetAttributes(database_path, identifier).do()
    if attributes:
        # TODO: Implementation.
        return "Attributes found", 200
    else:
        return "Not found", 404


@functools.lru_cache(maxsize=64)
def get_scene(identifier):
    scene = GetScene(database_path, identifier).do()
    if scene:
        assets = []
        props = []
        characters = []
        paths = []
        attributes = []
        entities_tags = []
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
        for attribute in scene.attributes:
            attributes.append({
                'identifier': attribute.identifier,
                'name': attribute.name,
                'value': attribute.value,
                'dataType': attribute.data_type.name,
                'scope': attribute.scope,
                'language': attribute.language.name
            })
        for tag, tagged_entities in scene.entities_tags.items():
            entities_tags.append({
                'tag': tag,
                'entityIdentifiers': list(tagged_entities)
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
                'paths': paths,
                'attributes': attributes,
                'tags': entities_tags
            }
        }
        return result, 200
    else:
        return "Not found", 404


@functools.lru_cache(maxsize=64)
def get_prop(identifier):
    prop = GetProp(database_path, identifier).do()
    if prop:
        assets = []
        attributes = []
        for asset in prop.assets:
            assets.append({
                'reference': asset.reference,
                'instanceOf': asset.instance_of
            })
        for attribute in prop.attributes:
            attributes.append({
                'identifier': attribute.identifier,
                'name': attribute.name,
                'value': attribute.value,
                'dataType': attribute.data_type.name,
                'scope': attribute.scope,
                'language': attribute.language.name
            })
        result = {
            'prop': {
                'identifier': prop.identifier,
                'name': prop.name,
                'location': prop.location,
                'rotation': prop.rotation,
                'scale': prop.scale,
                'assets': assets,
                'attributes': attributes
            }
        }
        return result, 200
    else:
        return "Not found", 404


@functools.lru_cache(maxsize=64)
def get_character(identifier):
    character = GetCharacter(database_path, identifier).do()
    if character:
        assets = []
        attributes = []
        for asset in character.assets:
            assets.append({
                'reference': asset.reference,
                'instanceOf': asset.instance_of
            })
        for attribute in character.attributes:
            attributes.append({
                'identifier': attribute.identifier,
                'name': attribute.name,
                'value': attribute.value,
                'dataType': attribute.data_type.name,
                'scope': attribute.scope,
                'language': attribute.language.name
            })
        result = {
            'character': {
                'identifier': character.identifier,
                'name': character.name,
                'location': character.location,
                'rotation': character.rotation,
                'scale': character.scale,
                'assets': assets,
                'attributes': attributes
            }
        }
        return result, 200
    else:
        return "Not found", 404


# POST /scenes
# POST /scenes/{identifier}/assets
# POST /scenes/{identifier}/attributes
# POST /paths
# POST /characters
# POST /characters/{identifier}/assets
# POST /props
# POST /props/{identifier}/assets

def set_scene():
    pass


def set_scene_asset():
    pass


def set_scene_attribute():
    pass


def set_path():
    pass


def set_character():
    pass


def set_character_asset():
    pass


def set_prop():
    pass


def set_prop_asset():
    pass
