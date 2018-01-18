def binarySearch(nums, target):
    if not nums: return -1;
    start = 0
    end = len(nums)
    while (start + 1 < end):
        mid = start + (start + end) / 2
        if(nums[mid] == target): return mid
        elif(nums[mid] > target): end = mid
        else: start = mid
    if(nums[start] == target): return mid
    elif (nums[end] == target): return end
    else: return -1


print binarySearch([1, 2, 3, 4, 5], 3)
print binarySearch([1, 2, 4, 5], 3)

import DataStructure
DataStructure.printInfo()
head = DataStructure.TreeNode(3)
head.setLeft(DataStructure.TreeNode(2))
head.setRight(DataStructure.TreeNode(4))
print head.value
print head.left.value
print head.right.value