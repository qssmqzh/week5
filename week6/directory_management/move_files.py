import shutil
import os

# Create destination directory
os.makedirs("destination", exist_ok=True)

# Move file
if os.path.exists("example.txt"):
    shutil.move("example.txt", "destination/example.txt")
    print("File moved successfully.")

# Copy file back
shutil.copy("destination/example.txt", "example_copy2.txt")
print("File copied back successfully.")