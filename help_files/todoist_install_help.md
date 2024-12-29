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

Okay, let's break down how to enhance your script to be OS-aware, manage your Todoist API key securely, and make it executable from the terminal.

**1. OS Detection and Conditional Execution**

We'll use the `platform` module to detect the operating system and then execute OS-specific code blocks.

```python
import platform
import os
import sys
from todoist_api_python.api import TodoistAPI
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

def get_todoist_tasks(api):
    """Fetches and prints Todoist tasks."""
    try:
        tasks = api.get_tasks()
        print(f"{Fore.CYAN}Your Todoist tasks:")
        for task in tasks:
            print(f"{Style.BRIGHT}- {task.content}")
    except Exception as e:
        print(f"{Fore.RED}Error fetching tasks: {e}")
        sys.exit(1)

def main():
    """Main function to handle OS detection and task fetching."""
    api = TodoistAPI("YOUR_TODOIST_API_KEY") # API key handling
    current_os = platform.system()

    if current_os == "Windows":
        print(f"{Fore.GREEN}Detected OS: Windows")
        # Windows-specific code here (if needed)

    elif current_os == "Darwin":  # Darwin is the system name for macOS
        print(f"{Fore.GREEN}Detected OS: macOS")
        # macOS-specific code here (if needed)

    elif current_os == "Linux":
        print(f"{Fore.GREEN}Detected OS: Linux")
        # Linux-specific code here (if needed)

    else:
        print(f"{Fore.YELLOW}Unsupported OS: {current_os}")
        sys.exit(1)

    get_todoist_tasks(api)

if __name__ == "__main__":
    main()
```

**2. Todoist API Key and .env File Management**

Here's how to manage your API key:

*   **Using .env (Recommended for Development):**
    1.  **Create a .env file:** In the same directory as your `todoist.py` script (or a parent directory), create a file named `.env`.
    2.  **Add your API key:** Inside `.env`, add the following line:
        ```
        TODOIST_API_KEY=YOUR_ACTUAL_API_KEY
        ```
        Replace `YOUR_ACTUAL_API_KEY` with your real Todoist API key.
    3.  **Install dotenv package:**
        ```bash
        pip install python-dotenv
        ```
    4.  **Use `python-dotenv` in your script:**
        ```python
        import os
        from dotenv import load_dotenv

        # Load .env file
        load_dotenv()

        # Get API key from environment variable
        api_key = os.getenv("TODOIST_API_KEY")

        # Check if API key is set
        if api_key:
            api = TodoistAPI(api_key)
        else:
            print("Error: TODOIST_API_KEY environment variable not set.")
            exit()
        ```

*   **Directly in the Script (Not Recommended):**
    *   You've already done this by replacing the `load_dotenv()` part with `api = TodoistAPI("YOUR_TODOIST_API_KEY")`. This is okay for quick testing but not secure for production or sharing your code.

*   **Using Environment Variables Directly (Recommended for Production):**
    1.  **Set the environment variable:**
        *   **Windows:**
            ```bash
            setx TODOIST_API_KEY "YOUR_ACTUAL_API_KEY"
            ```
        *   **macOS/Linux:**
            ```bash
            export TODOIST_API_KEY="YOUR_ACTUAL_API_KEY"
            ```
            (You might want to add this to your `~/.bashrc`, `~/.zshrc`, or equivalent shell configuration file to make it persistent across sessions).
    2.  **Use `os.getenv()` in your script:** You can use the code snippet from the `.env` method, but you won't need to install or use `python-dotenv`.

**3. Making the Script Executable and Adding it to the PATH**

Here's how to make your script easily runnable from the terminal:

**Steps (macOS/Linux):**

1.  **Add Shebang:**
    *   At the very top of your `todoist.py` file, add the following shebang line:

        ```bash
        #!/usr/bin/env python3
        ```

        This tells the system to use the Python 3 interpreter to run the script.

2.  **Make the Script Executable:**
    *   Use the `chmod` command in your terminal:

        ```bash
        chmod +x /path/to/your/todoist.py
        ```

        Replace `/path/to/your/todoist.py` with the actual path to your script.

3.  **Move to `/usr/local/bin/` (Recommended):**
    *   This directory is typically already in your `PATH`. Move your script there:

        ```bash
        sudo mv /path/to/your/todoist.py /usr/local/bin/todoist
        ```
        You are using `todoist` as the executable name for your script.
        If you have a `todoist` folder, you can move it to `/usr/local/bin` like so:
        ```bash
        sudo mv /path/to/your/todoist /usr/local/bin/
        ```
        Then create a symbolic link:
        ```bash
        sudo ln -s /usr/local/bin/todoist/todoist.py /usr/local/bin/todoist
        ```

**Steps (Windows):**

1.  **Add .py Extension to PATHEXT:**
    1.  Search for "environment variables" in the Start Menu and select "Edit the system environment variables."
    2.  Click "Environment Variables...".
    3.  Under "System variables," select `PATHEXT` and click "Edit...".
    4.  Add `; .PY` to the end of the variable value (make sure there's a semicolon separating it from the previous entry).
    5.  Click "OK" on all open windows.

2.  **Move Script to a Directory in PATH:**
    *   You can move your `todoist.py` script to a directory that's already in your `PATH` environment variable (e.g., `C:\Windows\System32`, but this is generally not recommended for user scripts).
    *   **Better:** Create a new directory for your scripts (e.g., `C:\Users\YourUserName\bin` or `C:\scripts`) and add that directory to your `PATH` environment variable (similar to how you edited `PATHEXT`).

**4. Running the Script**

After completing the steps above:

*   **macOS/Linux:**
    *   Open your terminal and simply type:

        ```bash
        todoist
        ```

*   **Windows:**
    *   Open a command prompt or PowerShell and type:

        ```bash
        todoist.py
        ```

        Or, if you followed the `PATHEXT` method, you can just type:

        ```bash
        todoist
        ```

**Best Way Forward**

1.  **OS Detection:** Use the `platform` module as outlined above.
2.  **API Key:**
    *   **Development:** Use a `.env` file for convenience.
    *   **Production:** Set the `TODOIST_API_KEY` environment variable directly in your system's environment.
3.  **Executable:**
    *   **macOS/Linux:** Use shebang, `chmod +x`, and move to `/usr/local/bin/`.
    *   **Windows:** Add `.PY` to `PATHEXT` and move the script to a directory in your `PATH`.

This detailed guide will help you create a robust and user-friendly Todoist script! Let me know if you have more questions.
