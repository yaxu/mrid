## Thanks to buobubobubobubo

import os
import json

def generate_json():
    data = {
        "_base": "https://raw.githubusercontent.com/yaxu/mrid/main/"
    }
    
    # Iterate through each directory in the sounds folder
    os.chdir("sounds")
    for dir_name, _, file_list in os.walk('./',True,None,True):
        print(dir_name, file_list)
        if len(file_list) == 0:
            continue
        dir_name = dir_name[2:]  # Remove the './' from the directory name
        data[dir_name] = []
        for file_name in file_list:
            if file_name.lower().endswith('.wav'):
                data[dir_name].append(f"sounds/{dir_name}/{file_name}")
    os.chdir("../")
    with open('strudel.json', 'w') as json_file:
        # Minify if possible
        json.dump(data, json_file, separators=(',', ':'))

if __name__ == "__main__":
    generate_json()
