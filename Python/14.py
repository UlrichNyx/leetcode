# 14. Longest Common Prefix
# URL: https://leetcode.com/problems/longest-common-prefix/


class Solution(object):
    def romanToInt(self, s):

        sum = 0
        values = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        last = None

        for x in s:
            if last is not None and values[x] > values[last]:
                sum = sum - values[last] + (values[x] - values[last])
            else:
                sum += values[x]
            last = x
        return sum
