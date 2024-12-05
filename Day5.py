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
# print(dir)
# print(pgs)
safe_rows = []

for i in range(len(pgs)):
    safe = True
    prev = []
    for j in range(len(pgs[i])):
        for k in range(len(dir)):
            for l in range(len(dir[k])):
                if (dir[k][l] == pgs[i][j]):
                    print(dir[k])
                    if (l == 0):
                        if (dir[k][1] in prev):
                            print("NO")
                            print(pgs[i])
                            safe = False
                            break
                    else:
                        if (dir[k][0] in pgs[i][j:len(pgs[i])]):
                            print("NO")
                            print(pgs[i])
                            safe = False
                            break
        prev.append(pgs[i][j])
        if (safe):
            safe_rows.append(pgs[i])

# print(matches)
print(safe_rows)