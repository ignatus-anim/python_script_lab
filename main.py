# Step 1: Import required Modules

import requests
import os
import shutil
from datetime import datetime

# step 2: Clean Up Previous Directory

if os.path.exists('ignatus_anim'):
    try:
        shutil.rmtree('ignatus_anim')
        print(f"Directory {'ignatus_anim'} has been removed successfully.")
    except Exception as e:
        print(f"Error: {e}")

# step 3: Create a New Directory

download_folder = 'ignatus_anim'
if not os.path.exists(download_folder):
    os.makedirs(download_folder)
    print(f"Directory: {download_folder} created.")

# step 4
local_file_path = os.path.join(download_folder, "ignatus_anim")

# step 5: Download the file
url = "https://raw.githubusercontent.com/sdg000/pydevops_intro_lab/main/change_me.txt"

response = requests.get(url)
if response.status_code == 200:
    print(f"File successfully downloaded.")
    with open(local_file_path, 'wb') as file:
        file.write(response.content)
        print("File saved successfully")

else:
    print(f"Failed to download file. Status code: {response.status_code}")

# Step 6: Overwrite File content

user_input = input("Describe what you have learned so far in a sentence: ")
now = datetime.now()
current_time = now.strftime("%Y-%m-%d %H:%M:%S")

with open(local_file_path, "w") as file:
    file.write(user_input + "\n")
    file.write(f"Last modified on: {current_time}")
    print("File successfully modified.")

# Step 7: Display the Updated File Content

with open(local_file_path, "r") as file:
    print("\nYou Entered: ", end='')
    print(file.read())