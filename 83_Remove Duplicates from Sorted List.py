"""
Given a sorted linked list, delete all duplicates such that each element appear only once.

For example,
Given 1->1->2, return 1->2.
Given 1->1->2->3->3, return 1->2->3.

"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head : 
            return None
        p = head.next
        pre = head
        pre.next = None 
        
        #  只需将不同元素 挂到pre即可
        while p :
            tmp =p.next
            if p.val != pre.val: 
                p.next = pre.next
                pre.next = p
                pre = pre.next
            p = tmp

        return head







if __name__ == "__main__":
    l1 = ListNode(1)
    l1.next = ListNode(2)
    l1.next.next=ListNode(2)
    l1.next.next.next=ListNode(3)
    s = Solution()
    r = s.deleteDuplicates(l1)
    while r:
       print(r.val)
       r = r.next









"""
Q :  从有序链表中删除重复元素
    1. 从第二个元素开始即可。
    2. 将head后置为none,  依次遍历与head 的最后一个比较， 不一样则入尾
"""