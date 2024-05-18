# 119. Pascal's Triangle II
# URL: https://leetcode.com/problems/pascals-triangle-ii/


class Solution(object):
    def getRow(self, rowIndex):
        if rowIndex == 0:
            return [1]
        previous_values = self.getRow(rowIndex - 1)
        values = [1]
        for x in range(1, rowIndex):
            values.append(previous_values[x - 1] + previous_values[x])
        values.append(1)
        return values
