
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums: return [int]
        dict = {}
        for index in range(len(nums)):
            if dict.has_key(nums[index]): return [dict[nums[index]], index]
            dict[target - nums[index]] = index
        return [int]


solution = Solution()

for index in solution.twoSum([2, 3, 4, 5, 7], 10):
    print index