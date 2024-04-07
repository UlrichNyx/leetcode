# 66. Plus One
# URL: https://leetcode.com/problems/plus-one/description/

class Solution(object):
    def plusOne(self, digits):
        leftover = 1
        for x in range(len(digits) - 1, -1, -1):
            if digits[x] + leftover > 9:
                digits[x] = 0
            else:
                digits[x] += 1
                return digits
        return [1] + digits