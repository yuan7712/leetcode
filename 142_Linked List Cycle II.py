"""
Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

Note: Do not modify the linked list.

Follow up:
Can you solve it without using extra space?

"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

"""
s1 : AC  108 ms
     当遇到环时，转化为两个求两个链表交点。
     1. 求两个链表长度
     2. 让长的先走k个单位
     3. p q 同步走，当相遇即 交点

"""
class Solution1(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head :
            return None
        fast ,slow  = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow :   #有环时找第一个node
                p ,q = head,fast.next 
                p_len , q_len = 0 ,0
                while p!=fast: 
                    p_len +=1
                    p = p.next
                while q!=fast:
                    q_len +=1
                    q = q.next
                if q_len > p_len :   #让p 指向长的
                    p , q = fast.next , head
                    p_len , q_len = q_len,p_len
                else :
                    p ,q = head ,fast.next
                while p_len !=q_len:
                    p_len -=1
                    p = p.next
                while p != q: 
                    p = p.next
                    q = q.next

                return p

        return None




"""
S2 :  优  96ms


"""
class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head : 
            return None
        fast ,slow = head , head
        while fast.next and fast.next.next :   #slow必定在fast之后
            slow = slow.next 
            fast = fast.next.next
            if fast == slow :   #设置p q 分别指向head 和slow next
                p ,q = head,fast  #q 应该是从fast 而不是 fast.next开始
                while p!=q:  #始终会相遇在环开始点
                    p = p.next
                    q = q.next
                return p
                
        return None
        









if __name__ == "__main__":
    l1 = ListNode(1)
    l1.next = ListNode(2)
    l1.next.next=ListNode(3)
    l1.next.next.next=ListNode(4)
    l1.next.next.next.next = l1.next
    s = Solution()
    r = s.detectCycle(l1)
    print(r.val)








"""
Q :  
    判断有没有环，午返回null, 有则返回  环起始点；

    1.  使用141 判断有无环，当有环时，在此处seg 分别计算环和head 到此处长度， 转化为两个链表的交点问题

    2. 假设环的长度为r ,当相遇时 slow 走了 k, 则 fast 走了2k ;head 到环起始点为m,则环起始点到第一次相遇点为s = k-m

        2k = k +N*r   (slow 到达时，fast 已经走了N圈)
        m +s = N*r  =>  m = N*r -s =(N-1)*r  +(r-s)
        说明 如果设置两个指针p q 分别指向head 和第一次相遇点
        每次走一步，他们始终会相遇， 因为 m = (r-s)  +(N-1)r 

            基于此 当fast==slow 时候 设置两个指针p q 

    3. Note[wiz]

"""