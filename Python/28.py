# 28. Find the Index of the First Occurrence in a String
# URL: https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/

class Solution(object):
    def strStr(self, haystack, needle):
        # Step 1: Check for an empty needle
            if not needle:
                return 0

            # Step 2: Iterate through haystack
            for i in range(len(haystack) - len(needle) + 1):
                # Step 3: Check if the substring from current position matches the needle
                if haystack[i:i+len(needle)] == needle:
                    return i

            # Step 4: Needle not found
            return -1
        