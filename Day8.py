def get_file_data(file_name):
    f = open(file_name)
    data = []
    for line in f:
        data.append(line.rstrip())
    return data

def partOne(list, r, c, r2, c2):
    antinodes = []
    rDiff = r - r2
    cDiff = c - c2
    if (r + rDiff >= 0 and (c + cDiff < len(list[r]) and c + cDiff >= 0)):
        antinodes.append((r + rDiff, c + cDiff))
    if (r - 2 * rDiff < len(list) and c - 2 * cDiff < len(list[r]) and c - 2 * cDiff >= 0):
        antinodes.append((r - 2 * rDiff, c - 2 * cDiff))
    return antinodes

def partTwo(list, r, c, r2, c2):
    antinodes = []
    rDiff = r - r2
    cDiff = c - c2
    for i in range(len(list)):
        if (i > 0):
            if (r + i * rDiff >= 0 and (c + i * cDiff < len(list[r]) and c + i * cDiff >= 0)):
                antinodes.append((r + i * rDiff, c + i * cDiff))
        if (i > 1):
            if (r - i * rDiff < len(list) and c - i * cDiff < len(list[r]) and c - i * cDiff >= 0):
                antinodes.append((r - i * rDiff, c - i * cDiff))
    return antinodes

file_data = get_file_data("Input")

map = []
for line in file_data:
    row = []
    for letter in line:
        row.append(letter)
    map.append(row)

for row in map:
    print(row)

print(partTwo(map, 9, 9, 8, 8))

# part one
checked = []
nodes = 0
for i in range(len(map)):
    for j in range(len(map[i])):
        if (map[i][j] != "."):
            for k in range(len(map)):
                if (k > i):
                    for l in range(len(map[i])):
                        if (map[i][j] == map[k][l] and (i != k or j != l)):
                            list = partOne(map, i, j, k ,l)
                            if (len(list) > 0):
                                for tuple in list:
                                    if not (tuple in checked):
                                        checked.append(tuple)

print(len(checked))


# part two
checked = []
total = 0
for i in range(len(map)):
    for j in range(len(map[i])):
        if (map[i][j] != "."):
            for k in range(len(map)):
                if (k > i):
                    for l in range(len(map[i])):
                        if (map[i][j] == map[k][l] and (i != k or j != l)):
                            list = partTwo(map, i, j, k, l)
                            if (len(list) > 0):
                                for tuple in list:
                                    if not (tuple in checked):
                                        checked.append(tuple)
print(len(checked))
