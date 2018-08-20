from slackclient import SlackClient

class Client:
    """ Slack client, powered by SlackClient """

    def __init__(self, token):
        self.token  = token
        self.client = SlackClient(token)
    
    def get_files(self):
        pass
    
    def delete_file(self, file_id):
        pass
