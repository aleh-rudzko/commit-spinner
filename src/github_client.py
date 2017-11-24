from datetime import datetime
import requests


class Client(object):
    base_api_url = 'https://api.github.com'

    def __init__(self, owner, repo):
        self.owner = owner
        self.repo = repo

    def get_current_commits(self):
        url = '{}/repos/{}/{}/commits'.format(
            self.base_api_url, self.owner, self.repo)
        params = {
            'since': datetime.now().replace(hour=0, minute=0, second=0).isoformat()
        }
        response = requests.get(url, params=params)
        return response.json()
