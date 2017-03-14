import graphene
import os

from flask import Flask, render_template, url_for
from flask_foundation import Foundation
from flask_graphql import GraphQLView

app = Flask(__name__)

Foundation(app)

app.config['FOUNDATION_USE_MINIFIED'] = True
app.config['FOUNDATION_USE_CDN'] = True
app.config['SECRET_KEY'] = 'devkey'

class Query(graphene.ObjectType):
    hello = graphene.String()

    def resolve_hello(self, args, context, info):
        return 'World'

schema = graphene.Schema(query=Query)


app.add_url_rule('/graphql', view_func=GraphQLView.as_view('graphql',
                                                           schema=schema,
                                                           graphiql=True,
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
