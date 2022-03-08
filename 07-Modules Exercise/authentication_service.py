import json

import os

def register(username, password, first_name, last_name):

    with open(os.path.join("db", "users.txt", "r+") as file:
        #validation
        for user_line in file:
            user = json.loads(user_line.strip())
            print(user["username"])
            print(type(user))
            if user["username"] == username:
                return False

        user_obj = {
            "username": username,
            "password": password,
            "firstName": first_name,
            "lastName": last_name
        }

        file.write(json.dumps(user_obj))
        file.write("\n")
        return True


def login(username, password):
    with open(os.path.join)
        for user_line in users:
