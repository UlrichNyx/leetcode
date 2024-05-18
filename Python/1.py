# 1. Two Sum
# URL: https://leetcode.com/problems/two-sum/


class Solution(object):
    def twoSum(self, nums, target):
        for i, v in enumerate(nums):
            sum = v
            for index, value in enumerate(nums[i + 1 :]):
                if sum + value == target:
                    return [i, i + index + 1]
        return None
