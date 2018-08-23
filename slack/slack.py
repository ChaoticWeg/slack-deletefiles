from slackclient import SlackClient
from .delete_thread import DeleteThread
from os import environ
from datetime import datetime
import queue

from .exceptions import TokenMissingError, ResponseNotOkError, MalformedResponseError, NoClientError

def validate_files_response(response):
    if not 'ok' in response:
        raise MalformedResponseError("no confirmation")
    
    if not response['ok']:
        if not 'error' in response:
            raise MalformedResponseError("not OK but no error given")
        else:
            raise ResponseNotOkError(response['error'])
    
    if not 'files' in response:
        raise MalformedResponseError("no files")

def get_page(page, client, ts_to):
    response = client.api_call("files.list", ts_to=ts_to, page=page)
    validate_files_response(response)
    return [f['id'] for f in response['files']]

def get_files(ts_to=datetime.now().timestamp()):
    token = environ.get('SLACK_TOKEN')
    if token is None:
        raise TokenMissingError()
    
    client = SlackClient(token)

    first_res = client.api_call("files.list", ts_to=ts_to)
    validate_files_response(first_res)
    
    files = [f['id'] for f in first_res['files']]
    num_pages = int(first_res['paging']['pages'])
    for this_page_num in range(1, num_pages):
        this_page = get_page(this_page_num, client, ts_to)
        files.extend(this_page)

    return files

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
        threads.append(DeleteThread(client, id, bad_bucket))
    
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
            bad_id = bad_bucket.get(block=False)
        except queue.Empty:
            return bad_ids
        else:
            bad_ids.append(bad_id)
