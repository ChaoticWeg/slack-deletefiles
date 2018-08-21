from slackclient import SlackClient
from .delete_thread import DeleteThread
from os import environ
from datetime import datetime
import queue

from .exceptions import TokenMissingError, ResponseNotOkError, MalformedResponseError, NoClientError

def get_files(ts_to=datetime.now().timestamp()):
    token = environ.get('SLACK_TOKEN')
    if token is None:
        raise TokenMissingError()
    
    client = SlackClient(token)

    response = client.api_call("files.list", ts_to=ts_to)

    if not 'ok' in response:
        raise MalformedResponseError("no confirmation")
    
    if not response['ok']:
        if not 'error' in response:
            raise MalformedResponseError("not OK but no error given")
        else:
            raise ResponseNotOkError(response['error'])
    
    if not 'files' in response:
        raise MalformedResponseError("no files")
    
    return [f['id'] for f in response['files']]

def delete_files(files):
    token = environ.get('SLACK_TOKEN')
    if token is None:
        raise TokenMissingError()
    
    client = SlackClient(token)

    # "bad bucket" - files that failed to delete
    bad_bucket = queue.Queue()
    
    # multi-thread to compensate for I/O
    threads = []
    for id in files:
        threads.append(DeleteThread(client, bad_bucket))
    
    # start each thread
    for thread in threads:
        thread.start()
    
    # wait for each thread
    for thread in threads:
        thread.join()

    # get all the bad files
    bad_ids = []
    while True:
        try:
            bad_id = bucket.get(block=False)
        except queue.Empty:
            return bad_ids
        else:
            bad_ids.append(bad_id)
