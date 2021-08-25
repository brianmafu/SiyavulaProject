from pyramid.httpexceptions import HTTPFound
from pyramid.response import Response
from pyramid.view import view_config, view_defaults
from .apis.api_settings import API_URL, API_VERSION
import requests


@view_defaults(route_name="todo_index")
class ToDoIndexViews(object):
    def __init__(self, request):
        self.request = request
        self.view_name = "ToDoViews"

    @view_config(request_method="GET", renderer="../templates/todo/index.jinja2")
    def get(self):
        return {}


    # @view_config(route_name="search", request_method="POST", renderer="json")
    # def post(self):
    #     try:
    #         if self.request.json_body:
    #             r = requests.post(
    #                 API_URL + "/{}/search-item".format(API_VERSION),
    #                 data={
    #                     "search_primer": self.request.json_body.get('search_primer')
    #                 }
                
    #             )
        
    #         return {"create_todo": {
    #             "name": self.request.json_body.get('search_primer')}}
    #     except Exception as e:
    #         print(e)

