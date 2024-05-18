# 125. Valid Palindrome
# URL: https://leetcode.com/problems/valid-palindrome/


class Solution(object):
    def isPalindrome(self, s):
        s = s.lower()
        s = re.sub(r"[^a-zA-Z0-9]", "", s)
        for x in range(0, len(s) / 2):
            if s[x] != s[len(s) - x - 1]:
                return False
        return True
