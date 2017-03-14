import graphene
import json
import os

from flask import Flask, render_template, url_for
from flask_foundation import Foundation
from flask_graphql import GraphQLView
from graphene.types.json import JSONString

app = Flask(__name__)

Foundation(app)

app.config['FOUNDATION_USE_MINIFIED'] = True
app.config['FOUNDATION_USE_CDN'] = True
app.config['SECRET_KEY'] = 'devkey'

schema_json = None
with open('data/schema.json') as schema_file:
    schema_json = json.load(schema_file)
    schema_file.close()

class Query(graphene.ObjectType):
    schema = JSONString()
    groups = JSONString()
    blocks = JSONString()
    questions = JSONString()

    def resolve_schema(self, args, context, info):
        return schema_json

    def resolve_groups(self, args, context, info):
        return schema_json['groups']

    def resolve_blocks(self, args, context, info):
        return schema_json['groups'][0]['blocks']

    def resolve_questions(self, args, context, info):
        return schema_json['groups'][0]['blocks'][0]['sections'][0]['questions']

schema = graphene.Schema(query=Query)
app.add_url_rule('/graphql', view_func=GraphQLView.as_view('graphql',
                                                           schema=schema,
                                                           graphiql=os.environ.get('DEBUG', False),
                                                           pretty=True))

@app.route('/')
def index():
    links = {
        'Home': url_for('index'),
        'GraphQL': url_for('graphql')
    }
    return render_template('index.html', links=links)


if __name__ == '__main__':
    app.run(os.environ.get('HOSTNAME', '0.0.0.0'),
            port=os.environ.get('PORT', 8080),
            debug=os.environ.get('DEBUG', False))
