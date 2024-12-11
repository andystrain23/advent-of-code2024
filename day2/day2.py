with open("day2/input", "r") as f:
    rows_in = f.readlines()

rows = [x.split() for x in rows_in] 

safe = 0


# to be honest I copied this off someone and rewrote it out but I understand it
# I just wish I had come up with it. I tried for 2 hours to unstick what I wrote.
for row in rows:
    # find the diffs, don't care about the +ve or -ve yet
    diffs = [int(row[a + 1]) - int(row[a]) for a in range(len(row) - 1)]

    # this one is complex. here we go.
    # all determines if all values are true, if not it returns false
    # so in this case it is checking if all values are negative (x < 0) and that all values are within the range needed
    if all(x < 0 and x in range(-3, 0) for x in diffs) or all(x > 0 and x in range(1, 4) for x in diffs):
        safe += 1

print(safe)
