from datas.classes.Node import Node


# 1. Maximum diff
def getMaxDiff(arr, arr_size):
    max_diff = arr[1] - arr[0]

    for i in range(0, arr_size):
        for j in range(i + 1, arr_size):
            if arr[j] - arr[i] > max_diff:
                max_diff = arr[j] - arr[i]

    return max_diff


arr_diff = [4, 2, 1, 5]
my_diff = getMaxDiff(arr_diff, len(arr_diff))
print(f"1. Maximum diff => {my_diff}")


# 2. Merge 2 array
def merge(arr1, arr2):
    arr = arr1 + arr2
    arr.sort()
    return arr


my_merge = merge([1, 7, 13, 15], [1, 4, 5, 9, 20])
print(f"2. Merge 2 sorted arrays => {my_merge}")


# 3. Tree Format
def printTree(node, file=None, _prefix="", _last=True):
    print(_prefix, "`- " if _last else "|- ", node.value, sep="", file=file)
    _prefix += "   " if _last else "|  "
    child_count = len(node.children)
    for i, child in enumerate(node.children):
        _last = i == (child_count - 1)
        printTree(child, file, _prefix, _last)


tree = Node("A", [
    Node("B"),
    Node("C", [
        Node("D"),
    ]),
    Node("E"),
])
print("3. Node Tree")
printTree(tree)

