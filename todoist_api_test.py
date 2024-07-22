from todoist_api_python.api import TodoistAPI

api = TodoistAPI("52dfdsfs83jnjnjj344426646346jbkjbjk")

try:
    projects = api.get_projects()
    print(projects)
except Exception as error:
    print(error)
