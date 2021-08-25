def includeme(config):
    config.add_static_view("static", "static", cache_max_age=3600)
    config.add_route("todo_index", "/")
    config.add_route("api_todo", "/api/todo")
    config.add_route("api_todo_search", "/api/todo/{name}")



