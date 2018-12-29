from flask import Flask, render_template
from flask_restful import Resource, Api

from .rest import Generate, Retrieve

app = Flask(__name__, static_folder='public')
api = Api(app)


@app.route('/')
def ui():
    return render_template('hp.html')


api.add_resource(Retrieve, '/get/<string:id_>')
api.add_resource(Generate, '/get/')

if __name__ == '__main__':
    app.run(debug=True)
