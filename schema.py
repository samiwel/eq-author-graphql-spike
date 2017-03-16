import graphene
import json


schema_json = None
with open('data/schema.json', encoding='utf-8') as schema_file:
    schema_json = json.load(schema_file)
    schema_file.close()


class Group(graphene.ObjectType):
    id = graphene.ID()
    title = graphene.String()
    completed_id = graphene.String()
    highlight_when = graphene.String()
    hide_in_navigation = graphene.String()
    skip_condition = graphene.String()
    routing_rules = graphene.String()

    def resolve_id(self, args, context, info):
        print(args)
        return schema_json.get('groups')


class Survey(graphene.ObjectType):
    mime_type = graphene.String()
    questionnaire_id = graphene.String()
    schema_version = graphene.String()
    data_version = graphene.String()
    survey_id = graphene.String()
    title = graphene.String()
    description = graphene.String()
    theme = graphene.String()
    legal_basis = graphene.String()
    navigation = graphene.Boolean()
    groups = graphene.List(Group, index=graphene.Argument(graphene.Int))

    def resolve_mime_type(self, args, context, info):
        return schema_json.get('mime_type')

    def resolve_questionnaire_id(self, args, context, info):
        return schema_json.get('questionnaire_id')

    def resolve_schema_version(self, args, context, info):
        return schema_json.get('schema_version')

    def resolve_data_version(self, args, context, info):
        return schema_json.get('data_version')

    def resolve_survey_id(self, args, context, info):
        return schema_json.get('survey_id')

    def resolve_title(self, args, context, info):
        return schema_json.get('title')

    def resolve_description(self, args, context, info):
        return schema_json.get('description')

    def resolve_theme(self, args, context, info):
        return schema_json.get('theme')

    def resolve_legal_basis(self, args, context, info):
        return schema_json.get('legal_basis')

    def resolve_navigation(self, args, context, info):
        return schema_json.get('navigation')

    def resolve_groups(self, args, context, info):
        index = args.get('index')
        if index is None:
            return schema_json.get('groups')
        else:
            return [schema_json['groups'][index]]


class Query(graphene.ObjectType):
    survey = graphene.Field(Survey)

    def resolve_survey(self, args, context, info):
        return schema_json

schema = graphene.Schema(query=Query)