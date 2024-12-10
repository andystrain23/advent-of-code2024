# day 1 part 1 begins here
# the task is to find the distance between two lists once they've been sorted

# initialise value
total_distance = 0

#read the values from the input into a lines variable
with open("day1/input", "r") as f:
    lines = f.readlines()

list_a = []
list_b = []

#split the values between two lists
for line in lines:
    parts = line.split()
    list_a.append(parts[0])
    list_b.append(parts[1])
        

# return the sorted lists to work with
sorted_a = sorted(list_a)
sorted_b = sorted(list_b)

# for each value in the list, get its counterpart, work out which is bigger, and then subtract the smaller to find the distance
for x in range(len(sorted_a)):
    if int(sorted_a[x]) > int(sorted_b[x]):
        distance = int(sorted_a[x]) - int(sorted_b[x])
    else:
        distance = int(sorted_b[x]) - int(sorted_a[x])
    total_distance += distance


# part 2 starts here
# task is to find how similar the two lists are. take each number in one list, find how many times it appears in the other, and then multiply by that number. big number means similar
total_similarity_score = 0

for number in sorted_a:
    similarity_score = int(number) * sorted_b.count(number)
    total_similarity_score += similarity_score
    

print(total_distance)
print(total_similarity_score)