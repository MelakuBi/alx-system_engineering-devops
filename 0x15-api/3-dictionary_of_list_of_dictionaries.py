#!/usr/bin/python3
""" Using what you did in the task #0, extend your
Python script to export data in the CSV format. """
if __name__ == "__main__":
    import requests
    import json
    url_todos = "https://jsonplaceholder.typicode.com/todos/"
    url_users = "https://jsonplaceholder.typicode.com/users/"
    req_todos = requests.get(url_todos).json()
    req_users = requests.get(url_users).json()
    filename = "todo_all_employees.json"
    myDict = {}
    with open(filename, mode="w") as my_file:
        for i in req_users:
            USER_ID = i.get("id")
            myDict[USER_ID] = []
            for j in req_todos:
                if USER_ID == j.get("userId"):
                    USERNAME = i.get("username")
                    TASK_COMPLETED_STATUS = j.get("completed")
                    TASK_TITLE = j.get("title")
                    myDict[USER_ID].append({"task": TASK_TITLE,
                                            "completed": TASK_COMPLETED_STATUS,
                                            "username": USERNAME})
        json.dump(myDict, my_file)
