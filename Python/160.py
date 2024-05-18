# 160. Intersection of Two Linked Lists
# URL: https://leetcode.com/problems/intersection-of-two-linked-lists/


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        # Find longer node and check difference in lengths
        lenA = self.getLength(headA)
        lenB = self.getLength(headB)

        diff = abs(lenA - lenB)
        # We need to equalize the lists in length
        if lenA > lenB:
            headA = self.equalizeLists(headA, diff)
        else:
            headB = self.equalizeLists(headB, diff)
        # Now that they are at the same length, the condition can be checked
        intersection = None
        flag = False
        while not headA is None and not headB is None:
            if not flag and headA == headB:
                intersection = headA
                flag = True
            elif flag and headA != headB:
                intersection = None
                flag = False
            headA = headA.next
            headB = headB.next
        return intersection

    def equalizeLists(self, nlist, diff):
        while diff > 0:
            nlist = nlist.next
            diff -= 1
        return nlist

    def getLength(self, nlist):
        iterN = nlist
        lenN = 0
        while not iterN is None:
            lenN += 1
            iterN = iterN.next
        return lenN
