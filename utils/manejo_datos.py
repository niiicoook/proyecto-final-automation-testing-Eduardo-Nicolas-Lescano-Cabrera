import os
import csv
import json


def get_csv(file = "data_login.csv"):
    """
    arg: file representa el nombre del archivo a abrir
    return: una lista te tumplas con los elementos del csv
    """


    current_file = os.path.dirname(__file__)
    file = os.path.join(current_file, "..", "data", file)

    file = os.path.abspath(file)

    cases = []

    with open(file, newline="") as users:
        read = csv.DictReader(users)

        for dicUser in read:
            cases.append((
                          dicUser["username"],
                          dicUser["password"],
                          (dicUser["login_example"]).lower() == "true"
                          ))
            
    return cases



def get_json(file = "data_login.json"):
    """
    arg: file representa el nombre del archivo a abrir
    return: una lista te tumplas con los elementos del json
    """
    current_file = os.path.dirname(__file__)
    file = os.path.join(current_file, "..", "data", file)

    file = os.path.abspath(file)

    cases = []

    with open(file, newline="") as users:
        read = json.load(users)

        for users in read:
            cases.append((
                          users["username"],
                          users["password"],
                          users["login_example"]
                          ))
            
    return cases
