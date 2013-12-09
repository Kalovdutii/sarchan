#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask
from flask import render_template
from flask import request
from werkzeug import secure_filename
from pytooshop import pytooshop
import os

UPLOAD_FOLDER = 'static/tmp'
ALLOWED_EXTENSIONS = set(['jpg', 'jpeg'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed(filename):
	return '.' in filename and filename.rsplit('.',1)[1] in ALLOWED_EXTENSIONS

@app.route("/")
def hello():
    return render_template('index.html') 

@app.route("/pytooshop", methods=['POST','GET'])
def pytooshop_view():
	if request.method == 'GET':
		return render_template('pytooshop.html')
	else:
		file = request.files['file']
		if file and allowed(file.filename):
			filename = secure_filename(file.filename)
			fullpath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
			file.save(fullpath)
			pytooshop(fullpath,14)
			return render_template('pytooshop.html',img=filename)

	
if __name__ == "__main__":
    app.run(debug=True)

