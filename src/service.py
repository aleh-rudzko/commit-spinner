import json
import settings
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
