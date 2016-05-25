"""
Given a linked list, determine if it has a cycle in it.

Follow up:
Can you solve it without using extra space?
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

"""
S1 :
        o(n^2)
Error : 超时
"""
class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head :
            return False
        p = head

        while p.next :    #判断该点next是否在之前出现
            if p.next == p:  #
                return True 
            q = head
            while q!=p: 
                if q == p.next: 
                    return True
                q = q.next
            p = p.next

        return False




"""
S2 :
     Accept ;
     使用dict; 将对象作为了dict的key 

O : 
    python 中要求dict的key是可哈希的； 而所有自定义的类（use-defined class）对象都是可哈希的（hashable）
    [Note->dict]
"""
class Solution2(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return False
        my_dict = {}
        p = head
        while p.next : 
            my_dict[p] = 1
            if my_dict.get(p.next,0) :   #exict
                return True
            p = p.next
        return False




"""
S3 :  优
    使用 fast slow 两个指针，

    1. fast 在slow 之前， 当fast到达末尾即无环。(fast 两步 slow 一步)
    2. 如果存在环， 当slow 和fast 都进入环时， fast 必定会和slow 相遇，(fast 相对slow速度为1)
"""
class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head : 
            return False
        fast ,slow = head , head
        # 
        while fast.next and fast.next.next :   #slow必定在fast之后
            slow = slow.next 
            fast = fast.next.next
            if fast == slow :
                return True
        return False



if __name__ == "__main__":
    l1 = ListNode(1)
    l1.next = ListNode(2)
    l1.next.next=ListNode(3)
    l1.next.next.next = l1.next
    s = Solution()
    r = s.hasCycle(l1)
    print(r)










"""
Q: 
     要判断链表是否循环。
     1. o(n^2), 最慢， 依次遍历每个node, 观察之前的是否==next
     2. 判断重复 使用hashmap ;  查看next时 看dict 中是否存在；
        Q : python 中 自定义的类是否可以作为 dict 的key 
        A :  yes
     3.  设置两个指针  slow fast ; fast 走两步slow走一步， 如果有环存在，二者必定会相等

        当存在环时，fast  和slow 都进入环时，fast 相对于slow 为一步速度，必定会相遇


R : 
    http://blog.csdn.net/v_july_v/article/details/6447013 
    http://www.cnblogs.com/wuyuegb2312/p/3183214.html
    http://www.cnblogs.com/hiddenfox/p/3408931.html

"""