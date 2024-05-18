# 9. Palindrome Number
# URL: https://leetcode.com/problems/palindrome-number/


class Solution(object):
    def isPalindrome(self, x):
        x = str(x)

        for i in range(len(x) // 2):
            print(x[i])
            if x[i] != x[len(x) - i - 1]:
                return False

        return True
