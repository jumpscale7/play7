import requests
import json

from JumpScale import j

from mongoengine import *

ENTRY_POINT =""
TOKEN=""

class ModelGogsRepo(j.core.models.getBaseModel()):
    name = StringField(default='')
    description = StringField(default='')
    private = BoolField(default=False)
    readme = StringField(default='Default')
    gitignores=StringField(default='Python')
    auto_init=BoolField(default=True)

def endpoint(resource):
    C='%s/%s' % (ENTRY_POINT, resource)
    if C.find("?")==-1:
        C+='?token=%s'%TOKEN
    else:
        C+='&token=%s'%TOKEN
    return C

def perform_post(resource, data):
    headers = {'Content-Type': 'application/json'}
    return requests.post(endpoint(resource), data, headers=headers)


def perform_delete(resource):
    return requests.delete(endpoint(resource))

def perform_get(resource):
    r = requests.get(endpoint(resource))
    print r.json


curlexample='''
curl -H "Authorization: token b9d3768004daf48b4b6f963ab94ca47515444074" http://192.168.99.100:3001/api/v1/user/repos
curl http://192.168.99.100:3001/api/v1/user/repos?token=b9d3768004daf48b4b6f963ab94ca47515444074
'''

class GOGSClient():

    def __init__(self):
    
        ENTRY_POINT = 'http://192.168.99.100:3001/api/v1/'
        TOKEN="b9d3768004daf48b4b6f963ab94ca47515444074"

    def repos_list(self):
        return perform_get("user/repos")
       


    def repo_create(self,name,description,private):
        model=ModelGogsRepo(name=name,description=description,private=private)
        perform_post("")

        
        people = [
            {
                'firstname': 'John',
                'lastname': 'Doe',
                'role': ['author'],
                'location': {'address': '422 South Gay Street', 'city': 'Auburn'},
                'born': 'Thu, 27 Aug 1970 14:37:13 GMT'
            },
            {
                'firstname': 'Serena',
                'lastname': 'Love',
                'role': ['author'],
                'location': {'address': '363 Brannan St', 'city': 'San Francisco'},
                'born': 'Wed, 25 Feb 1987 17:00:00 GMT'
            },
            {
                'firstname': 'Mark',
                'lastname': 'Green',
                'role': ['copy', 'author'],
                'location': {'address': '4925 Lacross Road', 'city': 'New York'},
                'born': 'Sat, 23 Feb 1985 12:00:00 GMT'
            },
            {
                'firstname': 'Julia',
                'lastname': 'Red',
                'role': ['copy'],
                'location': {'address': '98 Yatch Road', 'city': 'San Francisco'},
                'born': 'Sun, 20 Jul 1980 11:00:00 GMT'
            },
            {
                'firstname': 'Anne',
                'lastname': 'White',
                'role': ['contributor', 'copy'],
                'location': {'address': '32 Joseph Street', 'city': 'Ashfield'},
                'born': 'Fri, 25 Sep 1970 10:00:00 GMT'
            },
        ]

        r = perform_post('people', json.dumps(people))
        print "'people' posted", r.status_code

        valids = []
        if r.status_code == 201:
            response = r.json()
            if response['_status'] == 'OK':
                for person in response['_items']:
                    if person['_status'] == "OK":
                        valids.append(person['_id'])

        return valids


    # def post_works(ids):
    #     works = []
    #     for i in range(28):
    #         works.append(
    #             {
    #                 'title': 'Book Title #%d' % i,
    #                 'description': 'Description #%d' % i,
    #                 'owner': random.choice(ids),
    #             }
    #         )

    #     r = perform_post('works', json.dumps(works))
    #     print "'works' posted", r.status_code




    # def delete():
    #     r = perform_delete('people')
    #     print "'people' deleted", r.status_code
    #     r = perform_delete('works')
    #     print "'works' deleted", r.status_code


cl=GOGSClient
print (cl.list())




