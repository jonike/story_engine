"""
StoryTechnologies API functions. Part of the StoryTechnologies project.

July 09, 2016
Brett Alistair Kromkamp (brett.kromkamp@gmail.com)
"""

import base64
import functools

from topicdb.core.store.retrievaloption import RetrievalOption

from storyengine.core.store.scenestore import SceneStore
from storyengine.core.models.character import Character
from storyengine.core.models.prop import Prop


scene_store = SceneStore("localhost", "storytech", "5t0ryt3ch!")
scene_store.open()


def get_topic_identifiers(topic_map_identifier, query, offset=0, limit=100):
    result = scene_store.get_topic_identifiers(topic_map_identifier, query, offset, limit)
    # TODO: Filter out anything that is not either a prop, character, or scene.
    if result:
        return result, 200
    else:
        return "Not found", 404


@functools.lru_cache(maxsize=64)
def get_topic(topic_map_identifier, identifier):
    topic = scene_store.get_topic(topic_map_identifier, identifier, resolve_attributes=RetrievalOption.RESOLVE_ATTRIBUTES)
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


def get_topics(topic_map_identifier, instance_of='topic', offset=0, limit=100):
    topics = scene_store.get_topics(topic_map_identifier, instance_of=instance_of, offset=offset, limit=limit)
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
            topic_json = {
                'topic': {
                    'identifier': topic.identifier,
                    'firstBaseName': topic.first_base_name.name,
                    'baseNames': base_names,
                    'instanceOf': topic.instance_of,
                    'attributes': attributes
                }
            }
            result.append(topic_json)
        return result, 200
    else:
        return "Not found", 404


def get_topics_hierarchy(topic_map_identifier, identifier):

    def build_topics_hierarchy(inner_identifier):
        # JSON data structure suitable for the RGraph visualization from the
        # JavaScript InfoViz Toolkit (https://philogb.github.io/jit/)

        parent_identifier = tree[inner_identifier].parent
        base_name = tree[inner_identifier].topic.first_base_name.name
        instance_of = tree[inner_identifier].topic.instance_of
        children = tree[inner_identifier].children

        if instance_of == 'scene':
            node_data = {
                '$color': '#00ff00'
            }
        elif instance_of == 'character':
            node_data = {
                '$color': '#ff0000'
            }
        elif instance_of == 'prop':
            node_data = {
                '$color': '#0000ff'
            }
        else:
            node_data = {
                '$color': '#a6a6a6'
            }

        node = {
            'id': inner_identifier,
            'name': base_name,
            'instanceOf': instance_of,
            'data': node_data,
            'children': []
        }
        result[inner_identifier] = node

        if parent_identifier is not None:
            parent = result[parent_identifier]
            parent_children = parent['children']
            parent_children.append(node)
            parent['children'] = parent_children

        for child in children:
            build_topics_hierarchy(child)

    tree = scene_store.get_topics_hierarchy(topic_map_identifier, identifier)
    if len(tree) > 1:
        result = {}
        build_topics_hierarchy(identifier)
        return result[identifier], 200
    else:
        return "Not found", 404


@functools.lru_cache(maxsize=64)
def get_occurrence(topic_map_identifier, identifier):
    occurrence = scene_store.get_occurrence(topic_map_identifier, identifier,
                                            inline_resource_data=RetrievalOption.DONT_INLINE_RESOURCE_DATA)
    if occurrence:
        # TODO: Implementation.
        return "Occurrence found", 200
    else:
        return "Not found", 404


# ========== FIX ME ==========
def get_topic_occurrences(topic_map_identifier, identifier, instance_of=None):
    occurrences = scene_store.get_topic_occurrences(topic_map_identifier, identifier,
                                                    instance_of=instance_of,
                                                    inline_resource_data=RetrievalOption.INLINE_RESOURCE_DATA,
                                                    resolve_attributes=RetrievalOption.DONT_RESOLVE_ATTRIBUTES)
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
            occurrence_json = {
                'occurrence': {
                    'identifier': occurrence.identifier,
                    'instanceOf': occurrence.instance_of,
                    'scope': occurrence.scope,
                    'resourceRef': occurrence.resource_ref,
                    'resourceData': occurrence.resource_data.decode("utf-8"),
                    'language': occurrence.language.name,
                    'attributes': attributes
                }
            }
            result.append(occurrence_json)
        return result, 200
    else:
        return "Not found", 404
# ========== FIX ME ==========


@functools.lru_cache(maxsize=64)
def get_association(topic_map_identifier, identifier):
    association = scene_store.get_association(topic_map_identifier, identifier)
    if association:
        # TODO: Implementation.
        return "Association found", 200
    else:
        return "Not found", 404


def get_associations(topic_map_identifier, identifier):
    associations = scene_store.get_association_groups(topic_map_identifier, identifier)
    if len(associations):
        level1 = []
        for instance_of in associations.dict:
            level2 = []
            for role in associations.dict[instance_of]:
                level3 = []
                for topic_ref in associations[instance_of, role]:
                    topic3 = scene_store.get_topic(topic_map_identifier, topic_ref)
                    level3.append({'text': topic3.first_base_name.name, 'href': topic_ref, 'instanceOf': instance_of})
                topic2 = scene_store.get_topic(topic_map_identifier, role)
                level2.append({'text': topic2.first_base_name.name, 'nodes': level3})
            topic1 = scene_store.get_topic(topic_map_identifier, instance_of)
            level1.append({'text': topic1.first_base_name.name, 'nodes': level2})
        return level1, 200
    else:
        return "Not found", 404


@functools.lru_cache(maxsize=64)
def get_attribute(topic_map_identifier, identifier):
    attribute = scene_store.get_attribute(topic_map_identifier, identifier)
    if attribute:
        # TODO: Implementation.
        return "Attribute found", 200
    else:
        return "Not found", 404


def get_attributes(topic_map_identifier, identifier):
    attributes = scene_store.get_attributes(topic_map_identifier, identifier)
    if attributes:
        # TODO: Implementation.
        return "Attributes found", 200
    else:
        return "Not found", 404


@functools.lru_cache(maxsize=64)
def get_scene(topic_map_identifier, identifier):
    scene = scene_store.get_scene(topic_map_identifier, identifier)
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
                'destination': path.destination
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
def get_scene_tags(topic_map_identifier, identifier):
    entities_tags = scene_store.get_entities_tags(topic_map_identifier, identifier)
    if entities_tags:
        result = []
        for tag, tagged_entities in entities_tags.items():
            result.append({
                'tag': tag,
                'entityIdentifiers': list(tagged_entities)
            })
        return result, 200
    else:
        return "Not found", 404


@functools.lru_cache(maxsize=64)
def get_prop(topic_map_identifier, identifier):
    prop = scene_store.get_prop(topic_map_identifier, identifier)
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
def get_character(topic_map_identifier, identifier):
    character = scene_store.get_character(topic_map_identifier, identifier)
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


@functools.lru_cache(maxsize=64)
def get_story(story_identifier):
    story = scene_store.get_topic_map(story_identifier)
    if story:
        result = {
            'story': {
                'identifier': story.identifier,
                'title': story.title,
                'topicMapIdentifier': story.topic_map_identifier,
                'startSceneIdentifier': story.entry_topic_identifier,
                'description': story.description
            }
        }
        return result, 200
    else:
        return "Not found", 404


def get_stories():
    stories = scene_store.get_topic_maps()
    if stories:
        result = []
        for story in stories:
            story_json = {
                'story': {
                    'identifier': story.identifier,
                    'title': story.title,
                    'topicMapIdentifier': story.topic_map_identifier,
                    'startSceneIdentifier': story.entry_topic_identifier,
                    'description': story.description
                }
            }
            result.append(story_json)
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
