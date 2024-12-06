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
    maze.append(row)



for i in range(len(maze)):
    for j in range(len(maze[i])):
        indx = find_guard(maze)
        while (maze[indx[0] - 1][indx[1]] != "#"):
            maze[indx[0] - 1] = str(maze[indx[0] - 1:indx[1]]) + "^" + str(maze[indx[1] + 1:len(maze[indx[0]])])
            # maze[indx[0]][indx[1]:indx[1] + 1] = "X"
            indx = find_guard(maze)


for row in maze:
    print(row)