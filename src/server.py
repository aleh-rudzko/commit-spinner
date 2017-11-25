
from flask import Flask, request, abort
from flask import jsonify
from flask import send_from_directory

import settings
from service import calculate_contributions, JsonFileStore
from github_client import InvalidSignature, verify_github_request

app = Flask(__name__)

store = JsonFileStore(settings.PATH_TO_DATA_FILE)


@app.route('/webhook', methods=['POST'])
def webhook():
    # try:
    #     verify_github_request(request)
    # except InvalidSignature:
    #     abort(403)

    contributions = calculate_contributions()
    store.save(contributions)
    return "Ok."


@app.route('/speeds')
def speeds():
    contributions = store.restore()
    return jsonify(contributions)


@app.route('/')
def root():
    return app.send_static_file('index.html')


@app.route('/static/<path:path>')
def send_js(path):
    return send_from_directory('static', path)
