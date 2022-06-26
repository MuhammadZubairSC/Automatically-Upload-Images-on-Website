#!/usr/bin/env python3
import requests
import os
import glob

url = "http://localhost/upload/"
def upload_images(url, filePath):
    search_image=filePath+"*.jpeg"
    imageList = glob.glob(search_image)
    try:
        for image in imageList:
            with open(image, 'rb') as opened:
              r = requests.post(url, files={'file': opened})

    except IOError as e:
        print("IOError!")

if __name__ == "__main__":
    filePath=os.path.join(os.getcwd(),'supplier-data/images/')
    url = "http://localhost/upload/"
    dir_t = upload_images(url, filePath)