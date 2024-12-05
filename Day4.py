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


# Part 1
def right(list, row, col,):
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


def up(list, row, col):
    if (list[row - 1][col] == "M"):
        if (list[row - 2][col] == "A"):
            if (list[row - 3][col] == "S"):
                return True
    return False


def down(list, row, col):
    if (list[row + 1][col] == "M"):
        if (list[row + 2][col] == "A"):
            if (list[row + 3][col] == "S"):
                return True
    return False


def up_right(list, row, col):
    if (list[row - 1][col + 1] == "M"):
        if (list[row - 2][col + 2] == "A"):
            if (list[row - 3][col + 3] == "S"):
                return True
    return False


def up_left(list, row, col):
    if (list[row - 1][col - 1] == "M"):
        if (list[row - 2][col - 2] == "A"):
            if (list[row - 3][col - 3] == "S"):
                return True
    return False


def down_right(list, row, col):
    if (list[row + 1][col + 1] == "M"):
        if (list[row + 2][col + 2] == "A"):
            if (list[row + 3][col + 3] == "S"):
                return True
    return False


def down_left(list, row, col):
    if (list[row + 1][col - 1] == "M"):
        if (list[row + 2][col - 2] == "A"):
            if (list[row + 3][col - 3] == "S"):
                return True
    return False

sum = 0

for i in range(len(grid)):
    for j in range(len(grid[i])):
        if (grid[i][j] == "X"):
            if (j <= len(grid[i]) - 4):
                if (right(grid, i, j)):
                    sum += 1
            if (j >= 3):
                if (left(grid, i, j)):
                    sum += 1
            if (i >= 3):
                if (up(grid, i, j)):
                    sum += 1
                if (j <= len(grid[i]) - 4):
                    if (up_right(grid, i, j)):
                        sum += 1
                if (j >= 3):
                    if (up_left(grid, i, j)):
                        sum += 1
            if (i <= len(grid) - 4):
                if (down(grid, i, j)):
                    sum += 1
                if (j <= len(grid[i]) - 4):
                    if (down_right(grid, i, j)):
                        sum += 1
                if (j >= 3):
                    if (down_left(grid, i, j)):
                        sum += 1

print(sum)

#Part 2
sum = 0

for i in range(len(grid)):
    for j in range(len(grid[i])):
        if (grid[i][j] == "A"):
            if (i > 0 and i < len(grid) - 1 and j > 0 and j < len(grid[i]) - 1):
                if (grid[i - 1][j - 1] == "M" and grid[i - 1][j + 1] == "M"):
                    if (grid[i + 1][j - 1] == "S" and grid[i + 1][j + 1] == "S"):
                        sum += 1
                if (grid[i - 1][j - 1] == "M" and grid[i + 1][j - 1] == "M"):
                    if (grid[i - 1][j + 1] == "S" and grid[i + 1][j + 1] == "S"):
                        sum += 1
                if (grid[i + 1][j + 1] == "M" and grid[i - 1][j + 1] == "M"):
                    if (grid[i + 1][j - 1] == "S" and grid[i - 1][j - 1] == "S"):
                        sum += 1
                if (grid[i + 1][j + 1] == "M" and grid[i + 1][j - 1] == "M"):
                    if (grid[i - 1][j + 1] == "S" and grid[i - 1][j - 1] == "S"):
                        sum += 1

print(sum)
