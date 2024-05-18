# 136. Single Number
# URL: https://leetcode.com/problems/single-number/


class Solution(object):
    def singleNumber(self, nums):
        nums.sort()
        last_val = nums[0]
        for x in range(1, len(nums)):
            if last_val != nums[x] and not last_val is None:
                return last_val
            elif not last_val is None:
                last_val = None
            else:
                last_val = nums[x]
        return last_val
