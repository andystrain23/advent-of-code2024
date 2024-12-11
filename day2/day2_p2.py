def check_safe(row):
    diffs = [int(row[a + 1]) - int(row[a]) for a in range(len(row) - 1)]
    if all(x < 0 and x in range(-3, 0) for x in diffs) or all(x > 0 and x in range(1, 4) for x in diffs):
        return True
    return False

with open("day2/input", "r") as f:
    rows_in = f.readlines()

rows = [x.split() for x in rows_in] 

safe = 0

for row in rows:
    if check_safe(row):
        safe += 1
    else:
        for i in range(len(row)):
            copy_of_row = row.copy()
            copy_of_row.pop(i)
            if check_safe(copy_of_row):
                safe += 1
                break


print(safe)