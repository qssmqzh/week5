s = input()

# mapping
to_digit = {
    "ZER": "0", "ONE": "1", "TWO": "2", "THR": "3",
    "FOU": "4", "FIV": "5", "SIX": "6",
    "SEV": "7", "EIG": "8", "NIN": "9"
}

to_word = {v: k for k, v in to_digit.items()}

# find operator
for op in "+-*":
    if op in s:
        operator = op
        break

left, right = s.split(operator)

# convert left
num1 = ""
for i in range(0, len(left), 3):
    num1 += to_digit[left[i:i+3]]

# convert right
num2 = ""
for i in range(0, len(right), 3):
    num2 += to_digit[right[i:i+3]]

# calculate
num1 = int(num1)
num2 = int(num2)

if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
else:
    result = num1 * num2

# convert back
result_str = ""
for digit in str(result):
    result_str += to_word[digit]

print(result_str)
