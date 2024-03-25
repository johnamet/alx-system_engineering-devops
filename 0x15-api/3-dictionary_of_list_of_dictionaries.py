#!/usr/bin/python3
"""
This script gathers data from an API about a user's todo list.
"""
import csv
import json
import requests
import sys


def gather_data_to_csv():
    """
    Gather data from an API about a user's todo list.

    Returns:
        None
    """
    # Base URL for the API
    base_url = "https://jsonplaceholder.typicode.com"

    # URLs for user and todo requests
    user_req_url = f"{base_url}/users"
    todo_req_url = f"{base_url}/todos"

    # Fetch user data
    users_response = requests.get(user_req_url)
    users_json = json.loads(users_response.text)

    # Fetch todo list data
    todos_response = requests.get(todo_req_url)
    todos_json = json.loads(todos_response.text)

    with open("todo_all_employees.json", mode="w", newline="") as file:
        data = {f'{user["id"]}': [{"username": user["username"],
                                   "task": todo["title"],
                                   "completed": todo["completed"]}
                                  for todo in todos_json
                                  if todo["userId"] == user["id"]]
                for user in users_json}
        json.dump(data, file)
        # csv.writer.writerow(header)
        # for todo in todos_json:
        #     if todo["userId"] == user_id:
        #         csv.writer.writerow([f'{user_id}',
        #                              f'{user_json["username"]}',
        #                              f'{todo["completed"]}',
        #                              f'{todo["title"]}'])


if __name__ == "__main__":
    # Get user ID from command line argument
    # if len(sys.argv) != 2:
    #     print("Usage: python script.py <user_id>")
    #     sys.exit(1)

    # Gather and display user's todo list
    gather_data_to_csv()
