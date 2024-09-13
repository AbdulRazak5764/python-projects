import os
import shutil

# Define the directory to organize
source_dir = '/path/to/your/folder'

# Define the destination folders for different file types
dest_dirs = {
    'Images': ['.jpg', '.png', '.jpeg', '.gif'],
    'Documents': ['.pdf', '.docx', '.txt', '.xlsx'],
    'Videos': ['.mp4', '.mov', '.avi'],
}

# Create destination folders if they don't exist
for folder in dest_dirs.keys():
    os.makedirs(os.path.join(source_dir, folder), exist_ok=True)

# Move files to the appropriate folders
for filename in os.listdir(source_dir):
    file_ext = os.path.splitext(filename)[1].lower()
    for folder, extensions in dest_dirs.items():
        if file_ext in extensions:
            shutil.move(os.path.join(source_dir, filename), os.path.join(source_dir, folder, filename))
            print(f'Moved {filename} to {folder}')
            break

print("File organization complete.")
