from flask import Flask, request, abort
import json

from service import calculate_contributions, upload_to_file
from github_client import InvalidSignature, verify_github_request

app = Flask(__name__)


@app.route('/webhook', methods=['POST'])
def webhook():
    # try:
    #     verify_github_request(request)
    # except InvalidSignature:
    #     abort(403)

    contributions = calculate_contributions()
    upload_to_file(contributions)
    return "Ok."


@app.route('/calculate')
def calculate():
    contributions = calculate_contributions()
    return json.dumps(contributions)
