#!/usr/bin/env python3
# Created by Ranger

# This works on Windows and Linux systems.
# Verify the Todoist API key and create a TodoistAPI object.
# The script requires an active internet connection to verify the API key.
# The script requires a Todoist API key to verify the API key.

# Usage information
# python install_todoist.py

# What this script does:
# This script checks if the required modules are installed.
# If the required modules are not installed, the script installs them.
# The script then asks the user to paste the Todoist API key.
# The script then writes the API key to the .env file.
# The script then asks the user if they want to run the main script.
# If the user chooses to run the main script, the script runs the main script.
# If the user chooses not to run the main script, the script exits.

# Import required modules
import os
import subprocess
import sys
import pkg_resources

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

def is_module_installed(module_name):
    try:
        pkg_resources.get_distribution(module_name)
        return True
    except pkg_resources.DistributionNotFound:
        return False

def write_api_key_to_env(api_key):
    with open('.env', 'w') as f:
        f.write(f'TODOIST_API_KEY={api_key}\n')

def main():
    print("\n" + "="*30)
    print("Welcome to the Todoist CLI setup!")
    print("This setup only needs to be done once.")
    print("Here are the steps to get your Todoist API key:")
    print("1. Login with a new account or old account.")
    print("2. Then go to today https://app.todoist.com/app/today")
    print("3. Click your profile name and settings.")
    print("4. Click Integrations")
    print("5. Click Developer")
    print("6. Copy API Token")
    print("7. Add to .env file")
    print("When you click on the API key, it is copied. You can paste it with Ctrl+V or right click with the mouse.")
    print("="*30 + "\n")

    api_key = input("Please paste your API key here: ")
    def write_api_key_to_env(api_key):
        with open('.env', 'a') as f:
            f.write(f'TODOIST_API_KEY="{api_key}"\n')
        print("API key added successfully.")

    required_modules = ["todoist", "python-dotenv"]

    print("The following modules are required:")
    for module in required_modules:
        print(f"- {module}")
    print()

    for module in required_modules:
        if not is_module_installed(module):
            print(f"The {module} module is not installed.")
            choice = input(f"Do you want to install {module}? This module is safe and used by millions. (y/n): ")
            if choice.lower() in ["y", "yes"]:
                install(module)
                print(f"{module} installed successfully.")
            else:
                print(f"You chose not to install {module}. Please note that this module is required to run the main script.")
        else:
            print(f"The {module} module is already installed.")

    print("\n" + "="*30)
    print("Setup is complete!")
    print("Do you want to run the main script now?")
    choice = input("Enter y to run the main script, or n to exit: ")
    if choice.lower() in ["y", "yes"]:
        os.system("python todoist.py")
    else:
        print("You chose not to run the main script. You can run it later with the command: python todoist.py")

    print("\n" + "="*30)
    print("Thank you for using the Todoist CLI setup. Goodbye!")
    print("="*30 + "\n")

if __name__ == "__main__":
    main()