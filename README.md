# 📝 Todoist from Command Line

## README.md

<h1 align="center">Hi, guys! <img src="https://github.com/FujiwaraChoki/FujiwaraChoki/blob/main/assets/238178097-766d336d-b87d-44ba-807c-c51de2bc6b4d.gif" width="28px" alt="👋"></h1>

<p align="center">
    <br>
    <i>
        I'm Rangersmyth (internet name), 18 May 2024, there is a few problems with the script, I am working on fixing it.<br>
    </i>
<p align="center">


![PowerShell](https://img.shields.io/badge/-PowerShell-black?style=flat-square&logo=powershell)

![GitHub last commit](https://img.shields.io/github/last-commit/davidtkeane/jervis-ChatGPT?style=flat-square)
![GitHub issues](https://img.shields.io/github/issues-raw/davidtkeane/jervis-ChatGPT?style=flat-square)

<b>Languages</b>

[![Python](https://img.shields.io/badge/python-black?style=for-the-badge&logo=python)](https://github.com/davidtkeane)

<b>OS</b>

[![Linux](https://img.shields.io/badge/linux-black?style=for-the-badge&logo=Linux)](https://github.com/davidtkeane)
[![Windows](https://img.shields.io/badge/Windows-black?style=for-the-badge&logo=Windows)](https://github.com/davidtkeane)

<p align="center">
    <b>Welcome to Todoist online note taker uses with API!</b>
    <br>
    <br>
    <i>
        I'm Rangersmyth (internet name), and I'm currently learning Python and Bash coding.<br>
    <br>
    </i>
    <br>

<p align="center">
  <img src="https://count.getloli.com/get/@rangersmyth?theme=gelbooru" />
</p>

<div align="center">
<a href="https://github.com/davidtkeane" target="_blank">
<img src=https://img.shields.io/badge/github-%2324292e.svg?&style=for-the-badge&logo=github&logoColor=white alt=github style="margin-bottom: 5px;" />
</a>
<a href="https://twitter.com/davidtkeane" target="_blank">
<img src=https://img.shields.io/badge/twitter-%2300acee.svg?&style=for-the-badge&logo=twitter&logoColor=white alt=twitter style="margin-bottom: 5px;" />
</a>
<a href="https://linkedin.com/in/sami-hindi-b31435248/" target="_blank">
<img src=https://img.shields.io/badge/linkedin-%231E77B5.svg?&style=for-the-badge&logo=linkedin&logoColor=white alt=linkedin style="margin-bottom: 5px;" />
</a>
</div>

## 🧐 About


<img src="https://sm.pcmag.com/t/pcmag_uk/review/t/todoist/todoist_wpyr.1920.jpg" alt="Todoist" class="center">

<p style="text-align: center;">
<a href="https://todoist.com/">Sign up for a Todoist account</a>
</p>
 <p>
        Todoist is a powerful task management app that helps you organize your life. With Todoist, you can create tasks and projects, set due dates and priorities, and even assign tasks to others. Todoist syncs across all your devices, so you can manage your tasks wherever you are. It also integrates with many other apps and services, including Gmail, Google Calendar, Slack, Amazon Alexa, and more. Whether you're managing a team, writing an epic screenplay, or just making a grocery list, Todoist is there to help you achieve more every day.
</p>
<br>

I had an idea if I could connect Todoist to my original todo_list program I made (Not uploaded yet) for Powershell, the Powershell todo_list was finished, and I thought if I could connect my todo_list to Todoist. This script does not do that, this script is to let you control your Todoist from the terminal or command line. This script lets you do most things available with this code. I copied and pasted all the code from the Todoist API guide, and with the help of GitHUb CoPilot we arrived at this script. Please enjoy and upgrade and own it.

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

## 🥷 Where to get the Todoist API key.

1. Login with a new account or old account.
2. Then go to today https://app.todoist.com/app/today
3. Click your profile name and settings.
4. Click Integrations
5. Click Developer
6. Copy API Token
7. Add to .env file

## 💻 Developer API Documentation

1. Developing with Todoist https://developer.todoist.com/guides/#developing-with-todoist
2. Todoist REST API. This is the code the script uses https://developer.todoist.com/rest/v2/#overview

## 🚀 Now we are ready to launch

1. Clone this repository to your local machine.
2. Run the install_todoist.py file as this will go step by step to install the modules and also the ability to add the Todoist API key into the terminal and then that goes into the .env file for you. 
3. This install_todoist.py will then ask you if you want to run the main file todoist.py
4. You only need to run this file once.
5. The Normal way to run will be python todoist.py

Or

1. Install the required Python packages using pip:

```bash
pip install todoist-python python-dotenv
```
2. After install, get your Todoist key from the website.
3. Copy the .env key into the .env file in the same directory.
4. TODOIST_API_KEY=your_api_key
5. Replace `your_api_key` with your actual Todoist API key.
6. Run the script from your terminal with the following command:
7. Replace `your_api_key` with your actual Todoist API key.

## 📖 Usage

To use the `todoist.py` script, you can run the following command in PowerShell or Linux/Mac terminal:

```powershell
Run the script from your terminal with the following command:

python todoist.py
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
