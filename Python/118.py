# 118. Pascal's Triangle
# URL: https://leetcode.com/problems/pascals-triangle/

class Solution(object):
    def generate(self, numRows):
        if(numRows == 1):
            return [[1]]
        previous_values = self.generate(numRows-1)
        values = [1]
        for x in range(1, numRows - 1):
            values.append(previous_values[-1][x-1] + previous_values[-1][x])
        values.append(1)
        return previous_values + [values]
    