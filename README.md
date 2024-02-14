# EADME.md

## 📝 Todoist from Command Line

<h1 align="center">Hi, guys! <img src="https://github.com/FujiwaraChoki/FujiwaraChoki/blob/main/assets/238178097-766d336d-b87d-44ba-807c-c51de2bc6b4d.gif" width="28px" alt="👋"></h1>

![PowerShell](https://img.shields.io/badge/-PowerShell-black?style=flat-square&logo=powershell)

![GitHub last commit](https://img.shields.io/github/last-commit/davidtkeane/jervis-ChatGPT?style=flat-square)
![GitHub issues](https://img.shields.io/github/issues-raw/davidtkeane/jervis-ChatGPT?style=flat-square)

Languages

[![Python](https://img.shields.io/badge/python-black?style=for-the-badge&logo=python)](https://github.com/davidtkeane)

OS

[![Linux](https://img.shields.io/badge/linux-black?style=for-the-badge&logo=Linux)](https://github.com/davidtkeane)
[![Windows](https://img.shields.io/badge/Windows-black?style=for-the-badge&logo=Windows)](https://github.com/davidtkeane)

<p align="center">
  <img src="https://user-images.githubusercontent.com/49094051/227788148-a8ff8e06-86a4-41a6-aa53-8b7d6855360c.png"/>
  <br>
  <i>Image by MidJourney AI</i>
  <br>
  <a href="https://github.com/gia-guar/JARVIS-ChatGPT/tree/main">This is the URL to the Jarvis Github Project</a>
  <br>
  This is Jervis by Gia-Guar.
  <br>
  <a href="https://github.com/davidtkeane/todoist-cli-python-api/tree/main">This is the URL to the my Jervis Github Project</a>
  <p>This Python script is for a voice interface chatbot named Jervis. It uses OpenAI's GPT-3.5-turbo-instruct model to respond to user input. The user can interact with the chatbot through speech, and the chatbot responds with text and/or speech. The conversation can be saved as an MP3 file and emailed to a specified address. The conversation is also logged to a MongoDB database.</p>
  <br>
</p>


## 🧐 About

The Todoist CLI is a Python script that interacts with the Todoist API to provide a command-line interface for managing your Todoist tasks.

The script uses the `todoist-python` package to interact with the Todoist API and the `python-dotenv` package to load environment variables from a .env file. The environment variable `TODOIST_API_KEY` is used to authenticate with the Todoist API.

When you run the script, it displays a menu of options for managing your Todoist tasks. You can list, add, update, close, reopen, and delete tasks. You can also manage projects and comments. In addition, you can open the Todoist web app to view today's tasks and your active projects.

Here's how it works:

1. The script loads your Todoist API key from a .env file using `python-dotenv`.
2. It creates a `TodoistAPI` object using your API key.
3. It displays a menu of options and asks you to choose an option.
4. Depending on your choice, it calls a function to perform the chosen operation. For example, if you choose to list tasks, it calls the `get_tasks` method on the `TodoistAPI` object and then prints the tasks.
5. If an operation requires user input, such as adding a task, it prompts you to enter the necessary information.
6. After performing an operation, it goes back to step 3, unless you choose to exit the script.

This script provides a quick and easy way to manage your Todoist tasks from your terminal. It's especially useful if you prefer using the command line over a graphical user interface, or if you want to automate your task management with scripts.

## 🚀 Installation

1. Clone this repository to your local machine.
2. Install the required Python packages using pip:

```bash
pip install todoist-python python-dotenv
```

3. Create a .env file in the same directory as the script and add your Todoist API key:
4. TODOIST_API_KEY=your_api_key
5. Replace `your_api_key` with your actual Todoist API key.
6. Run the script from your terminal with the following command:
7. Replace `your_api_key` with your actual Todoist API key.

## 📖 Usage

To use the `todoist_list.py` script, you can run the following command in PowerShell:

```powershell
Run the script from your terminal with the following command:

python todoist_list.py
```

## 📚 Available Commands in Program

==============================

1. List projects
2. Add project
3. Delete project
4. List tasks
5. Add task
6. Update task
7. Close task
8. Reopen task
9. Delete task
10. List comments
11. Add comment
12. Update comment
13. Delete comment
14. View today's tasks online
15. View projects online
16. Exit

## 🛠️ Functions

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📜 License

This project is licensed under the MIT License.

## 📞 Contact

If you have any questions, feel free to reach out to me at rangersmyth.74@gmail.com
