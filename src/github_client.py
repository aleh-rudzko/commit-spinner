import hmac
from datetime import datetime, timedelta
from sys import hexversion

import requests
import settings


# Augmented Reality
class Client(object):
    base_api_url = 'https://api.github.com'

    def __init__(self, owner, repo):
        self.owner = owner
        self.repo = repo

    def get_current_commits(self):
        url = '{}/repos/{}/{}/commits'.format(
            self.base_api_url, self.owner, self.repo)
        params = {
            'since': (datetime.now() - timedelta(hours=1)).isoformat()
        }
        response = requests.get(url, params=params)
        return response.json()


def verify_github_request(request):
    header_signature = request.headers.get('X-Hub-Signature')
    if not header_signature:
        raise InvalidSignature

    sha_name, signature = header_signature.split('=')
    if sha_name != 'sha1':
        raise InvalidSignature

    # HMAC requires the key to be bytes, but data is string
    mac = hmac.new(bytes(settings.WEBHOOK_SECRET), msg=request.data, digestmod='sha1')

    # Python prior to 2.7.7 does not have hmac.compare_digest
    if hexversion >= 0x020707F0:
        if not hmac.compare_digest(str(mac.hexdigest()), str(signature)):
            raise InvalidSignature
    else:
        # What compare_digest provides is protection against timing
        # attacks; we can live without this protection for a web-based
        # application
        if not str(mac.hexdigest()) == str(signature):
            raise InvalidSignature


class InvalidSignature(Exception):
    pass
