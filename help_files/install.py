#!/usr/bin/env python3

# Created by Ranger

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
        f.write(f'TODOIST_API_KEY="{api_key}"\n')
    print("API key added successfully.")
    print("Contents of .env file:")
    with open('.env', 'r') as f:
        print(f.read())

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
    print("When you click on the API key, it is copied. You can paste it with Cmd+V or right click with the mouse.")
    print("="*30 + "\n")

    api_key = input("Please paste your API key here: ")
    write_api_key_to_env(api_key)

    required_modules = ["todoist-api-python", "python-dotenv", "tabulate", "todoist"]

    print("\nThe following modules are required:")
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
    print("Requirements are installed and this Setup is complete!")
    print("Running the API test script...")
    os.system("python todoist_api_test.py")
    print("The API test Setup is complete if you see your Todoist Account!")

    print("\n" + "="*30)
    print("The API test Setup is complete!")
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