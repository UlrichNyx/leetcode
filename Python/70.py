# 70. Climbing Stairs
# URL: https://leetcode.com/problems/climbing-stairs/description/

class Solution(object):
    def climbStairs(self, n):
        # Base cases
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        # Dynamic programming array
        dp = [0] * (n + 1)
        dp[1], dp[2] = 1, 2
        
        # Calculate the number of ways for each step
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        
        # The last element is the answer
        return dp[n]