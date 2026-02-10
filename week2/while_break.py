# while loop with break

# Example 1
i = 1
while True:
    print(i)
    if i == 3:
        break
    i += 1

# Example 2
x = 0
while x < 10:
    if x == 5:
        break
    print(x)
    x += 1

# Example 3
while True:
    print("Running")
    break

# Example 4
num = 1
while num <= 10:
    if num == 7:
        break
    print(num)
    num += 1

# Example 5
i = 0
while i < 5:
    print(i)
    if i == 2:
        break
    i += 1
