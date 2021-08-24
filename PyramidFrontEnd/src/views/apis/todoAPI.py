from pyramid.httpexceptions import HTTPFound
from pyramid.response import Response
from pyramid.view import view_config, view_defaults
import requests
API_URL = "http://localhost:5000"
API_VERSION = "v1"

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
                r = requests.post(
                    API_URL + "/{}/add-item".format(API_VERSION),
                    data={
                        "name": self.request.json_body.get('name')
                    }
                
                )
        
            return {"create_todo": {
                "name": self.request.json_body.get('name')}}
        except Exception as e:
            print(e)

    @view_config(request_method="DELETE", renderer="json")
    def delete(self):
        pass
        # sp = self.request.tm.savepoint()
        # if self.request.json_body:
        #     try:
        #         query = self.request.dbsession.query(models.ToDoModel).filter(
        #             models.ToDoModel.id == self.request.json_body
        #         )
        #         target_todo = query.first()
        #         self.request.dbsession.delete(target_todo)
        #         self.request.dbsession.flush()
        #     except IntegrityError:
        #         sp.rollback()
        # else:
        #     return {"result": "削除失敗"}
        # return {"delete_todo": Todo().dump(target_todo)}
