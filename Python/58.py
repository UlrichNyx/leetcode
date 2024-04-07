# 58. Length of Last Word
# URL: https://leetcode.com/problems/length-of-last-word/


class Solution(object):
    def lengthOfLastWord(self, s):
        length = 0
        word_encountered = False
        for x in range(len(s) - 1, -1, -1):
            if s[x] == ' ' and word_encountered:
                return length
            elif not s[x] == ' ':
                word_encountered = True
                length += 1
        return length
        