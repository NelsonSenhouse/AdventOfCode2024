def get_data(file_name):
    f = open(file_name)
    data = []
    for line in f:
        data.append(line.rstrip())
    return data


def find_trailheads(list, row, col, sum):
    if (row > 0):
        if (list[row - 1][col] == list[row][col] + 1):
            if (list[row - 1][col] == 9):
                print("found up")
                sum += 1
                # return True
            else:
                find_trailheads(list, row - 1, col, sum)
    if (row < len(list) - 1):
        if (list[row + 1][col] == list[row][col] + 1):
            if (list[row + 1][col] == 9):
                print("found down")
                sum += 1
                # return True
            else:
                find_trailheads(list, row + 1, col, sum)
    return sum


nums = [[9],
        [8],
        [7],
        [6],
        [5],
        [4],
        [3],
        [2],
        [1],
        [0],
        [1],
        [2],
        [3],
        [4],
        [5],
        [6],
        [7],
        [8],
        [9]]
print(find_trailheads(nums, 9, 0, 0))



text = get_data("Input.txt")
twoD = []
for row in text:
    list = []
    for num in row:
        list.append(num)
    twoD.append(list)

for row in twoD:
    print(row)

