# 21. Merge Two Sorted Lists
# URL: https://leetcode.com/problems/merge-two-sorted-lists/description/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        root = ListNode()
        traverse = ListNode()
        root.next = traverse
        while not list1 is None or not list2 is None:
            if list1 is None:
                traverse.next = ListNode(list2.val, None)
                list2 = list2.next
            elif list2 is None:
                traverse.next = ListNode(list1.val, None)
                list1 = list1.next
            else:
                traverse.next = ListNode(min(list1.val, list2.val), None)
                if list1.val <= list2.val:
                    list1 = list1.next
                else:
                    list2 = list2.next
            traverse = traverse.next
        return root.next.next
        