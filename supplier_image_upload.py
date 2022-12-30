#!/usr/bin/env python3
import os
import re
import requests

SOURCE = "supplier-data/images"
URL = "http://localhost/upload/"

for img in os.listdir(os.path.realpath(SOURCE)):
    if re.search(r"jpeg$", img):
        img_fp = os.path.join(SOURCE, img)
    with open(img_fp) as opened:
        r = requests.post(URL, files={'file': opened})
        opened.close()