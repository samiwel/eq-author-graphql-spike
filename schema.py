import graphene
import json


schema_json = None
with open('data/schema.json', encoding='utf-8') as schema_file:
    schema_json = json.load(schema_file)
    schema_file.close()

class Answer(graphene.ObjectType):
    id = graphene.String()
    parent_answer_id = graphene.String()
    q_code = graphene.String()
    label = graphene.String()
    guidance = graphene.String()
    description = graphene.String()
    type = graphene.String()
    options = graphene.String()
    mandatory = graphene.String()
    alias = graphene.String()
    repeats = graphene.String()
    validation = graphene.String()
    calculated = graphene.String()

    def resolve_id(self, args, context, info):
        return self.get('id')

    def resolve_parent_answer_id(self, args, context, info):
        return self.get('parent_answer_id')

    def resolve_q_code(self, args, context, info):
        return self.get('q_code')

    def resolve_label(self, args, context, info):
        return self.get('label')

    def resolve_guidance(self, args, context, info):
        return self.get('guidance')

    def resolve_description(self, args, context, info):
        return self.get('description')

    def resolve_type(self, args, context, info):
        return self.get('type')

    def resolve_options(self, args, context, info):
        return self.get('options')

    def resolve_mandatory(self, args, context, info):
        return self.get('mandatory')

    def resolve_alias(self, args, context, info):
        return self.get('alias')

    def resolve_repeats(self, args, context, info):
        return self.get('repeats')

    def resolve_validation(self, args, context, info):
        return self.get('validation')

    def resolve_calculated(self, args, context, info):
        return self.get('calculated')


class Question(graphene.ObjectType):
    id = graphene.String()
    title = graphene.String()
    number = graphene.String()
    description = graphene.String()
    guidance = graphene.String()
    skip_condition = graphene.String()
    type = graphene.String()
    answers = graphene.List(Answer, index=graphene.Argument(graphene.Int))

    def resolve_id(self, args, context, info):
        return self.get('id')

    def resolve_title(self, args, context, info):
        return self.get('title')

    def resolve_number(self, args, context, info):
        return self.get('number')

    def resolve_description(self, args, context, info):
        return self.get('description')

    def resolve_guidance(self, args, context, info):
        return self.get('guidance')

    def resolve_skip_condition(self, args, context, info):
        return self.get('skip_condition')

    def resolve_type(self, args, context, info):
        return self.get('type')

    def resolve_answers(self, args, context, info):
        index = args.get('index')
        if index is None:
            return self.get('answers')
        else:
            return [self['answers'][index]]


class Section(graphene.ObjectType):
    id = graphene.String()
    title = graphene.String()
    number = graphene.String()
    description = graphene.String()
    questions = graphene.List(Question, index=graphene.Argument(graphene.Int))

    def resolve_id(self, args, context, info):
        return self.get('id')

    def resolve_title(self, args, context, info):
        return self.get('title')

    def resolve_number(self, args, context, info):
        return self.get('number')

    def resolve_description(self, args, context, info):
        return self.get('description')

    def resolve_questions(self, args, context, info):
        index = args.get('index')
        if index is None:
            return self.get('questions')
        else:
            return [self['questions'][index]]


class Block(graphene.ObjectType):
    id = graphene.String()
    title = graphene.String()
    type = graphene.String()
    description = graphene.String()
    information_to_provide = graphene.String()
    basis_for_completion = graphene.String()
    routing_rules = graphene.String()
    skip_condition = graphene.String()
    sections = graphene.List(Section, index=graphene.Argument(graphene.Int))

    def resolve_id(self, args, context, info):
        return self.get('id')

    def resolve_title(self, args, context, info):
        return self.get('title')

    def resolve_type(self, args, context, info):
        return self.get('type')

    def resolve_description(self, args, context, info):
        return self.get('description')

    def resolve_information_to_provide(self, args, context, info):
        return self.get('information_to_provide')

    def resolve_basis_for_completion(self, args, context, info):
        return self.get('basis_for_completion')

    def resolve_routing_rules(self, args, context, info):
        return self.get('routing_rules')

    def resolve_skip_condition(self, args, context, info):
        return self.get('skip_condition')

    def resolve_sections(self, args, context, info):
        index = args.get('index')
        if index is None:
            return self.get('sections')
        else:
            return [self['sections'][index]]


class Group(graphene.ObjectType):
    id = graphene.ID()
    title = graphene.String()
    completed_id = graphene.String()
    highlight_when = graphene.String()
    hide_in_navigation = graphene.String()
    skip_condition = graphene.String()
    routing_rules = graphene.String()
    blocks = graphene.List(Block, index=graphene.Argument(graphene.Int))

    def resolve_id(self, args, context, info):
        return self.get('id')

    def resolve_title(self, args, context, info):
        return self.get('title')

    def resolve_completed_id(self, args, context, info):
        return self.get('completed_id')

    def resolve_highlight_when(self, args, context, info):
        return self.get('highlight_when')

    def resolve_hide_in_navigation(self, args, context, info):
        return self.get('hide_in_navigation')

    def resolve_skip_condition(self, args, context, info):
        return self.get('skip_condition')

    def resolve_routing_rules(self, args, context, info):
        return self.get('routing_rules')

    def resolve_blocks(self, args, context, info):
        index = args.get('index')
        if index is None:
            return self.get('blocks')
        else:
            return [self['blocks'][index]]


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