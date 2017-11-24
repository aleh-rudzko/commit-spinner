import os

REPO_NAME = 'dummy-project'
OWNER_NAME = 'aleh-rudzko'

PATH_TO_DATA_FILE = os.environ.get('SPEEDS_FILE', 'data.json')

WEBHOOK_SECRET = os.environ.get('WEBHOOK_SECRET')
print(WEBHOOK_SECRET)
print('settings')
