import configparser
import datetime
import os
import subprocess

# Read configuration from INI file
config = configparser.ConfigParser()
config.read("config.ini")

from_date = config["TRACE"]["FROM_DATE"]
image_file_name_to_get = config["GENERAL"]["IMAGE_FILE_NAME_TO_GET"]
default_dir = config["GENERAL"]["DEFAULT_DIR"]

subdirs = []
for key, value in config["SUB_DIRECTORIES_TO_SEARCH"].items():
    subdirs.append(value)

# Get current date and extract month and date
current_date = datetime.datetime.now()
month = current_date.strftime("%m")
date = current_date.strftime("%d")

# Construct search folder path
search_dirs = []
for subdir in subdirs:
    search_dir = os.path.join(default_dir, subdir, month, date)
    if os.path.exists(search_dir):
        search_dirs.append(search_dir)

# Check if output folder exists, create if not
# if not os.path.exists(search_dirs):
#     os.makedirs(search_dirs)

# Loop through all subfolders in the specified path
# for subfolder in os.listdir(search_dirs):
#     subfolder_path = os.path.join(search_dirs, subfolder)
    for search_dir in search_dirs:
        


    # Look for the image file in the subfolder
    image_path = os.path.join(subfolder_path, image_file_name_to_get)
    if os.path.exists(image_path):
        # Convert TIF to JPG using IrfanView
        output_filename = os.path.splitext(image_file_name_to_get)[0] + ".jpg"
        output_path = os.path.join(search_dirs, output_filename)
        command = f"i_view64.exe \"{image_path}\" /advancedbatch /convert=.\\output\\\"{output_filename}\""
        subprocess.run(command, shell=True)

# Update FROM_DATE in INI file
config["DEFAULT"]["FROM_DATE"] = str(current_date)
with open("config.ini", "w") as f:
    config.write(f)

# Exit program
print(f"Finished converting TIFs to JPGs for {current_date}.")
exit()