# 67. Add Binary
# URL: https://leetcode.com/problems/add-binary/description/

class Solution(object):
    def addBinary(self, a, b):
        if len(b) > len(a):
            a, b = b, a
        b = b.zfill(len(a))
        leftover = 0
        result = ''
        for x in range(len(a) -1, -1, -1):
            total_sum = leftover
            total_sum += int(a[x]) + int(b[x])
            leftover = 1 if total_sum > 1 else 0
            result = str(total_sum % 2) + result
        return "1" + result if leftover > 0 else result
        