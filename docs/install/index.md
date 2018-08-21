---
layout: page
title: Install
permalink: /install
---

<style type="text/css">
    div.highlight, code {
        margin: 1em;
    }
</style>

**Note: these instructions are not valid yet.** I am still working on a website where you can fetch your token given to you by Slack once you install. Hang tight.

1. Clone or fork the [git repo][git]:
    - `$ git clone https://github.com/ChaoticWeg/slack-deletefiles.git`
2. [Click here][clickme] to install `deletefiles` to your Slack team
3. Create a file in the new repo directory called `.env` with the following contents:
    ```
        SLACK_TOKEN=<paste your token>
    ```
4. `$ ./run.sh`

[git]: https://github.com/ChaoticWeg/slack-deletefiles
[clickme]: https://slack.com/oauth/authorize?client_id=81954967892.419510101061&scope=files:read,files:write:user
