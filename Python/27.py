# 27. Remove Element
# URL: https://leetcode.com/problems/remove-element/


class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        res = []
        for x in nums:
            if x == val:
                continue
            else:
                res.append(x)

        for x in range(len(res)):
            nums[x] = res[x]
        return len(res)
