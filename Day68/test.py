import os

# Define the folder path
folder_path = 'path_to_your_folder'  # Replace with the actual folder path

# Create a dictionary to track the count of each file extension
file_count = {}

# Iterate through the files in the folder
for filename in os.listdir(folder_path):
    if os.path.isfile(os.path.join(folder_path, filename)):
        # Get the file extension
        file_extension = filename.split('.')[-1].lower()

        # Check if we have encountered this extension before
        if file_extension not in file_count:
            file_count[file_extension] = 1
        else:
            file_count[file_extension] += 1

        # Rename the file to the desired format
        new_filename = f"{file_count[file_extension]}.{file_extension}"
        os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, new_filename))

print("Files have been renamed successfully.")
