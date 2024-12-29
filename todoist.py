# renamed to todoist.py from main.py

from todoist_api_python.api import TodoistAPI
from dotenv import load_dotenv
import os
import webbrowser

# Load the .env file
load_dotenv()

# Get the API key
api_key = os.getenv("TODOIST_API_KEY")

# Use the API key
api = TodoistAPI(api_key)

init(autoreset=True)  # Initialize colorama for colored terminal text

def print_projects(projects):
    for project in projects:
        print(f"{Fore.CYAN}Project ID: {project.id}, Name: {project.name}")

def print_tasks(tasks):
    for task in tasks:
        print(f"{Fore.YELLOW}Task ID: {task.id}, Content: {task.content}")

def get_user_input(prompt):
    try:
        return input(prompt)
    except KeyboardInterrupt:
        print(f"\n{Fore.RED}User interrupted with Ctrl+C. Exiting back to main menu.")
        return "back"

def print_banner():
    print(f"\n{Fore.GREEN}{'='*30}")
    print("Welcome to the Todoist CLI!")
    print(f"{Fore.GREEN}{'='*30}\n")

def print_goodbye():
    print(f"\n{Fore.GREEN}{'='*30}")
    print(f"Thank you for using the {Fore.YELLOW}Todoist CLI{Fore.RESET}. {Fore.GREEN}Goodbye!")
    print(f"{Fore.GREEN}{'='*30}\n")

def main():
    print_banner()
    while True:
        print(f"\n{Fore.GREEN}{'='*30}")
        print(f"{Fore.CYAN} 1. {Fore.RESET}List projects")
        print(f"{Fore.CYAN} 2. {Fore.RESET}Add project")
        print(f"{Fore.CYAN} 3. {Fore.RESET}Delete project")
        print(f"{Fore.CYAN} 4. {Fore.RESET}List tasks")
        print(f"{Fore.CYAN} 5. {Fore.RESET}Add task")
        print(f"{Fore.CYAN} 6. {Fore.RESET}Update task")
        print(f"{Fore.CYAN} 7. {Fore.RESET}Close task")
        print(f"{Fore.CYAN} 8. {Fore.RESET}Reopen task")
        print(f"{Fore.CYAN} 9. {Fore.RESET}Delete task")
        print(f"{Fore.CYAN}10. {Fore.RESET}List comments")
        print(f"{Fore.CYAN}11. {Fore.RESET}Add comment")
        print(f"{Fore.CYAN}12. {Fore.RESET}Update comment")
        print(f"{Fore.CYAN}13. {Fore.RESET}Delete comment")
        print(f"{Fore.CYAN}14. {Fore.RESET}View today's tasks online")
        print(f"{Fore.CYAN}15. {Fore.RESET}View projects online")
        print(f"{Fore.CYAN} 0. {Fore.RESET}Exit")
        print(f"{Fore.GREEN}{'='*30}\n")
        choice = get_user_input("Choose an option (or type 'back' to return to menu): ")

        if choice.lower() == 'exit':
            print_goodbye()
            sys.exit(0)
        elif choice.lower() == 'back':
            continue

        if choice == "1":
            projects = api.get_projects()
            print_projects(projects)
        elif choice == "2":
            project_name = get_user_input("Enter project name (or 'back' to return): ")
            if project_name.lower() != 'back':
                project = api.add_project(name=project_name)
                print(f"{Fore.GREEN}Added project {project.name} with ID {project.id}")
        elif choice == "3":
            project_id = get_user_input("Enter project ID to delete (or 'back' to return): ")
            if project_id.lower() != 'back':
                is_success = api.delete_project(project_id=project_id)
                print(f"Deleted project {project_id}: {is_success}")
        elif choice == "4":
            tasks = api.get_tasks()
            print_tasks(tasks)
        elif choice == "5":
            content = get_user_input("Enter task content (or 'back' to return): ")
            if content.lower() != 'back':
                due_string = get_user_input("Enter due date (or 'back' to return): ")
                if due_string.lower() != 'back':
                    priority = get_user_input("Enter priority (1-4) (or 'back' to return): ")
                    if priority.lower() != 'back':
                        task = api.add_task(content=content, due_string=due_string, due_lang="en", priority=int(priority))
                        print(f"{Fore.GREEN}Added task {task.content} with ID {task.id}")
        elif choice in ["6", "7", "8", "9"]:
            tasks = api.get_tasks()
            print_tasks(tasks)
            task_id = get_user_input("Enter task ID (or 'back' to return): ")
            if task_id.lower() != 'back':
                if choice == "6":
                    content = get_user_input("Enter new content (or 'back' to return): ")
                    if content.lower() != 'back':
                        is_success = api.update_task(task_id=task_id, content=content)
                        print(f"Updated task {task_id}: {is_success}")
                elif choice == "7":
                    is_success = api.close_task(task_id=task_id)
                    print(f"Closed task {task_id}: {is_success}")
                elif choice == "8":
                    is_success = api.reopen_task(task_id=task_id)
                    print(f"Reopened task {task_id}: {is_success}")
                elif choice == "9":
                    is_success = api.delete_task(task_id=task_id)
                    print(f"Deleted task {task_id}: {is_success}")
        elif choice in ["10", "11", "12", "13"]:
            tasks = api.get_tasks()
            print_tasks(tasks)
            task_id = get_user_input("Enter task ID (or 'back' to return): ")
            if task_id.lower() != 'back':
                if choice == "10":
                    comments = api.get_comments(task_id=task_id)
                    if comments:
                        for comment in comments:
                            print(f"{Fore.BLUE}Comment ID: {comment.id}, Content: {comment.content}")
                    else:
                        print("No comments found for this task.")
                elif choice == "11":
                    content = get_user_input("Enter comment content (or 'back' to return): ")
                    if content.lower() != 'back':
                        comment = api.add_comment(content=content, task_id=task_id)
                        print(f"Added comment {comment.content} with ID {comment.id} to task {task_id}")
                elif choice == "12":
                    comment_id = get_user_input("Enter comment ID to update (or 'back' to return): ")
                    if comment_id.lower() != 'back':
                        content = get_user_input("Enter new content (or 'back' to return): ")
                        if content.lower() != 'back':
                            is_success = api.update_comment(comment_id=comment_id, content=content)
                            print(f"Updated comment {comment_id}: {is_success}")
                elif choice == "13":
                    comment_id = get_user_input("Enter comment ID to delete (or 'back' to return): ")
                    if comment_id.lower() != 'back':
                        is_success = api.delete_comment(comment_id=comment_id)
                        print(f"Deleted comment {comment_id}: {is_success}")
        elif choice == "14":
            webbrowser.open("https://app.todoist.com/app/today")
        elif choice == "15":
            webbrowser.open("https://app.todoist.com/app/projects/active")
        elif choice == "0":
            print_goodbye()
            break
        else:
            print(f"{Fore.RED}Invalid choice. Please choose a number from 1 to 16 or type 'back'/'exit'.")

if __name__ == "__main__":
    main()