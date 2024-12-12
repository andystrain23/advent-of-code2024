with open("day4/input", "r") as f:
    challenge_input = f.readlines()

# matrices don't exist in python but you can make a list of lists and it acts kinda the same, not as performant (but it's Python so who cares)
matrix = [list(x.strip()) for x in challenge_input]

# for each row in matrix
for i in range(len(matrix)):
    # for each value in row
    for x in range(len(matrix[i])):
        # check if the character is X
        if matrix[i][x] == "X":
            print(f"[{i}],[{x}]")
            # check in all dimensions if the next letters are 'M', 'A', 'S' in that order

print(matrix[130][52])