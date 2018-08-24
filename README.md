# DeleteFiles

Delete files older than 30 days from your Slack team. Purges public and private files to free up space under the free team storage limit imposed by Slack.

## Requirements

- [Python 3](https://www.python.org) and [pip](https://pypi.org/project/pip)
- [Pipenv](https://pipenv.readthedocs.io/en/latest/)

**Note**: a `run.sh` file is provided - this is my own personal script, provided as an example. If you try to run it, there will likely be errors: I am using [my own script](https://chaoticweg.cc/discord.sh) to post logs to a Discord webhook. If you manage to successfully configure and run it, timestamped logs will be posted in `./logs/`.

## How to Use

1. Set up DeleteFiles on your machine
  - `$ git clone https://github.com/ChaoticWeg/slack-deletefiles && cd slack-deletefiles`
  - `$ pipenv install`
2. Authorize DeleteFiles for your team (see below)
3. `$ python3 -m pipenv run python main.py`


## Authorizing DeleteFiles for your Team

**Note: you must have JavaScript enabled to fetch your OAuth token! Read more under #3 below.**

1. Authorize DeleteFiles with the required permissions for your Slack team. [Click here](https://chaoticweg.cc/slack-deletefiles/install) to do so.
2. You will be redirected to a site that will give you your token - **save this token!**
  - You must have JavaScript enabled to fetch the token. This is because the temporary one-time-use code is sent to my API, which fetches your token from Slack using `deletefiles`' client ID and secret token.
3. Copy your OAuth token to a file called `.env` inside the folder created by `git clone` during the install process

## Required Permissions

- `files:read`
  - Required to get a list of files from your Slack team
- `files:write:user`
  - Required to delete public and private files
