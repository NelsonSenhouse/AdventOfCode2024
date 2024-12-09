def get_first_data(file_name):
    f = open(file_name)
    data = []
    for line in f:
        if ("|" in line):
            data.append(line.rstrip().split("|"))
    return data


def get_sec_data(file_name):
    f = open(file_name)
    data = []
    for line in f:
        if ("," in line):
            data.append(line.rstrip().split(","))
    return data


dir = get_first_data("Input.txt")
pgs = get_sec_data("Input.txt")
safe_rows = []
unsafe_rows = []

# Part 1
for i in range(len(pgs)):
    safe = True
    for j in range(len(pgs[i])):
        for k in range(len(dir)):
            for l in range(len(dir[k])):
                if (dir[k][l] == pgs[i][j]):
                    if (l == 0):
                        if (dir[k][1] in pgs[i][0:j]):
                            safe = False
                    else:
                        if (dir[k][0] in pgs[i][j:len(pgs[i])]):
                            safe = False
        if (not safe):
            break
    if (safe):
        safe_rows.append(pgs[i])
    else:
        unsafe_rows.append(pgs[i])

sum = 0
for row in safe_rows:
    sum += int(row[int(len(row) / 2)])
print(sum)

# Part 2
print(unsafe_rows)
for i in range(len(unsafe_rows)):
    for j in range(len(unsafe_rows[i])):
        for k in range(len(dir)):
            for l in range(len(dir[k])):
                if (dir[k][l] == unsafe_rows[i][j]):
                    if (l == 0):
                        if (dir[k][1] in unsafe_rows[i][0:j]):
                            temp = dir[k][1]
                            unsafe_rows[i][unsafe_rows[i].index(dir[k][1])] = unsafe_rows[i][j]
                            unsafe_rows[i][j] = temp
                    else:
                        if (dir[k][0] in unsafe_rows[i][j:len(unsafe_rows[i])]):
                            temp = dir[k][0]
                            unsafe_rows[i][unsafe_rows[i].index(dir[k][0])] = unsafe_rows[i][j]
                            unsafe_rows[i][j] = temp

print(unsafe_rows)
sum = 0
for row in unsafe_rows:
    sum += int(row[int(len(row) / 2)])
print(sum)
