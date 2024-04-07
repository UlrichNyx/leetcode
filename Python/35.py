# 35. Search Insert Position
# URL: https://leetcode.com/problems/search-insert-position/

class Solution(object):
    def searchInsert(self, nums, target):
        for x in range(len(nums)):
            if target <= nums[x]:
                return x
        return len(nums)
        