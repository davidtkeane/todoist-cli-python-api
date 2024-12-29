# Install instructions for todoist_api_test.py

## Macbook Air M1 and Macbook Pro M3

## Asus Rog Strix 2

Works on:

1. Windows PowerShell
2. Macbook Terminal - Python Version 3.11.8

### Modules to install

1. run the command $ pip install -r requirements.txt
2. This will install the below modules for install_todoist.py, todoist_api_test.py and todoist.py

- todoist
- todoist_api_python
- python-dotenv
- tabulate

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

Making the Script Executable and Adding it to the PATH

Here's how to make your script easily runnable from the terminal:

Steps (macOS/Linux):

Add Shebang:

At the very top of your todoist.py file, add the following shebang line:

Bash

#!/usr/bin/env python3
This tells the system to use the Python 3 interpreter to run the script.

Make the Script Executable:

Use the chmod command in your terminal:

Bash

chmod +x /path/to/your/todoist.py
Replace /path/to/your/todoist.py with the actual path to your script.

Move to /usr/local/bin/ (Recommended):

This directory is typically already in your PATH. Move your script there:

Bash

sudo mv /path/to/your/todoist.py /usr/local/bin/todoist
You are using todoist as the executable name for your script.
If you have a todoist folder, you can move it to /usr/local/bin like so:

Bash

sudo mv /path/to/your/todoist /usr/local/bin/
Then create a symbolic link:

Bash

sudo ln -s /usr/local/bin/todoist/todoist.py /usr/local/bin/todoist
Steps (Windows):

Add .py Extension to PATHEXT:

Search for "environment variables" in the Start Menu and select "Edit the system environment variables."
Click "Environment Variables...".
Under "System variables," select PATHEXT and click "Edit...".
Add ; .PY to the end of the variable value (make sure there's a semicolon separating it from the previous entry).
Click "OK" on all open windows.
Move Script to a Directory in PATH:

You can move your todoist.py script to a directory that's already in your PATH environment variable (e.g., C:\Windows\System32, but this is generally not recommended for user scripts).
Better: Create a new directory for your scripts (e.g., C:\Users\YourUserName\bin or C:\scripts) and add that directory to your PATH environment variable (similar to how you edited PATHEXT).
4. Running the Script

After completing the steps above:

macOS/Linux:

Open your terminal and simply type:

Bash

todoist
Windows:

Open a command prompt or PowerShell and type:

Bash

todoist.py
Or, if you followed the PATHEXT method, you can just type:

Bash

todoist
Best Way Forward

OS Detection: Use the platform module as outlined above.
API Key:
Development: Use a .env file for convenience.
Production: Set the TODOIST_API_KEY environment variable directly in your system's environment.
Executable:
macOS/Linux: Use shebang, chmod +x, and move to /usr/local/bin/.
Windows: Add .PY to PATHEXT and move the script to a directory in your PATH.
