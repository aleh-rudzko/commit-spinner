import json
import settings
from datetime import datetime, timedelta
from github_client import Client
from collections import defaultdict


def calculate_contributions():
    github = Client(settings.OWNER_NAME, settings.REPO_NAME)

    commits = github.get_current_commits()

    contributions = defaultdict(int)
    for commit in commits:
        print(commit)
        author_name = commit['commit']['author']['name']
        contributions[author_name] += 1

    for name, contrib in contributions.items():
        contributions[name] = float(contrib) / len(commits)

    return contributions


class Store(object):
    def __init__(self, path, *args, **kwargs):
        self.path = path


class JsonFileStore(Store):
    def save(self, data):
        with open(self.path, 'w') as outfile:
            json.dump(data, outfile)

    def restore(self):
        with open(self.path, 'r') as outfile:
            return json.load(outfile)


class ClickCounter(object):
    TARGET_SPEED = 300

    def __init__(self):
        self.clicks = []

    def get_current_speed(self):
        delta = datetime.now() - timedelta(seconds=5)
        last_clicks = sum([click['count'] for click in self.clicks if click['timestamp'] > delta])

        return min(last_clicks / 300, 1)

    def add_click_count(self, count):
        self.clicks.append({'timestamp': datetime.now(), 'count': count})
