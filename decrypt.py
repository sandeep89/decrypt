from flask import request, Flask, render_template, send_from_directory
from flask_restful import reqparse, Resource, Api
import json
from core.aes_encyption import decrypt

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

@app.route('/fonts/<path:path>')
def send_fonts(path):
    return send_from_directory('static/fonts', path)

@app.route('/decrypt/text', methods=['GET', 'POST'])
def decrypt_text():
	if request.method == 'POST':
		value = decrypt('V3/bLnDsAFDGmKYqeAsD8ScvhvxZ7/FudPa5Psytl7Y=')
		return render_template('text_decrypt.html', value=value)
	else:
		return render_template('text_decrypt.html')

if __name__ == '__main__':
    app.run(debug=True)
