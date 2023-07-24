#!/usr/bin/python3
""" script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress. """
if __name__ == "__main__":
    import requests
    import sys
    empl_id = sys.argv[1]
    uri_todos = "https://jsonplaceholder.typicode.com/todos?userId=" + empl_id
    uri_users = "https://jsonplaceholder.typicode.com/users?id=" + empl_id
    req_todos = requests.get(uri_todos).json()
    req_users = requests.get(uri_users).json()
    empl_name = req_users[0].get("name")
    tasks = []
    for task in req_todos:
        if task.get("completed") is True:
            tasks.append(task.get("title"))
    print("Employee {} is done with tasks({}/{}):"
          .format(empl_name, len(tasks), len(req_todos)))
    for task in tasks:
        print("\t {}".format(task))
