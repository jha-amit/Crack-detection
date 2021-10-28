# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# convert images from tif to jpeg
import os
from PIL import Image

path = os.getcwd()+'\Data\OneDrive_2021-08-16\Parking Lot'
#print(path)
for root, dirs, files in os.walk(path, topdown=False):
    for name in files:
        print(os.path.join(root, name))
        if os.path.splitext(os.path.join(root, name))[1].lower() == ".tif":
            print(1)
        # if os.path.splitext(os.path.join(root, name))[1].lower() == ".tif":
            if os.path.isfile(os.path.splitext(os.path.join(root, name))[0] + ".jpg"):
                print ("A jpeg file already exists for %s" % name)
            # If a jpeg is *NOT* present, create one from the tiff.
            outfile = os.path.splitext(os.path.join(root, name))[0] + ".jpg"
            try:
                im = Image.open(os.path.join(root, name))
                print ("Generating jpeg for %s" % name)
                im.thumbnail(im.size)
                im.save(outfile, "JPEG", quality=100)
            except Exception as e:
                print (e)