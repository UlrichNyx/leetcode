# 171. Excel Sheet Column Number
# URL: https://leetcode.com/problems/excel-sheet-column-number/


class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """
        result = 0
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        for x in range(0, len(columnTitle)):
            result += 26 ** (len(columnTitle) - 1 - x) * (
                alphabet.index(columnTitle[x]) + 1
            )
        return result
