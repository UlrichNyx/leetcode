# 141. Linked List Cycle
# URL: https://leetcode.com/problems/linked-list-cycle/


class Solution(object):
    def hasCycle(self, head):
        if head is None:
            return False
        turt = head
        hare = head.next

        while not turt is None and not hare is None:
            if hare == turt:
                return True
            try:
                turt = turt.next
                hare = hare.next.next
            except AttributeError:
                return False
        return False
