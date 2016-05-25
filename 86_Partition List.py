"""
Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

For example,
Given 1->4->3->2->5->2 and x = 3,
return 1->2->2->4->3->5.

"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


"""
S1 : 
    1.  分别将<x  和>= x 的设置两个链表，依次遍历 填充
    2.  最后连接。保证原来顺序不变，之前 尾插
"""
class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        min_head , max_head = ListNode(0),ListNode(0)
        min_p ,max_p = min_head , max_head
        # 尾插
        while head : 
            tmp = head.next
            if head.val <x: 
                head.next = min_p.next
                min_p.next = head
                min_p = min_p.next
            else: 
                head.next = max_p.next
                max_p.next = head
                max_p = max_p.next
            head = tmp

        min_p.next = max_head.next  #连接两个链表 
        return min_head.next


"""
T : 
  while 内部也不必每次修改head的next,因为min_p max_p  始终指向最后node; 循环后 只要将max_head   后继置为none 即可。 min_p 后继连接max_head

  while head:
        if head.val<x:
            p1.next=head
            p1=p1.next
        else:
            p2.next=head
            p2=p2.next
        head=head.next
    #join the lists
    p2.next=None
    p1.next=hd2.next
"""





if __name__ == "__main__":
    l1 = ListNode(1)
    l1.next = ListNode(4)
    l1.next.next=ListNode(3)
    l1.next.next.next=ListNode(2)
    l1.next.next.next.next=ListNode(5)
    l1.next.next.next.next.next=ListNode(2)
    s = Solution()
    r = s.partition(l1,3)
    while r:
       print(r.val)
       r = r.next

















"""
Q  :  
     题目要求将链表中<X 的数字放到前面，>=x 的数字放到后面。 原来的顺序保持不变。
      1->4->3->2->5->2  X =3 
      < 3  : 1 2 2   >=3 4 3 5 

      所以可以设置两个链表表示 <  >=  最后连接

"""