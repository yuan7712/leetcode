"""
Reverse a linked list from position m to n. Do it in-place and in one-pass.

For example:
Given 1->2->3->4->5->NULL, m = 2 and n = 4,

return 1->4->3->2->5->NULL.

Note:
Given m, n satisfy the following condition:
1 ≤ m ≤ n ≤ length of list.
"""



# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


"""
Error
 题目是 m->n  之间的 逆置， 不是 m 和n 逆置
"""
class Solution1(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        my_head = ListNode(0)  #头结点
        my_head.next = head
        if m == n :
            return head

        pre_m ,pre_n = my_head , my_head

        i = 1
        while i < m:
            pre_m = pre_m.next
            i +=1
        pre_n = pre_m
        while i <n :
            pre_n = pre_n.next
            i +=1

        if m +1 == n:   # 1 2 3 4 (2 3 )
            tmp = pre_n.next #3
            pre_n.next = pre_n.next.next
            pre_m.next = tmp
            tmp.next = pre_n
        else :  # 1 2 3 4 5 (2 4)
            m = pre_m.next
            n = pre_n.next
            tmp = n.next
            pre_m.next = n
            n.next = m.next
            pre_n.next = m
            m.next = tmp


        return my_head.next



"""
 S1 : 
  逆置m-n  之间Node 
  1. 找到m 前驱
  2. 将m-n  之间的头插
  3. 记住标记m 点， 最后将m.next  = n 后面的


"""
class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        my_head = ListNode(0)  #head
        my_head.next = head

        if m == n :
            return head
        pre_m = my_head  #m pre
        i = 1 
        while i <m: 
            pre_m = pre_m.next
            i +=1
        last = pre_m.next  #m
        p = last.next
        while i <n :
            tmp = p.next
            p .next = pre_m.next
            pre_m.next =  p
            p = tmp
            i +=1
        last.next = p
        return my_head.next  

        










if __name__ == "__main__":
    l1 = ListNode(1)
    l1.next = ListNode(2)
    l1.next.next=ListNode(3)
    s = Solution()
    r = s.reverseBetween(l1,2,3)
    while r:
       print(r.val)
       r = r.next
