from flask import Flask
from flask import request
import json

from service import calculate_contributions, upload_to_file

app = Flask(__name__)


@app.route('/webhook', methods=['POST'])
def webhook():
    contributions = calculate_contributions()
    upload_to_file(contributions)
    return "Ok."


@app.route('/calculate')
def calculate():
    contributions = calculate_contributions()
    upload_to_file(contributions)
    return json.dumps(contributions)


