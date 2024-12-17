def get_file_data(file_name):
    f = open(file_name)
    data = []
    for line in f:
        data.append(line.rstrip())
    return data

def partOne(list, r, c, r2, c2):
    sum = 0
    rDiff = r - r2
    cDiff = c - c2
    print(str(r + rDiff) + ", " + str(c + cDiff))
    print(str(r - 2 * rDiff) + ", " + str(c - 2 * cDiff))
    if (r + rDiff >= 0 and (c + cDiff < len(list[r]) and c + cDiff >= 0)):
        sum += 1
    if (r - rDiff * 2 < len(list) and c - 2 * cDiff < len(list[r]) and c - 2 * cDiff >= 0):
        sum += 1
    print(sum)
    return sum

file_data = get_file_data("Input")

map = []
for line in file_data:
    row = []
    for letter in line:
        row.append(letter)
    map.append(row)

for row in map:
    print(row)

checked = []
total = 0
for i in range(len(map)):
    for j in range(len(map[i])):
        if (map[i][j] != "."):
            for k in range(len(map)):
                if (k > i):
                    for l in range(len(map[i])):
                        if (map[i][j] == map[k][l] and (i != k or j != l)):
                            # print("Row " + str(k) + ":")
                            total += partOne(map, i, j, k, l)

                            # print(partOne(map, i, j, k, l))
        # checked.append(map[i][j])

print(total)
