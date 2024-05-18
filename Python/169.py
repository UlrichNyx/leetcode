# 169. Majority Element
# URL: https://leetcode.com/problems/majority-element/

from collections import Counter


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counter = Counter(nums)
        return counter.most_common(1)[0][0]
