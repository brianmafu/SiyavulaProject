from pyramid.httpexceptions import HTTPFound
from pyramid.response import Response
from pyramid.view import view_config, view_defaults
import requests
API_URL = "http://localhost:5000"
API_VERSION = "v1"



def classify_error_messages (error_message): 
  if "Connection refused" in error_message:
      return "Service API is down: {}".format(API_URL)



@view_defaults(route_name="api_todo")
class ToDoAPIViews(object):
    def __init__(self, request):
        self.request = request
        self.view_name = "ToDoAPIViews"

    @view_config(
        request_method="GET", renderer="json",
    )
    def get(self):
        r = requests.get(API_URL + "/{}/all-items".format(API_VERSION))
        todo_list = []
        try:
            todo_list = r.json()['items']
        except Exception as e:
            print(e)
        return {"todo_list":todo_list}

    @view_config(request_method="POST", renderer="json")
    def post(self):
        try:
            if self.request.json_body:
                # validation check
                name = self.request.json_body.get('name')
                if name:
                    if not len(name) >10 or  not len(name) <100:                        
                        return {
                           "create_todo":{"error_message": "Title must be between \
                            10 and 100 Characters"}
                        }
                r = requests.post(
                    API_URL + "/{}/add-item".format(API_VERSION),
                    data={
                        "name": name
                    }
                
                )
            
                return {"create_todo": {
                    "id": self.request.json_body.get('id'),
                    "name": self.request.json_body.get('name')}}
        except Exception as e:
            return {"create_todo": {
               "error_message": classify_error_messages(str(e))}
            }