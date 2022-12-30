#!/usr/bin/env python3
import os
import re
from PIL import Image

source = "supplier-data/images"

for img in os.listdir(os.path.realpath(source)):
    nimg = os.path.join(source, img)
    if re.search(r"tiff", img):
        im = Image.open(nimg)
        im.resize([600, 400]).convert("RGB").save(nimg.replace(".tiff", ".jpeg"))
