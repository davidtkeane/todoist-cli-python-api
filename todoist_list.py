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

def print_projects(projects):
    for project in projects:
        print(f"Project ID: {project.id}, Name: {project.name}")

def print_tasks(tasks):
    for task in tasks:
        print(f"Task ID: {task.id}, Content: {task.content}")

def get_user_input(prompt):
    return input(prompt)

def print_banner():
    print("\n" + "="*30)
    print("Welcome to the Todoist CLI!")
    print("="*30 + "\n")

def print_goodbye():
    print("\n" + "="*30)
    print("Thank you for using the Todoist CLI. Goodbye!")
    print("="*30 + "\n")

def main():
    print_banner()
    while True:
        print("\n" + "="*30)
        print("1. List projects")
        print("2. Add project")
        print("3. Delete project")
        print("4. List tasks")
        print("5. Add task")
        print("6. Update task")
        print("7. Close task")
        print("8. Reopen task")
        print("9. Delete task")
        print("10. List comments")
        print("11. Add comment")
        print("12. Update comment")
        print("13. Delete comment")
        print("14. View today's tasks online")
        print("15. View projects online")
        print("16. Exit") 
        print("="*30 + "\n")
        choice = get_user_input("Choose an option: ")

        if choice == "1":
            projects = api.get_projects()
            print_projects(projects)
        elif choice == "2":
            project_name = get_user_input("Enter project name: ")
            project = api.add_project(name=project_name)
            print(f"Added project {project.name} with ID {project.id}")
        elif choice == "3":
            project_id = get_user_input("Enter project ID to delete: ")
            is_success = api.delete_project(project_id=project_id)
            print(f"Deleted project {project_id}: {is_success}")
        elif choice == "4":
            tasks = api.get_tasks()
            print_tasks(tasks)
        elif choice == "5":
            content = get_user_input("Enter task content: ")
            due_string = get_user_input("Enter due date: ")
            priority = get_user_input("Enter priority (1-4): ")
            task = api.add_task(content=content, due_string=due_string, due_lang="en", priority=int(priority))
            print(f"Added task {task.content} with ID {task.id}")
        elif choice in ["6", "7", "8", "9"]:
            tasks = api.get_tasks()
            print_tasks(tasks)
            task_id = get_user_input("Enter task ID: ")
            if choice == "6":
                content = get_user_input("Enter new content: ")
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
            task_id = get_user_input("Enter task ID: ")
            if choice == "10":
                task_id = get_user_input("Enter task ID to list comments: ")
                comments = api.get_comments(task_id=task_id)
                if comments:
                    for comment in comments:
                        print(f"Comment ID: {comment.id}, Content: {comment.content}")
                else:
                    print("No comments found for this task.")
            elif choice == "11":
                content = get_user_input("Enter comment content: ")
                comment = api.add_comment(content=content, task_id=task_id)
                print(f"Added comment {comment.content} with ID {comment.id} to task {task_id}")
            elif choice == "12":
                comment_id = get_user_input("Enter comment ID to update: ")
                content = get_user_input("Enter new content: ")
                is_success = api.update_comment(comment_id=comment_id, content=content)
                print(f"Updated comment {comment_id}: {is_success}")
            elif choice == "13":
                comment_id = get_user_input("Enter comment ID to delete: ")
                is_success = api.delete_comment(comment_id=comment_id)
                print(f"Deleted comment {comment_id}: {is_success}")
        elif choice == "14":
            webbrowser.open("https://app.todoist.com/app/today")
        elif choice == "15":
            webbrowser.open("https://app.todoist.com/app/projects/active")
        elif choice == "16":
            print_goodbye()
            break
        else:
            print("Invalid choice. Please choose a number from 1 to 16.")

if __name__ == "__main__":
    main()