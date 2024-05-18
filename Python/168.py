# 168. Excel Sheet Column Title
# URL: https://leetcode.com/problems/excel-sheet-column-title/


class Solution(object):
    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        result = ""
        while columnNumber > 0:
            result = alphabet[(columnNumber - 1) % 26] + result
            columnNumber = (columnNumber - 1) // 26
        return result
