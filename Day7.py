def get_data(file_name):
    f = open(file_name)
    data = []
    for line in f:
        data.append(line.rstrip())
    return data

def mult_evaluate(list, indx, start, target):
    mult = start * int(list[indx + 1])
    add = start + int(list[indx + 1])
    if (indx == len(list) - 2):
        return (mult == target or add == target)
    return mult_evaluate(list, indx + 1, start, target)

def add_evaluate(list, indx, start, target):
    add = start + int(list[indx + 1])
    if (indx == len(list) - 2):
        print("hello")
        return (add == target)
    return add_evaluate(list, indx + 1, add, target)

nums = [1, 2, 3]
print(mult_evaluate(nums, 0, nums[0], 6))
print(add_evaluate(nums, 0, nums[0], 7))

input = get_data("Input.txt")
test = []
ops = []
op_nums = []
for data in input:
    test.append(data.split(":")[0])
    ops.append(data.split(":")[1][1:len(data.split(":")[1])])
for op in ops:
    op_nums.append(op.split(" "))
print(test)
print(op_nums)

