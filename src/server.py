
from flask import Flask, request, abort
import json

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
def calculate():
    contributions = store.restore()
    return json.dumps(contributions)
