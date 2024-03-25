#!/usr/bin/python3
"""
This script gathers data from an API about a user's todo list.
"""

import json
import requests
import sys


def gather_data(user_id):
    """
    Gather data from an API about a user's todo list.

    Args:
        user_id (int): The ID of the user.

    Returns:
        None
    """
    # Base URL for the API
    base_url = "https://jsonplaceholder.typicode.com"

    # URLs for user and todo requests
    user_req_url = f"{base_url}/users/{user_id}"
    todo_req_url = f"{base_url}/todos"

    # Fetch user data
    user_response = requests.get(user_req_url)
    user_json = json.loads(user_response.text)

    # Fetch todo list data
    todos_response = requests.get(todo_req_url)
    todos_json = json.loads(todos_response.text)

    # Filter todos for the specific user
    user_todos_dict = {
        "completed": [todo for todo in todos_json
                      if todo['userId'] == user_id and todo["completed"]],
        "uncompleted": [todo for todo in todos_json
                        if todo['userId'] == user_id and not todo["completed"]]
    }

    # Count completed and uncompleted todos
    num_completed = len(user_todos_dict["completed"])
    num_uncompleted = len(user_todos_dict["uncompleted"])
    total_todos = num_completed + num_uncompleted

    # Print user's todo list summary
    print("Employee {} is done with tasks({}/{}):"
          .format(user_json["name"], num_completed, total_todos))
    for todo in user_todos_dict["completed"]:
        print("\t {}".format(todo["title"]))


if __name__ == "__main__":
    # Get user ID from command line argument
    if len(sys.argv) != 2:
        print("Usage: python script.py <user_id>")
        sys.exit(1)
    user_id = int(sys.argv[1])

    # Gather and display user's todo list
    gather_data(user_id)
