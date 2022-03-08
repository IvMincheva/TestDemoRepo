import os
import json


def get_all_products():
    products = []
    with open(os.path.join("db", "products.txt"), "r") as file:
        for line in file:
            products.append(json.dumps())