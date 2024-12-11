import re

input = ""

with open("day3/input", "r") as f:
    input = f.read()


commands = re.findall(r"mul\(\d{1,3},\d{1,3}\)", input)

result = 0

for command in commands:
    sides = command.split(",")
    num1 = int(sides[0][4:])
    num2 = int(sides[1][:-1])

    result += (num1 * num2)
    
print(result)