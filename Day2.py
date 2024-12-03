def get_file_data(file_name):
    f = open(file_name)
    data = []
    for line in f:
        data.append(line.rstrip())
    return data

input = get_file_data("Input.txt")

# Part 1
counter = 0
for i in range(len(input)):
    inc = True
    dec = True
    adj = True
    split = input[i].split(" ")
    for j in range(len(split) - 1):
        if (int(split[j]) > int(split[j + 1])):
            inc = False
        if (int(split[j]) < int(split[j + 1])):
            dec = False
        diff = abs(int(split[j]) - int(split[j + 1]))
        if (diff < 1 or diff > 3):
            adj = False
    safe = (inc or dec) and adj
    if (safe):
        counter += 1
print(counter)

# Part 2
counter = 0
for i in range(len(input)):
    inc = True
    dec = True
    adj = True
    split = input[i].split(" ")
    for j in range(len(split) - 1):
        if (int(split[j]) > int(split[j + 1])):
            inc = False
        if (int(split[j]) < int(split[j + 1])):
            dec = False
        diff = abs(int(split[j]) - int(split[j + 1]))
        if (diff < 1 or diff > 3):
            adj = False
    safe = (inc or dec) and adj
    if (not safe):
        for k in range(len(split)):
            temp = split.pop(k)
            temp_list = split
            inc = True
            dec = True
            adj = True
            for l in range(len(temp_list) - 1):
                if (int(temp_list[l]) > int(temp_list[l + 1])):
                    inc = False
                if (int(temp_list[l]) < int(temp_list[l + 1])):
                    dec = False
                diff = abs(int(temp_list[l]) - int(temp_list[l + 1]))
                if (diff < 1 or diff > 3):
                    adj = False
            safe = (inc or dec) and adj
            split.insert(k, temp)
            if (safe):
                break
    if (safe):
        counter += 1
print(counter)