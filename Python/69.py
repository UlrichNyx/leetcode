# 69. Sqrt(x)
# URL: https://leetcode.com/problems/sqrtx/description/

class Solution(object):
    def mySqrt(self, x):
        if x < 2:
            return x
        
        left, right = 2, x // 2  # Start the binary search range
        
        while left <= right:
            pivot = left + (right - left) // 2
            num = pivot * pivot
            
            if num > x:
                right = pivot - 1
            elif num < x:
                left = pivot + 1
            else:
                return pivot  # Exact square root found
        
        return right  # Floor of the square root
