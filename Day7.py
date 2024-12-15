def get_data(file_name):
    f = open(file_name)
    data = []
    for line in f:
        data.append(line.rstrip())
    return data

def evaluate1(list, indx, start_list, nums_list, target):
    for num in start_list:
        nums_list.append(num * list[indx + 1])
        nums_list.append(num + list[indx + 1])
    new_list = []
    for num in nums_list:
        new_list.append(num)
    if (indx == len(list) - 2):
        answers = []
        for i in range(len(nums_list)):
            if (i >= len(nums_list) - (2 ** (len(list) - 1))):
                answers.append(nums_list[i])
        return (target in answers)
    return evaluate1(list, indx + 1, new_list, nums_list, target)

input = get_data("Input.txt")
test = []
ops = []
op_nums = []
for data in input:
    test.append(int(data.split(":")[0]))
    ops.append(data.split(":")[1][1:len(data.split(":")[1])])
for op in ops:
    op_nums.append(op.split(" "))
for i in range(len(op_nums)):
    for j in range(len(op_nums[i])):
        op_nums[i][j] = int(op_nums[i][j])

sum = 0
for i in range(len(op_nums)):
    if (evaluate1(op_nums[i], 0, [op_nums[i][0]], [], test[i])):
        sum += test[i]
print(sum)

