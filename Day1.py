def get_file_data(file_name):
    f = open(file_name)
    data = []
    for line in f:
        data.append(line.rstrip())
    return data

# Part 1
input = get_file_data("Input.txt")
left = []
right = []
sum = 0

for i in range(len(input)):
    left.append(input[i].split("   ")[0])
    right.append(input[i].split("   ")[1])


left.sort()
right.sort()
for i in range(len(left)):
    sum += abs(int(left[i]) - int(right[i]))
print(sum)

# Part 2
sum = 0
for i in range(len(left)):
    count = 0
    for j in range(len(right)):
        if (int(right[j]) == int(left[i])):
            count += 1
    sum += count

print(sum)