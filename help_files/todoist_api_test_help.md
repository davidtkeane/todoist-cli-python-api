# Install instructions for todoist_api_test.py

## Macbook Air M1

## Asus Rog Strix 2

Works on:

1. Windows PowerShell
2. Macbook Terminal

### Modules to install

1. run the command $ pip install -r requirements.txt
2. This will install the below modules for install_todoist.py, todoist_api_test.py and todoist.py

- todoist
- todoist_api_python
- python-dotenv

## Run the todoist_api_test.py

$ python todoist_api_test.py

C:\ python todoist_api_test.py

### Testing Todoist API Key.

1. You can test with curl or,
2. Use the python file.

### 1. Curl Your API key to test connection.

1. Change 0123456789abcdef0123456789 api key to the one that you got from the Todoist website.
2. Then copy all the text below starting with curl -X GET \ and paste it into the terminal and press enter.

```
curl -X GET \
  https://api.todoist.com/rest/v2/projects \
  -H "Authorization: Bearer 0123456789abcdef0123456789"
```

3. You should get a return in the terminal similar to this. If this comes back then you have connected to Todoist from your terminal.

```
[
    {
        "id": "220474322",
        "name": "Inbox",
        "comment_count": 10,
        "order": 0,
        "color": "grey",
        "is_shared": false,
        "is_favorite": false,
        "is_inbox_project": true,
        "is_team_inbox": false,
        "view_style": "list",
        "url": "https://todoist.com/showProject?id=220474322",
        "parent_id": null,
    }
]
```

### 2. Python script to test APi Key.

1. Create a python file and name it todoist_test_api.py or use the same file I have in this folder.
2. Add your api key
3. run the command python todoist_test_api.py

```
from todoist_api_python.api import TodoistAPI

api = TodoistAPI("0123456789abcdef0123456789")

try:
    projects = api.get_projects()
    print(projects)
except Exception as error:
    print(error)
```

4. If sucessful then you should get a reply in the terminal like below to know it works.

```
[
    Project(
        id: "220474322",
        name: "Inbox",
        comment_count: 10,
        order: 0,
        color: "grey",
        is_shared: False,
        is_favorite: False,
        is_inbox_project: True,
        is_team_inbox: False,
        view_style: "list",
        url: "https://todoist.com/showProject?id=220474322",
        parent_id: None,
    )
]
```
