"""
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        header = ListNode(0)
        p = header

        while l1 and l2:
            if l1.val< l2.val:
                tmp = l1
                l1 =l1.next
            else:
                tmp = l2
                l2 = l2.next
            p.next = tmp
            p = p.next
        if l1 ==None :
            l1 = l2
        p.next = l1
        return header.next

