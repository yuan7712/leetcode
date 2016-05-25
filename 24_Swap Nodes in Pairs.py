"""
Given a linked list, swap every two adjacent nodes and return its head.

For example,
Given 1->2->3->4, you should return the list as 2->1->4->3.

Your algorithm should use only constant space. You may not modify the values in the list, only nodes itself can be changed.

"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

"""
S : 
      添加head 方便操作。一组一组add新的list 中；
      注意 : 最后添加上 单个node
"""
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        my_head = ListNode(0)
        p = my_head

        while head and head.next:   #两个一组
            p_1 = head
            p_2 = head.next
            head = p_2.next #转向下一组

            p_2.next=p_1
            p.next = p_2
            p = p_1  # 指向末尾。最后置 后继none

        if head : # 单数个 添加末尾
            p.next = head
        else:
            p.next = None

        return my_head.next





if __name__ == "__main__":
    l1 = ListNode(1)
    l1.next = ListNode(2)
    l1.next.next=ListNode(3)
    #l1.next.next.next=ListNode(4)
    s = Solution()
    r = s.swapPairs(l1)
    while r:
       print(r.val)
       r = r.next









"""
Q :  交换链表 相邻的每两个元素， 剩余1个时 不管
"""