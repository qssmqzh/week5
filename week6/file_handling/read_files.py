# Read and print file contents

with open("example.txt", "r") as f:
    content = f.read()

print("File content:")
print(content)