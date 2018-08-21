from .exceptions import NoClientError, MalformedResponseError, ResponseNotOkError
import threading

class DeleteThread(threading.Thread):

    def __init__(self, client, id, bad_bucket):
        threading.Thread.__init__(self)
        self.client = client
        self.id = id
        self.bad_bucket = bad_bucket
    
    def run(self):
        id = self.id

        try:

            if self.client is None or not self.client:
                raise NoClientError(id)

            response = self.client.api_call("files.delete", file=id)

            if not 'ok' in response:
                raise MalformedResponseError("no confirmation")
            
            if not response['ok']:
                if not 'error' in response:
                    raise MalformedResponseError("not OK but no error given")
                else:
                    raise ResponseNotOkError(response['error'])
            
        except NoClientError:
            pass
        
        except Exception:
            # if an exception is raised, put this id in the "bad bucket"
            self.bad_bucket.put(id)
