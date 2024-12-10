total_distance = 0

with open("day1/input", "r") as f:
    lines = f.readlines()

list_a = []
list_b = []

for line in lines:
    parts = line.split()
    list_a.append(parts[0])
    list_b.append(parts[1])
        
sorted_a = sorted(list_a)
sorted_b = sorted(list_b)

for x in range(len(sorted_a)):
    if int(sorted_a[x]) > int(sorted_b[x]):
        distance = int(sorted_a[x]) - int(sorted_b[x])
    else:
        distance = int(sorted_b[x]) - int(sorted_a[x])
    total_distance += distance


    

print(total_distance)