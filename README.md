# Task Tracker

## About the Project:

Task Tracker is a simple yet powerful command-line interface (CLI) application originally created by [roadmap.sh](https://roadmap.sh/projects/task-tracker)
. It has been adapted to follow an Object-Oriented Programming (OOP) approach, enhancing the structure and scalability of the code. This application is designed to help users efficiently manage and track their tasks. Users can easily add, update, delete, and list tasks, as well as mark tasks as in-progress or completed. The project remains lightweight and easy to use, providing a practical solution for managing tasks directly from the terminal.

Key features of Task Tracker include:

- **Adding Tasks**: Quickly add tasks with a brief description.
- **Updating Tasks**: Modify task descriptions or update their status.
- **Deleting Tasks**: Remove tasks that are no longer needed.
- **Listing Tasks**: View tasks by their status (todo, in-progress, done) or view all tasks at once.
- **Multiple Task Addition**: Add multiple tasks in a single command.

This project solves the problem of task management by offering a streamlined, no-nonsense approach to keeping track of what needs to be done, what is in progress, and what has been completed, all within a simple command-line interface.

## Built With:

- **Python**: The primary programming language used to build the CLI.
- **JSON**: For lightweight and easy-to-manage data storage of tasks.

## Getting Started:

To get a local copy up and running, follow these simple steps.

### Prerequisites:

Ensure you have the following installed:

- **Python 3.6+**: Task Tracker requires Python to run.
- **Git**: To clone the repository.

### Installation:

1. **Clone the repository:**

 ```bash
   git clone https://github.com/your-username/task-tracker.git
 ```
 
2. **Navigate to the project directory:**

 ```bash
   cd task-tracker
 ```

3. **No additional dependencies are required**

No additional dependencies are required, as the project only relies on Python's standard library.

### Usage:

Task Tracker is designed to be used directly from the command line. Below are some example commands to get you started.

1. **Adding a single task:**
 ```bash
   python task_tracker.py add --description "Create a Task Tracker"
 ```
1. **Adding multiple task:**
 ```bash
   python task_tracker.py add --description "Learn OOP" "Refactor the code" "Write unit tests"
 ```
1. **Listing all tasks:**
```bash
   python task_tracker.py list
 ```
1. **Listing tasks by status:**
```bash
   python task_tracker.py list --status done
 ```
1. **Updating a task::**
```bash
   python task_tracker.py update --id 1 --status in-progress
 ```
1. **Deleting a task:**
```bash
   python task_tracker.py delete --id 2
 ```
### Features:

* Task Management: Add, update, delete, and list tasks.
* Task Status Tracking: Mark tasks as todo, in-progress, or done.
* Multiple Task Addition: Add several tasks at once with a single command.
* Lightweight and Fast: Minimal dependencies and quick execution.

## Contact:
For any questions or feedback, feel free to reach out:
* Github: [mmarcosh17](https://github.com/marcosh17r)
