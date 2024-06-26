# 191. Number of 1 Bits
# URL: https://leetcode.com/problems/number-of-1-bits/


def func(n):
    result = 1
    for x in str(n):
        print(n >> 1)
        n >>= 1


func(11)
