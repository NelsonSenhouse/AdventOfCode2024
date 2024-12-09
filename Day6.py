def get_data(file_name):
    f = open(file_name)
    data = []
    for line in f:
        data.append(line.rstrip())
    return data


def find_guard(list):
    for i in range(len(list)):
        for j in range(len(list[i])):
            if (list[i][j] == "^"):
                return [i, j]


input = get_data("Input.txt")
maze = []
for row in input:
    new_maze = []
    for point in row:
        new_maze.append(point)
    maze.append(new_maze)

# Part 1
up = True
down = False
right = False
left = False
end = False

while (not end):
    if (up):
        indx = find_guard(maze)
        while (not end and maze[indx[0] - 1][indx[1]] != "#"):
            maze[indx[0] - 1][indx[1]] = "^"
            maze[indx[0]][indx[1]] = "X"
            indx = find_guard(maze)
            # for row in maze:
            #     print(row)
            # print("")
            if (indx[0] == 0):
                end = True
        up = False
        right = True
    if (right):
        indx = find_guard(maze)
        while (not end and maze[indx[0]][indx[1] + 1] != "#"):
            maze[indx[0]][indx[1] + 1] = "^"
            maze[indx[0]][indx[1]] = "X"
            indx = find_guard(maze)
            # for row in maze:
            #     print(row)
            # print("")
            if (indx[1] == len(maze[0]) - 1):
                end = True
        right = False
        down = True
    if (down):
        indx = find_guard(maze)
        while (not end and maze[indx[0] + 1][indx[1]] != "#"):
            maze[indx[0] + 1][indx[1]] = "^"
            maze[indx[0]][indx[1]] = "X"
            # for row in maze:
            #     print(row)
            # print("")
            indx = find_guard(maze)
            if (indx[0] == len(maze) - 1):
                end = True
        down = False
        left = True
    if (left):
        indx = find_guard(maze)
        while (not end and maze[indx[0]][indx[1] - 1] != "#"):
            maze[indx[0]][indx[1] - 1] = "^"
            maze[indx[0]][indx[1]] = "X"
            indx = find_guard(maze)
            # for row in maze:
            #     print(row)
            # print("")
            if (indx[1] == 0):
                end = True
        left = False
        up = True

for i in range(len(maze)):
    print(str(i) + str(maze[i]))
print("")
sum = 0
for row in maze:
    for point in row:
        if (point == "X" or point == "^"):
            sum += 1
print(sum)
