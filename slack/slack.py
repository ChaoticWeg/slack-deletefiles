from slackclient import SlackClient
from threading import Thread
from os import environ

from .exceptions import TokenMissingError, ResponseNotOkError, MalformedResponseError, NoClientError

def get_files():
    token = environ.get('SLACK_TOKEN')
    if token is None:
        raise TokenMissingError()
    
    client = SlackClient(token)

    response = client.api_call("files.list")

    if not 'ok' in response:
        raise MalformedResponseError("no confirmation")
    
    if not response['ok']:
        if not 'error' in response:
            raise MalformedResponseError("not OK but no error given")
        else
            raise ResponseNotOkError(response['error'])
    
    if not 'files' in response:
        raise MalformedResponseError("no files")
    
    return [f['id'] for f in response['files']]

def delete_files(files):
    token = environ.get('SLACK_TOKEN')
    if token is None:
        raise TokenMissingError()
    threads = []
    for id in files:
        threads.append(Thread(target=deletion_worker, args=(id, client)))
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    
def deletion_worker(id, client):
    if client is None or not client:
        raise NoClientError(id)

    print("deleting file: %s" % id)
    response = client.api_call("files.delete", file=id)

    if not 'ok' in response:
        raise MalformedResponseError("no confirmation")
    
    if not response['ok']:
        if not 'error' in response:
            raise MalformedResponseError("not OK but no error given")
        else
            raise ResponseNotOkError(response['error'])
    
    print("successfully deleted file: %s" % id)
