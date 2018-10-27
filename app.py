from flask import Flask
# encoding:utf-8
from flask import request
from flask import render_template
from flask import redirect
from flask import session
from flask import url_for
from modules import *
from modules import *
from plugins.whatweb import Whatweb
import json
from flask import jsonify

app = Flask(__name__)


@app.route('/')
def fast():
    return render_template('whatweb.html')


@app.route('/api',methods=['GET'])
def api():
    query = request.args.get('query', '')
    web_api = Whatweb()
    return jsonify(web_api.api(query))

if __name__ == '__main__':
    app.run()
