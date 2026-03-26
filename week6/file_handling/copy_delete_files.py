import shutil
import os

# Copy file
shutil.copy("example.txt", "example_copy.txt")

# Create a backup
shutil.copy("example.txt", "backup_example.txt")

print("Files copied successfully.")

# Safely delete a file
file_to_delete = "example_copy.txt"

if os.path.exists(file_to_delete):
    os.remove(file_to_delete)
    print("File deleted successfully.")
else:
    print("File not found.")