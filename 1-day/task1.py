with open("data.txt", 'r') as file:
    data = file.read()

def find_number(data):
    numbers = []
    for line in data.split("\n"):
        digits = [char for char in line if char.isdigit()]
        numbers.append(10*int(digits[0]) + int(digits[-1]))
    return numbers

numbers = find_number(data)
numbers_sum = sum(numbers)
print(numbers)
print(numbers_sum)