#! /usr/bin/env python3
import os
import requests

SOURCE = "supplier-data/descriptions"
URL = "http://localhost/upload/"

for file in os.listdir(SOURCE):
    with open(os.path.join(SOURCE, file)) as f:
        x = f.readlines()
        name = x[0].strip()
        weight = int(x[1].strip())
        description = x[2].strip()
        image_name = file.replace("txt", "jpeg")
        product = {"name": name, "weight": weight, "description": description, "image_name": image_name}
        print(product)
        r = requests.post(URL, data=product)