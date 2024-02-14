# README.md

## Todo PowerShell Script 📝

![PowerShell](https://img.shields.io/badge/-PowerShell-black?style=flat-square&logo=powershell)

![GitHub last commit](https://img.shields.io/github/last-commit/<username>/<repo>?style=flat-square)

![GitHub issues](https://img.shields.io/github/issues-raw/<username>/<repo>?style=flat-square)

This is a robust and user-friendly PowerShell script that provides a simple yet powerful todo list functionality. It allows you to add, remove, and list todo items, and it also supports notifications.

## 🚀 Installation

1. Clone this repository to your local machine using `git clone <repo-link>`.
2. Navigate to the directory that contains the `Todo.ps1` script.
3. Run the   `.\install.ps1` script in PowerShell.
4. This will check if you have powershell installed.
5. This script will then check if the module for making notifications.
6. The script will then ask you for the PATH of where you saved these files to E.G. "C:\Users\You\todo" Replace `<path to Todo.ps1>` with the actual path to the `Todo.ps1` script.
7. This script will then add the PATH to the PowerShell profile file, this is so you can just type "todo list" without running the file from it's folder all the time. See Usage for more details.
8. Now the script is ready to be used on the terminal. Type "todo hello" and
9. Commands can be found by typing "todo --help" or see below.
10. The script will create 2 .xml files and one folder called xml and a error.log file and log folder.

## 📖 Usage

To use the `Todo.ps1` script, you can run the following command in PowerShell:

```powershell
C:\todo hello
C:\todo --help
C:\todo add "Hello-There"
C:\todo notify 10 1 minutes
C:\todo done
```

📚 Available Commands

* `todo add <item>`: Add a new todo item.
* `todo rm <item>`: Remove a todo item by its content.
* `todo list`: List all todo items with timestamps.
* `todo list`-all: List all todo items without the time being shown.
* `todo done`: List all todo done items.
* `todo hello`: Shows you the welcome screen.
* `todo --help`: Shows you the help menu with these commands.
* `todo notify <id> <time> <unit>`: Set a notification for a todo item. The `<id>` is the number of the todo item, `<time>` is the time before the notification, and `<unit>` is the unit of time (e.g., `minutes`, `hours, days`).

## 🛠️ Functions

* `Show-Help`: Show the help information.
* `Set-TodoNotification`: Set a notification for a todo item.

## 📝 Error Logging

If an error occurs during the execution of the script, the error message and the line of code that caused the error will be written to the `error.log` file.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📜 License

This project is licensed under the MIT License.

## 📞 Contact

If you have any questions, feel free to reach out to me at rangersmyth.74@gmail.com
