# for loop with continue

# Example 1
for i in range(5):
    if i == 2:
        continue
    print(i)

# Example 2
for i in range(1, 6):
    if i % 2 == 0:
        continue
    print(i)

# Example 3
for char in "python":
    if char == "o":
        continue
    print(char)

# Example 4
nums = [1, 2, 3, 4]
for n in nums:
    if n == 3:
        continue
    print(n)

# Example 5
for i in range(10):
    if i < 5:
        continue
    print(i)
