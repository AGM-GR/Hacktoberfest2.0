import request
import json

class getJsonData(object):
    def __init__(self, data):
        self.__dict__ = json.loads(data)


def get_url(uri):
    r = requests.post('localhost:5000/'+uri)

    data = getJsonData(r)
    print(r.user)
    print(r.array_test)

get_url(protected)
