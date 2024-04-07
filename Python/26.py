# 26. Remove Duplicates from Sorted Array
# URL: https://leetcode.com/problems/remove-duplicates-from-sorted-array/

class Solution(object):
    def removeDuplicates(self, nums):
        freq = {}
        res = []
        for x in nums:
            if x not in freq:
                freq[x] = 1
                res.append(int(x))
        for x in range(len(res)):
            nums[x] = res[x]
        return len(res)
        