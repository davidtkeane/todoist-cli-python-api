
from todoist_api_python.api import TodoistAPI
from dotenv import load_dotenv
import os
import webbrowser
from tabulate import tabulate

# Load the .env file
load_dotenv()

# Get the API key
api_key = os.getenv("TODOIST_API_KEY")

# Use the API key
api = TodoistAPI(api_key)

try:
    projects = api.get_projects()
    print("Connection Established.")
    print("\nYour Todoist Projects:")
    
    # Prepare data for tabulation
    table_data = []
    for project in projects:
        table_data.append([
            project.name,
            project.id,
            project.color,
            "Yes" if project.is_favorite else "No",
            "Yes" if project.is_shared else "No"
        ])
    
    # Print tabulated data
    headers = ["Name", "ID", "Color", "Favorite", "Shared"]
    print(tabulate(table_data, headers=headers, tablefmt="grid"))

except Exception as error:
    print(f"Error: {error}")
    print("Connection failed. Please check your API key and internet connection.")
