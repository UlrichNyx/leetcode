# 83. Remove Duplicates from Sorted List
# URL: https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        temp = ListNode(val = 0, next = head)
        temp = temp.next
        prev = None

        freq = {}
        while not temp is None:
            print(temp.val)
            if temp.val in freq:
                prev.next = temp.next
            else:
                freq[temp.val] = 1
                prev = temp
            if not temp is None:
                temp = temp.next
        return head
        