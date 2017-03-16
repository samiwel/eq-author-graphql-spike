from flask import Flask, render_template, url_for
from flask_foundation import Foundation
from flask_graphql import GraphQLView

from config import HOSTNAME, PORT, DEBUG
from schema import schema

app = Flask(__name__)

Foundation(app)

app.config['FOUNDATION_USE_MINIFIED'] = True
app.config['FOUNDATION_USE_CDN'] = True
app.config['SECRET_KEY'] = 'devkey'


app.add_url_rule('/graphql', view_func=GraphQLView.as_view('graphql',
                                                           schema=schema,
                                                           graphiql=DEBUG,
                                                           pretty=True))


@app.route('/')
def index():
    links = {
        'Home': url_for('index'),
        'GraphQL': url_for('graphql')
    }
    return render_template('index.html', links=links)


if __name__ == '__main__':
    app.run(HOSTNAME, port=PORT, debug=DEBUG)
