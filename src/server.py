
from flask import Flask, request, abort
from flask import jsonify

import settings
from service import calculate_contributions, JsonFileStore
from github_client import InvalidSignature, verify_github_request

app = Flask(__name__, static_url_path='/frontend')

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


@app.route('/hello')
def root():
    return app.send_static_file('index.html')
