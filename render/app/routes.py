from flask import render_template, jsonify, request
from app import app

from make_weird import process

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/process_input', methods=['GET', 'POST'])
def process_input():
    return jsonify({'text':process(request.form['text'])})
