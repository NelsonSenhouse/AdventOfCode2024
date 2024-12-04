def get_file_data(file_name):
    f = open(file_name)
    data = []
    for line in f:
        data.append(line.rstrip())
    return data

file_data = get_file_data("Input.txt")

# build a 2D List based on the file_data
grid = []
for line in file_data:
    row = []
    for letter in line:
        row.append(letter)
    grid.append(row)

for row in grid:
    print(row)

def right(list, row, col):
    if (list[row][col + 1] == "M"):
        if (list[row][col + 2] == "A"):
            if (list[row][col + 3] == "S"):
                return True
    return False

def left(list, row, col):
    if (list[row][col - 1] == "M"):
        if (list[row][col - 2] == "A"):
            if (list[row][col - 3] == "S"):
                return True
    return False


for i in range(len(grid)):
    yes = False
    for j in range(len(grid[i])):
        if (grid[i][j] == "X"):
            if (j <= len(grid[i]) - 4):
                if (right(grid, i, j)):
                    yes = True
                    print("Yes")
            if (j >= 3):
                if (left(grid, i, j)):
                    yes = True
                    print("Yes")
