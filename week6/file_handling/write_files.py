# Create a file and write sample data

with open("example.txt", "w") as f:
    f.write("Hello, world!\n")
    f.write("This is a sample file.\n")

# Append new lines to the file
with open("example.txt", "a") as f:
    f.write("New line added.\n")

print("File created and updated successfully.")