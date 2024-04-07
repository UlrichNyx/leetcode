# 20. Valid Parentheses
# URL: https://leetcode.com/problems/valid-parentheses/description/

class Solution(object):
    def isValid(self, s):
        mapping = {
            "(": None,
             ")":"(",
        "[":None, "]":"[",
        "{":None, "}":"{"}
        open_brackets = []
        for x in s:
            if mapping[x] is None:
                open_brackets.append(x)
            else:
                if len(open_brackets) == 0 or mapping[x] != open_brackets.pop():
                    return False
        return len(open_brackets) == 0