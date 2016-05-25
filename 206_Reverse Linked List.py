"""
Reverse a singly linked list.

click to show more hints.

Hint:
A linked list can be reversed either iteratively or recursively. Could you implement both?
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


"""
S1 : 
链表逆置，  头插即可。 为方便操作 创建头结点my_head
"""
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head :  #空 返回
            return 
        my_head = ListNode(0)
        p = head
        # 头插
        while p : 
            tmp = p.next
            p.next = my_head.next
            my_head.next = p
            p = tmp

        return my_head.next


"""
S2  : 
 递归操作 

 1-2-3-4 

  保留1 操作234 -> 432 返回4 ; 当前1 仍然指向2 ，修改2->1  1->none 即可

"""

class Solution2(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        def my_reverse(head):
            if  not head.next :  # 当最后一个时返回
                return head
            tmp = my_reverse(head.next)
            head.next.next=head
            head.next = None
            return tmp

        if not head : 
            return None
        
        return  my_reverse(head)










if __name__ == '__main__':
    S = Solution2()
    l1 = ListNode(1)
    l1.next = ListNode(2)
    r = S.reverseList(l1)
    while r:
        print(r.val)
        r = r.next