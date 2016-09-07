CREATE TABLE IF NOT EXISTS member (
    identifier TEXT PRIMARY KEY,
    role_spec TEXT,
    association_identifier_fk TEXT
);
CREATE INDEX IF NOT EXISTS member_1_index ON member (association_identifier_fk);

CREATE TABLE IF NOT EXISTS attribute (
    identifier TEXT,
    parent_identifier_fk TEXT,
    name TEXT,
    value TEXT,
    data_type TEXT,
    scope TEXT,
    language TEXT
);
CREATE UNIQUE INDEX IF NOT EXISTS attribute_1_index ON attribute (identifier, parent_identifier_fk, name, scope);
CREATE INDEX IF NOT EXISTS attribute_2_index ON attribute (name);
CREATE INDEX IF NOT EXISTS attribute_3_index ON attribute (identifier);
CREATE INDEX IF NOT EXISTS attribute_4_index ON attribute (parent_identifier_fk, language);
CREATE INDEX IF NOT EXISTS attribute_5_index ON attribute (parent_identifier_fk);
CREATE INDEX IF NOT EXISTS attribute_6_index ON attribute (parent_identifier_fk, name);

CREATE TABLE IF NOT EXISTS occurrence (
    identifier TEXT PRIMARY KEY,
    instance_of TEXT,
    scope TEXT,
    resource_ref TEXT,
    resource_data BLOB,
    topic_identifier_fk TEXT,
    language TEXT
);
CREATE INDEX IF NOT EXISTS occurrence_1_index ON occurrence (topic_identifier_fk, scope, language);
CREATE INDEX IF NOT EXISTS occurrence_2_index ON occurrence (topic_identifier_fk, instance_of, language);
CREATE INDEX IF NOT EXISTS occurrence_3_index ON occurrence (topic_identifier_fk);

CREATE TABLE IF NOT EXISTS topicref (
    topic_ref TEXT,
    member_identifier_fk TEXT
);
CREATE UNIQUE INDEX IF NOT EXISTS topicref_1_index ON topicref (topic_ref, member_identifier_fk);

CREATE TABLE IF NOT EXISTS topic (
    identifier TEXT,
    instance_of TEXT,
    scope TEXT
);
CREATE UNIQUE INDEX IF NOT EXISTS topic_1_index ON topic (identifier);
CREATE INDEX IF NOT EXISTS topic_2_index ON topic (instance_of);
CREATE INDEX IF NOT EXISTS topic_3_index ON topic (scope);
CREATE INDEX IF NOT EXISTS topic_4_index ON topic (identifier, scope);
CREATE INDEX IF NOT EXISTS topic_5_index ON topic (identifier, instance_of);

CREATE TABLE IF NOT EXISTS basename (
    identifier TEXT,
    name TEXT,
    topic_identifier_fk TEXT,
    language TEXT
);
CREATE UNIQUE INDEX IF NOT EXISTS basename_1_index ON basename (identifier, name, language);
CREATE INDEX IF NOT EXISTS basename_2_index ON basename (topic_identifier_fk);
CREATE INDEX IF NOT EXISTS basename_3_index ON basename (language, name);
CREATE INDEX IF NOT EXISTS basename_4_index ON basename (topic_identifier_fk, language);
