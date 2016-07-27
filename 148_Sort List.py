"""
Sort a linked list in O(n log n) time using constant space complexity.

"""
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
"""
常数空间&&O(n log n), 单链表适合归并排序.  双向链表适合快排.(取pivot 左右移动即可.)
"""

"""
S1:
    1. 归并排序, 每次讲list 分为两段. 最后合并.
    2. 分段, 找到中间位置. 设置 fast slow 指针, 速度2:1

"""
class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next :   # 0 or 1 
            return head
        fast ,slow = head,head
        while fast.next and fast.next.next:  # center : slow.next
            fast = fast.next.next 
            slow = slow.next

        right = self.sortList(slow.next)
        slow.next = None
        left =  self.sortList(head)
        return self.mergeTwoLists(left,right)

    # merge 两个链表
    def mergeTwoLists(self, l1, l2):
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



"""
S2:
   非递归 
R: https://discuss.leetcode.com/topic/3085/my-o-n-log-n-time-o-1-space-solution/2
"""