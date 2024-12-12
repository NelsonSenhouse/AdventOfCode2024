def get_data(file_name):
    f = open(file_name)
    data = []
    for line in f:
        data.append(line.rstrip())
    return data

def evaluate(list, indx, start_list, nums_list, target):
    print(list)
    print(indx)
    print(nums_list)
    print(target)
    for num in start_list:
        nums_list.append(num * list[indx + 1])
        nums_list.append(num + list[indx + 1])
    if (indx == len(list) - 2):
        print("done")
        return nums_list
    start_list = nums_list
    #
    # if (indx == len(list) - 2):
    #     print("done")
    #     return nums_list

    return evaluate(list, indx + 1, [2, 3], nums_list, target)



nums = [1, 2, 3]
print(evaluate(nums, 0, [nums[0]], [], 2))

# input = get_data("Input.txt")
# test = []
# ops = []
# op_nums = []
# for data in input:
#     test.append(int(data.split(":")[0]))
#     ops.append(data.split(":")[1][1:len(data.split(":")[1])])
# for op in ops:
#     op_nums.append(op.split(" "))
# for i in range(len(op_nums)):
#     for j in range(len(op_nums[i])):
#         op_nums[i][j] = int(op_nums[i][j])
# print(test)
# print(op_nums)

