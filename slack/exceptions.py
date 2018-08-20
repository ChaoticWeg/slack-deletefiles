class DeleteFilesError(Exception):
    """ Base exception class """
    pass

class TokenMissingError(DeleteFilesError):
    """ Raised when no token is provided in the environment (or in .env). """
    def __init__(self):
        self.message = "No Slack OAuth token provided. Provide a .env file in the same directory as main.py with SLACK_TOKEN=<token>."

class ResponseNotOkError(DeleteFilesError):
    """ Raised when Slack responds with an error. """
    def __init__(self, reason):
        self.message = "Slack responded with an error: %s" % reason
        self.reason = reason

class MalformedResponseError(DeleteFilesError):
    """ Raised when a response from Slack is malformed. """
    def __init__(self, reason):
        self.message = "Received a malformed response from Slack: %s" % reason
        self.reason = reason

class NoClientError(DeleteFilesError):
    """ Raised when a worker receives a null or bad SlackClient. """
    def __init__(self, id):
        self.message = "Worker for file %s received a null or bad SlackClient" % id
        self.client_id = id
