#!/usr/bin/env python3

import glob
import os
import requests
import json
import re

# get list of all files (full path) in the descriptions directory
descriptions_folder = "C:/Users/Elliot/Python/Google/capstone/supplier-data/descriptions/"
descriptions = glob.glob(descriptions_folder + '*')

# update with lab's external IP address
url = 'http://104.197.242.180/fruits/'

def generate_json(descriptions_file_list):
    """This function parses the description files and returns a list of JSON dictionaries to be uploaded one-by-one"""

    json_list = []
    for d in descriptions_file_list:
        if d.endswith('.txt') == False:
            continue
        f = open(d, 'r')
        # convert each line of the file into an element in a list
        lines = f.readlines()
        # get the filename of the image associated with the description
        fn, ext = os.path.splitext(os.path.basename(d))
        img_fn = fn + '.jpeg'
        # create the dictionary with description data to be uploaded later
        weight_int = int(re.sub(r"[^0-9]", '', lines[1].strip()))
        description_data = {
        'name': lines[0].strip(),
        'weight': weight_int,
        'description': lines[2].strip(),
        'image_name': img_fn,
        }
        # add the dictionary to the list, which we will later iterate thru & upload each description
        json_list.append(description_data)
    return json_list

def upload_data(descriptions_formatted):
    for description in descriptions_formatted:
        data_json = json.loads(json.dumps(description))
        print("Uploading {}...".format(description['name']))
        response = requests.post(url, json=data_json)
        if response.status_code == 201:
            print("Successfully uploaded {}.".format(description['name']))

def main():
    data = generate_json(descriptions)
    # print(data)
    #upload_data(data) #uncomment in lab to actually upload the data

main()
