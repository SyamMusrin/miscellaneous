#Python Script to rename multiple of files in a folder
import os

folder_path = ''  # Specify the path to the folder containing the files
file_extension = ''  # Specify the file extension of the files you want to rename

# Get a list of all files with the specified extension in the folder
files = [file for file in os.listdir(folder_path) if file.endswith(file_extension)]

# Sort the files alphabetically
files.sort()

# Rename the files with increasing numbers
for i, file_name in enumerate(files):
    file_path = os.path.join(folder_path, file_name)
    new_file_name = 'C' + str(i + 1) + file_extension
    new_file_path = os.path.join(folder_path, new_file_name)
    os.rename(file_path, new_file_path)
