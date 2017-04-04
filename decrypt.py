from flask import Flask, render_template, send_from_directory
from flask_restful import reqparse, Resource, Api
import json

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('static/js', path)

@app.route('/css/<path:path>')
def send_css(path):
    return send_from_directory('static/css', path)

if __name__ == '__main__':
    app.run(debug=True)
