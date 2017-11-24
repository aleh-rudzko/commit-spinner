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


def upload_to_file(data):
    with open(settings.PATH_TO_DATA_FILE, 'w') as outfile:
        json.dump(data, outfile)
    print('uploaded to file.')
