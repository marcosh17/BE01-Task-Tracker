import json
import os
from datetime import datetime
import argparse

TASKS_FILE = 'tasks.json'

class Task:
    def __init__(self, id, description, status='todo', createdAt=None, updatedAt=None):
        self.id = id
        self.description = description
        self.status = status
        self.created_at = createdAt if createdAt else datetime.now().isoformat()
        self.updated_at = updatedAt if updatedAt else datetime.now().isoformat()

    def update(self, description=None, status=None):
        if description:
            self.description = description
        if status:
            self.status = status
        self.updated_at = datetime.now().isoformat()

    def to_dict(self):
        return {
            'id': self.id,
            'description': self.description,
            'status': self.status,
            'createdAt': self.created_at,
            'updatedAt': self.updated_at
        }

class TaskManager:
    def __init__(self, file_name=TASKS_FILE):
        self.file_name = file_name
        self.tasks = self.load_tasks()

    def load_tasks(self):
        if not os.path.exists(self.file_name):
            return []
        with open(self.file_name, 'r') as file:
            tasks_data = json.load(file)
            return [Task(**task_data) for task_data in tasks_data]

    def save_tasks(self):
        with open(self.file_name, 'w') as file:
            json.dump([task.to_dict() for task in self.tasks], file, indent=4)

    def add_task(self, description):
        new_id = self.generate_task_id()
        new_task = Task(new_id, description)
        self.tasks.append(new_task)
        self.save_tasks()
        print(f"Task '{description}' added successfully.")

    def generate_task_id(self):
        if self.tasks:
            return max(task.id for task in self.tasks) + 1
        else:
            return 1

    def list_tasks(self, status=None):
        tasks_to_list = self.tasks
        if status:
            tasks_to_list = [task for task in self.tasks if task.status == status]

        if not tasks_to_list:
            print("No tasks to display.")
        else:
            for task in tasks_to_list:
                print(f"[{task.id}] {task.description} - {task.status} (Created: {task.created_at}, Updated: {task.updated_at})")

    def update_task(self, task_id, description=None, status=None):
        task = self.find_task_by_id(task_id)
        if task:
            task.update(description, status)
            self.save_tasks()
            print(f"Task '{task_id}' updated successfully.")
        else:
            print(f"Task with ID: {task_id} not found.")

    def delete_task(self, task_id):
        task = self.find_task_by_id(task_id)
        if task:
            self.tasks.remove(task)
            self.save_tasks()
            print(f"Task '{task_id}' deleted successfully.")
        else:
            print(f"Task with ID: {task_id} not found.")

    def find_task_by_id(self, task_id):
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None

def main():
    manager = TaskManager()

    parser = argparse.ArgumentParser(description="Task Tracker CLI")
    parser.add_argument('action', choices=['add', 'list', 'update', 'delete'], help="Action to perform")
    parser.add_argument('--description', nargs='+', help="Task description(s)")
    parser.add_argument('--id', type=int, help="Task ID")
    parser.add_argument('--status', choices=['todo', 'in-progress', 'done'], help="Task status")

    args = parser.parse_args()

    if args.action == 'add':
        if not args.description:
            print("Error: At least one description is required to add a task.")
        else:
            for desc in args.description:
                manager.add_task(desc)

    elif args.action == 'list':
        if args.status:
            manager.list_tasks(status=args.status)
        else:
            manager.list_tasks()

    elif args.action == 'update':
        if not args.id:
            print("Error: An ID is required to update a task.")
        elif not args.description and not args.status:
            print("Error: At least a description or status is required to update the task.")
        else:
            manager.update_task(args.id, description=args.description[0] if args.description else None, status=args.status)

    elif args.action == 'delete':
        if not args.id:
            print("Error: An ID is required to delete a task.")
        else:
            manager.delete_task(args.id)

if __name__ == "__main__":
    main()


