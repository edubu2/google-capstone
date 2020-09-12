#!/usr/bin/env python3
import requests
import glob

image_dir = "/home/student-04-fbc89b151ccf/supplier-data/images/" # update to linux path
images = glob.glob(image_dir + '*')

url = 'http://localhost/upload/'

def upload_images(image_files):
  for image in images:
    print("Uploading image: {}...".format(image))
    with open(image, 'rb') as f:
        response = requests.post(url, files={'file':f})
        print(response.status_code, ' ', response.reason)

def main():
  upload_images(images)

if __name__ == '__main__':
  main()
