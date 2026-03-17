def isUsual(num):
    if num <= 0:
        return False

    for d in [2, 3, 5]:
        while num % d == 0:
            num //= d

    return num == 1


n = int(input())

if isUsual(n):
    print("Yes")
else:
    print("No")
