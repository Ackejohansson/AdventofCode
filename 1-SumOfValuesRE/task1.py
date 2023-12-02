with open("data.txt", 'r') as file:
    data = file.read().split("\n")

def find_sum(data):
    sum = 0
    for line in data:
        digits = [int(char) for char in line if char.isdigit()]
        sum += 10*digits[0] + digits[-1]
    return sum

sum = find_sum(data)
print(sum)


