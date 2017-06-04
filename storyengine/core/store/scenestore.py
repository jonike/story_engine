"""
TopicStore class. Part of the StoryTechnologies project.

February 25, 2017
Brett Alistair Kromkamp (brett.kromkamp@gmail.com)
"""

from topicdb.core.models.association import Association
from topicdb.core.models.attribute import Attribute
from topicdb.core.models.occurrence import Occurrence
from topicdb.core.models.topic import Topic
from topicdb.core.store.ontologymode import OntologyMode
from topicdb.core.store.retrievaloption import RetrievalOption
from topicdb.core.store.topicstore import TopicStore
from storyengine.core.models.asset import Asset
from storyengine.core.models.character import Character
from storyengine.core.models.path import Path
from storyengine.core.models.prop import Prop
from storyengine.core.models.scene import Scene


class SceneStore:

    def __init__(self, username, password, host='localhost', port=5432):
        self.topic_store = TopicStore(username, password, host, port)

    def open(self):
        self.topic_store.open()

    def close(self):
        self.topic_store.close()

    def get_character(self, topic_map_identifier, identifier):
        result = None
        topic = self.topic_store.get_topic(topic_map_identifier, identifier,
                                           resolve_attributes=RetrievalOption.RESOLVE_ATTRIBUTES)
        if topic:
            result = Character(topic.identifier, topic.first_base_name.name)
            result.description = topic.get_attribute_by_name('description').value if topic.get_attribute_by_name('description') else None
            result.location = topic.get_attribute_by_name('location').value
            result.rotation = topic.get_attribute_by_name('rotation').value
            result.scale = topic.get_attribute_by_name('scale').value

            occurrences = self.topic_store.get_topic_occurrences(topic_map_identifier, identifier)
            for occurrence in occurrences:
                result.add_asset(Asset(occurrence.instance_of, occurrence.resource_ref))

            attributes = [attribute for attribute in topic.attributes if
                          attribute.name not in ('description', 'location', 'rotation', 'scale')]
            result.add_attributes(attributes)
        return result

    def get_prop(self, topic_map_identifier, identifier):
        result = None
        topic = self.topic_store.get_topic(topic_map_identifier, identifier,
                                           resolve_attributes=RetrievalOption.RESOLVE_ATTRIBUTES)
        if topic:
            result = Prop(topic.identifier, topic.first_base_name.name)
            result.description = topic.get_attribute_by_name('description').value if topic.get_attribute_by_name('description') else None
            result.location = topic.get_attribute_by_name('location').value
            result.rotation = topic.get_attribute_by_name('rotation').value
            result.scale = topic.get_attribute_by_name('scale').value

            occurrences = self.topic_store.get_topic_occurrences(topic_map_identifier, identifier)
            for occurrence in occurrences:
                result.add_asset(Asset(occurrence.instance_of, occurrence.resource_ref))

            attributes = [attribute for attribute in topic.attributes if
                          attribute.name not in ('description', 'location', 'rotation', 'scale')]
            result.add_attributes(attributes)
        return result

    def get_scene(self, topic_map_identifier, identifier):
        result = None
        topic = self.topic_store.get_topic(topic_map_identifier, identifier,
                                           resolve_attributes=RetrievalOption.RESOLVE_ATTRIBUTES)
        if topic:
            result = Scene(topic.identifier, topic.first_base_name.name)
            result.description = topic.get_attribute_by_name('description').value if topic.get_attribute_by_name('description') else None
            result.location = topic.get_attribute_by_name('location').value
            result.rotation = topic.get_attribute_by_name('rotation').value
            result.scale = topic.get_attribute_by_name('scale').value
            result.ordinal = topic.get_attribute_by_name('ordinal').value if topic.get_attribute_by_name('ordinal') else None

            result.add_associations(self.topic_store.get_topic_associations(topic_map_identifier, identifier))

            # Add scene's entities (props and characters).
            if result.associations:
                groups = self.topic_store.get_association_groups(topic_map_identifier, identifier)
                for instance_of in groups.dict:
                    for role in groups.dict[instance_of]:
                        for topic_ref in groups[instance_of, role]:
                            if topic_ref == identifier:
                                continue
                            if instance_of == 'navigation':
                                path = Path(role, topic_ref)
                                result.add_path(path)
                            elif instance_of == 'prop':
                                result.add_entity(self.get_prop(topic_map_identifier, topic_ref))
                            elif instance_of == 'character':
                                result.add_entity(self.get_prop(topic_map_identifier, topic_ref))
                            elif instance_of == 'categorization':  # Tags.
                                result.add_tag(topic_ref)

            occurrences = self.topic_store.get_topic_occurrences(topic_map_identifier, identifier)
            for occurrence in occurrences:
                result.add_asset(Asset(occurrence.instance_of, occurrence.resource_ref))

            attributes = [attribute for attribute in topic.attributes
                          if attribute.name not in ('description', 'location', 'rotation', 'scale', 'ordinal')]
            result.add_attributes(attributes)
            result.entities_tags = self.get_entities_tags(topic_map_identifier, identifier)
        return result

    def set_character(self, topic_map_identifier, character, scene_identifier):
        topic = Topic(character.identifier, character.instance_of, character.name)
        self.topic_store.set_topic(topic_map_identifier, topic)

        description_attribute = Attribute('description', character.description, topic.identifier) if character.description else None
        location_attribute = Attribute('location', character.location, topic.identifier)
        rotation_attribute = Attribute('rotation', character.rotation, topic.identifier)
        scale_attribute = Attribute('scale', character.scale, topic.identifier)

        attributes = [x for x in [description_attribute, location_attribute, rotation_attribute, scale_attribute] if x is not None]
        self.topic_store.set_attributes(topic_map_identifier, attributes)

        for asset in character.assets:
            occurrence = Occurrence(
                instance_of=asset.instance_of,
                topic_identifier=topic.identifier,
                resource_ref=asset.reference,
                resource_data=asset.data)
            self.topic_store.set_occurrence(topic_map_identifier, occurrence)

        scene_association = Association(
            instance_of='character',
            src_topic_ref=topic.identifier,  # The character's reference.
            dest_topic_ref=scene_identifier,
            src_role_spec='included-in',
            dest_role_spec='includes')
        self.topic_store.set_association(topic_map_identifier, scene_association)

        book_association = Association(
            instance_of='character',
            src_topic_ref=topic.identifier,  # The character's reference.
            dest_topic_ref='genesis',
            src_role_spec='included-in',
            dest_role_spec='includes',
            scope='book')
        self.topic_store.set_association(topic_map_identifier, book_association)

    def set_prop(self, topic_map_identifier, prop, scene_identifier):
        topic = Topic(prop.identifier, prop.instance_of, prop.name)
        self.topic_store.set_topic(topic_map_identifier, topic)

        description_attribute = Attribute('description', prop.description, topic.identifier) if prop.description else None
        location_attribute = Attribute('location', prop.location, topic.identifier)
        rotation_attribute = Attribute('rotation', prop.rotation, topic.identifier)
        scale_attribute = Attribute('scale', prop.scale, topic.identifier)

        attributes = [x for x in [description_attribute, location_attribute, rotation_attribute, scale_attribute] if x is not None]
        self.topic_store.set_attributes(topic_map_identifier, attributes)

        for asset in prop.assets:
            occurrence = Occurrence(
                instance_of=asset.instance_of,
                topic_identifier=topic.identifier,
                resource_ref=asset.reference,
                resource_data=asset.data)
            self.topic_store.set_occurrence(topic_map_identifier, occurrence)

        scene_association = Association(
            instance_of='prop',
            src_topic_ref=topic.identifier,  # The prop's reference.
            dest_topic_ref=scene_identifier,
            src_role_spec='included-in',
            dest_role_spec='includes')
        self.topic_store.set_association(topic_map_identifier, scene_association)

        book_association = Association(
            instance_of='prop',
            src_topic_ref=topic.identifier,  # The prop's reference.
            dest_topic_ref='genesis',
            src_role_spec='included-in',
            dest_role_spec='includes',
            scope='book')
        self.topic_store.set_association(topic_map_identifier, book_association)

    def set_scene(self, topic_map_identifier, scene):
        topic = Topic(scene.identifier, scene.instance_of, scene.name)
        self.topic_store.set_topic(topic_map_identifier, topic)

        description_attribute = Attribute('description', scene.description, topic.identifier) if scene.description else None
        location_attribute = Attribute('location', scene.location, topic.identifier)
        rotation_attribute = Attribute('rotation', scene.rotation, topic.identifier)
        scale_attribute = Attribute('scale', scene.scale, topic.identifier)
        ordinal_attribute = Attribute('ordinal', scene.ordinal, topic.identifier) if scene.ordinal else None

        attributes = [x for x in [description_attribute, location_attribute, rotation_attribute, scale_attribute, ordinal_attribute] if x is not None]
        self.topic_store.set_attributes(topic_map_identifier, attributes)

        for asset in scene.assets:
            occurrence = Occurrence(
                instance_of=asset.instance_of,
                topic_identifier=topic.identifier,
                resource_ref=asset.reference,
                resource_data=asset.data)
            self.topic_store.set_occurrence(topic_map_identifier, occurrence)

        book_association = Association(
            instance_of='scene',
            src_topic_ref=topic.identifier,  # The scene's reference.
            dest_topic_ref='genesis',
            src_role_spec='included-in',
            dest_role_spec='includes',
            scope='book')
        self.topic_store.set_association(topic_map_identifier, book_association)

    def set_navigation(self, topic_map_identifier, src_scene_identifier, dest_scene_identifier,
                       src_scene_role='previous',
                       dest_scene_role='next'):
        association = Association(
            instance_of='navigation',
            src_topic_ref=src_scene_identifier,
            dest_topic_ref=dest_scene_identifier,
            src_role_spec=src_scene_role,
            dest_role_spec=dest_scene_role)
        self.topic_store.set_association(topic_map_identifier, association)

    def get_entities_tags(self, topic_map_identifier, identifier):
        result = {}

        # Map from topics with tags to tags with topics. For example, the below topic -> tags mappings:
        # topic1 -> tag1, tag2, tag3
        # topic2 -> tag2, tag4
        # topic3 -> tag3, tag4, tag5
        # topic4 -> tag4, tag5, tag6, tag7
        # topic5 -> tag1, tag8
        #
        # Should become the following tag -> topics mappings:
        # tag1 -> topic1, topic5
        # tag2 -> topic1, topic2
        # tag3 -> topic1, topic3
        # tag4 -> topic2, topic3, topic4
        # tag5 -> topic3, topic4
        # tag6 -> topic4
        # tag7 -> topic4
        # tag8 -> topic5

        topic_tags = {}
        groups = self.topic_store.get_association_groups(topic_map_identifier, identifier)
        for instance_of in groups.dict:
            for role in groups.dict[instance_of]:
                for topic_ref in groups[instance_of, role]:
                    if topic_ref == identifier:
                        continue
                    if instance_of == 'prop' or instance_of == 'character':
                        topic_tags[topic_ref] = self.topic_store.get_tags(topic_map_identifier, topic_ref)

        for topic, tags in topic_tags.items():
            for tag in tags:
                if tag not in result.keys():
                    result[tag] = {topic}  # Topics set. Will guarantee that topic identifiers are unique for each tag.
                else:
                    result[tag].add(topic)
        return result

    # ========== TOPIC STORE PROXY METHODS ==========

    def get_association(self, topic_map_identifier, identifier,
                        language=None,
                        resolve_attributes=RetrievalOption.DONT_RESOLVE_ATTRIBUTES,
                        resolve_occurrences=RetrievalOption.DONT_RESOLVE_OCCURRENCES):
        return self.topic_store.get_association(topic_map_identifier, identifier, language, resolve_attributes, resolve_occurrences)

    def get_association_groups(self, topic_map_identifier, identifier='', associations=None, instance_of=None, scope=None):
        return self.topic_store.get_association_groups(topic_map_identifier, identifier, associations, instance_of=instance_of, scope=scope)

    def get_attributes(self, topic_map_identifier, entity_identifier, scope=None, language=None):
        return self.topic_store.get_attributes(topic_map_identifier, entity_identifier, scope, language)

    def get_attribute(self, topic_map_identifier, identifier):
        return self.topic_store.get_attribute(topic_map_identifier, identifier)

    def get_occurrence(self, topic_map_identifier, identifier,
                       inline_resource_data=RetrievalOption.DONT_INLINE_RESOURCE_DATA,
                       resolve_attributes=RetrievalOption.DONT_RESOLVE_ATTRIBUTES):
        return self.topic_store.get_occurrence(topic_map_identifier, identifier, inline_resource_data, resolve_attributes)

    def get_topic_occurrences(self, topic_map_identifier, identifier,
                              instance_of=None,
                              scope=None,
                              language=None,
                              inline_resource_data=RetrievalOption.DONT_INLINE_RESOURCE_DATA,
                              resolve_attributes=RetrievalOption.DONT_RESOLVE_ATTRIBUTES):
        return self.topic_store.get_topic_occurrences(topic_map_identifier, identifier, instance_of, scope, language, inline_resource_data, resolve_attributes)

    def get_topic(self, topic_map_identifier, identifier,
                  language=None,
                  resolve_attributes=RetrievalOption.DONT_RESOLVE_ATTRIBUTES,
                  resolve_occurrences=RetrievalOption.DONT_RESOLVE_OCCURRENCES):
        return self.topic_store.get_topic(topic_map_identifier, identifier, language, resolve_attributes, resolve_occurrences)

    def get_topic_identifiers(self, topic_map_identifier, query, offset=0, limit=100):
        return self.topic_store.get_topic_identifiers(topic_map_identifier, query, offset, limit)

    def get_topics(self, topic_map_identifier,
                   instance_of=None,
                   language=None,
                   offset=0,
                   limit=100,
                   resolve_attributes=RetrievalOption.DONT_RESOLVE_ATTRIBUTES):
        return self.topic_store.get_topics(topic_map_identifier, instance_of, language, offset, limit, resolve_attributes)

    def get_topics_network(self, topic_map_identifier, identifier,
                           maximum_depth=10,
                           cumulative_depth=0,
                           accumulative_tree=None,
                           accumulative_nodes=None):
        return self.topic_store.get_topics_network(topic_map_identifier,
                                                   identifier,
                                                   maximum_depth,
                                                   cumulative_depth,
                                                   accumulative_tree,
                                                   accumulative_nodes,
                                                   instance_of=['prop', 'character', 'scene', 'navigation'],
                                                   scope='*')

    def get_topic_map(self, identifier):
        return self.topic_store.get_topic_map(identifier)

    def get_topic_maps(self):
        return self.topic_store.get_topic_maps()

    def set_attribute(self, topic_map_identifier, attribute, ontology_mode=OntologyMode.LENIENT):
        self.topic_store.set_attribute(topic_map_identifier, attribute, ontology_mode)

    def set_tags(self, topic_map_identifier, identifier, tags):
        self.topic_store.set_tags(topic_map_identifier, identifier, tags)

    def set_occurrence(self, topic_map_identifier, occurrence, ontology_mode=OntologyMode.STRICT):
        self.topic_store.set_occurrence(topic_map_identifier, occurrence, ontology_mode)

    def set_topic(self, topic_map_identifier, topic, ontology_mode=OntologyMode.STRICT):
        self.topic_store.set_topic(topic_map_identifier, topic, ontology_mode)
