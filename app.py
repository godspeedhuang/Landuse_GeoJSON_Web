# -*- coding: UTF-8 -*-
from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import send_file

app = Flask(__name__, static_folder='static', static_url_path='/')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/search')
def download_file():
    district_code = request.args.get('district', '')
    return redirect(district_code+'.json')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=False)
