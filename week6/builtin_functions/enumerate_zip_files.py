names = ["Alice", "Bob", "Charlie"]
scores = [85, 90, 78]

# enumerate()
for i, name in enumerate(names):
    print(f"{i}: {name}")

# zip()
for name, score in zip(names, scores):
    print(f"{name} scored {score}")

# type checking и преобразования
value = "123"

if isinstance(value, str):
    number = int(value)
    print("Converted to int:", number)