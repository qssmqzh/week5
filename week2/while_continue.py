# while loop with continue

# Example 1
i = 0
while i < 5:
    i += 1
    if i == 3:
        continue
    print(i)

# Example 2
x = 0
while x < 6:
    x += 1
    if x % 2 == 0:
        continue
    print(x)

# Example 3
num = 0
while num < 4:
    num += 1
    if num == 2:
        continue
    print(num)

# Example 4
i = 1
while i <= 5:
    if i == 4:
        i += 1
        continue
    print(i)
    i += 1

# Example 5
count = 0
while count < 5:
    count += 1
    if count == 1:
        continue
    print(count)
