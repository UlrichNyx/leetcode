# 88. Merge Sorted Array
# URL: https://leetcode.com/problems/merge-sorted-array/


class Solution(object):
    def replace_tail(self, nums1, n):
        for x in range(len(nums1) - 1, len(nums1) - n - 1, -1):
            if nums1[x] == 0:
                nums1[x] = None
            else:
                return

    def pushback(self, nums1, index, value):
        previous = nums1[index]
        nums1[index] = value
        for x in range(index + 1, len(nums1)):
            temp = nums1[x]
            nums1[x] = previous
            previous = temp

    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """

        pivot1 = 0
        pivot2 = 0

        self.replace_tail(nums1, n)
        while pivot2 < n:
            print(nums1)
            if nums1[pivot1] is None:
                print("It was None")
                self.pushback(nums1, pivot1, nums2[pivot2])
                pivot2 += 1
                pivot1 += 1
            elif nums1[pivot1] < nums2[pivot2]:
                print("Pivot1")
                pivot1 += 1
                continue
            else:
                print("Pivot2")
                self.pushback(nums1, pivot1, nums2[pivot2])
                pivot2 += 1
                pivot1 += 1
