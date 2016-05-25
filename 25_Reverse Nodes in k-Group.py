"""
Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

You may not alter the values in the nodes, only nodes itself may be changed.

Only constant memory is allowed.

For example,
Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5

"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        my_head = ListNode(0) #head
        p  = my_head  #p游标指向末尾
        while  head:
            last = head   # 当add k 后p 指向此处
            i = k
            # add k ge
            while head and i >0 :
                tmp = head.next
                head.next = p.next
                p.next = head
                head = tmp
                i -=1
            if i >0 : #不够k个;k=4  p -> 4 3 2
                now = p.next  #432逆序
                p.next = None
                while  now :
                    tmp = now.next
                    now.next = p.next
                    p.next = now 
                    now = tmp
                return my_head.next
            else : 
                p = last
        return my_head.next






if __name__ == "__main__":
    l1 = ListNode(1)
    l1.next = ListNode(2)
    l1.next.next=ListNode(3)
    l1.next.next.next=ListNode(4)
    s = Solution()
    r = s.reverseKGroup(l1,2)
    while r:
       print(r.val)
       r = r.next












"""
Q: 
     此题是对24题目的变形，24是k=2, 而此处是指定k

     1. add head
     2. 每次添加k个 长度反串， 头插； 当发现不够k时，将此次的add的反串 逆置， return 即可


S2： 
    使用递归。 [1,2,3,4,5,6,7,8,9] k=4

    def (head ,k): 
        1. 计数k 个node , 如果小于k个 返回head
        2. ==k个，逆置4个 last.next = def(head ,k) 
            返回head 
"""