from pyramid.httpexceptions import HTTPFound
from pyramid.response import Response
from pyramid.view import view_config, view_defaults


@view_defaults(route_name="todo_index")
class ToDoIndexViews(object):
    def __init__(self, request):
        self.request = request
        self.view_name = "ToDoViews"

    @view_config(request_method="GET", renderer="../templates/todo/index.jinja2")
    def get(self):
        return {}
