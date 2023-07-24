#!/usr/bin/python3
""" Using what you did in the task #0, extend your
Python script to export data in the CSV format. """
if __name__ == "__main__":
    import requests
    import sys
    import json
    USER_ID = sys.argv[1]
    uri_todos = "https://jsonplaceholder.typicode.com/todos?userId=" + USER_ID
    uri_users = "https://jsonplaceholder.typicode.com/users?id=" + USER_ID
    req_todos = requests.get(uri_todos).json()
    req_users = requests.get(uri_users).json()
    USERNAME = req_users[0].get("username")
    my_list = []
    my_dict = {}
    for i in req_todos:
        TASK_COMPLETED_STATUS = i.get("completed")
        TASK_TITLE = i.get("title")
        my_dict = {"task": TASK_TITLE,
                   "completed": TASK_COMPLETED_STATUS,
                   "username": USERNAME}
        my_list.append(my_dict)
    my_dict = {}
    my_dict = {USER_ID: my_list}
    filename = "{}.json".format(USER_ID)
    with open(filename, mode="w") as my_file:
        json.dump(my_dict, my_file)
