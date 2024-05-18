from todoist_api_python.api import TodoistAPI

api = TodoistAPI("5f9117b0202d3506cda51819abe8eeb5d006aa3c")

try:
    projects = api.get_projects()
    print(projects)
except Exception as error:
    print(error)