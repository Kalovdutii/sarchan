#!/usr/bin/env python
# coding: utf-8
from flask import Flask, render_template, request
from werkzeug import secure_filename
from pytooshop import pytooshop
import os
import pyimgur

UPLOAD_FOLDER = 'static/tmp'
ALLOWED_EXTENSIONS = {'jpg', 'jpeg'}
IMGUR_CLIENT_ID = 'cb3261c208340f9'

app = Flask(__name__)
imgur = pyimgur.Imgur(IMGUR_CLIENT_ID)

def allowed(filename):
	return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/')
def hello():
    return render_template('index.html') 

@app.route('/pytooshop', methods=['GET', 'POST'])
def pytooshop_view():
	if request.method == 'GET':
		return render_template('pytooshop.html')
	if request.method == 'POST':
		image = request.files['file']
		cycles = 14 if not request.form['cycles'] else int(request.form['cycles'])
		if image and allowed(image.filename):
			filename = secure_filename(image.filename)
			fullpath = os.path.join(UPLOAD_FOLDER, filename)
			image.save(fullpath)
			pytooshop(fullpath, cycles)
			img = imgur.upload_image(fullpath)
			os.remove(fullpath)
			return render_template('pytooshop.html', img=img.link)

	
if __name__ == '__main__':
    app.run(debug=True)

