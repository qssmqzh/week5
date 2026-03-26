import os

# Create nested directories
os.makedirs("test_dir/subdir1/subdir2", exist_ok=True)

print("Directories created successfully.")

# List files and folders
items = os.listdir("test_dir")
print("Contents of test_dir:", items)