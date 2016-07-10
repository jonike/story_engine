"""
Scene API functions. Part of the StoryTechnologies Builder project.

July 09, 2016
Brett Alistair Kromkamp (brett.kromkamp@gmail.com)
"""

from engine.store.commands.topic.gettopic import GetTopicCommand
from engine.store.retrievaloption import RetrievalOption


database_path = '/home/brettk/Source/storytechnologies/story-engine/topics.db'


def get_topic(topic_identifier):
    get_topic_command = GetTopicCommand(database_path, topic_identifier, RetrievalOption.resolve_metadata)
    topic = get_topic_command.execute()
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
        return result
    else:
        return "Not found", 404


def get_occurrence(identifier):
    pass


def get_occurrences(topic_identifier):
    pass


def get_association(identifier):
    pass


def get_associations(topic_identifier):
    pass


def get_metadatum(identifier):
    pass


def get_metadata(entity_identifier):
    pass
