# Call a function N times in Python

def print_message(message):
    print(message)

number = 1

for _ in range(5):
    number = number * 2
    print_message('bobbyhadz.com')

print(number)  # 👉️ 32