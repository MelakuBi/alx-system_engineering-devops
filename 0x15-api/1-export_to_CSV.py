#!/usr/bin/python3
""" Using what you did in the task #0, extend your
Python script to export data in the CSV format. """
if __name__ == "__main__":
    import requests
    import sys
    import csv
    USER_ID = sys.argv[1]
    uri_todos = "https://jsonplaceholder.typicode.com/todos?userId=" + USER_ID
    uri_users = "https://jsonplaceholder.typicode.com/users?id=" + USER_ID
    req_todos = requests.get(uri_todos).json()
    req_users = requests.get(uri_users).json()
    USERNAME = req_users[0].get("username")
    filename = "{}.csv".format(USER_ID)
    with open(filename, mode="w") as my_file:
        writer_file = csv.writer(my_file, quoting=csv.QUOTE_ALL)
        for i in req_todos:
            TASK_COMPLETED_STATUS = i.get("completed")
            TASK_TITLE = i.get("title")
            writer_file.writerow([USER_ID,
                                  USERNAME, TASK_COMPLETED_STATUS, TASK_TITLE])
