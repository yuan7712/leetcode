"""
Given a list, rotate the list to the right by k places, where k is non-negative.

For example:
Given 1->2->3->4->5->NULL and k = 2,
return 4->5->1->2->3->NULL.

"""



# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x

        self.next = None
"""
Error : 
    题目是向右循环k次； 此解是 将后k个循环到 之前；  k可能> 链表长度。 
    所以需要对k%len(链表) 
"""
class Solution1(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        fast  = slow = head 
        while fast and k!=0:
            fast = fast.next
            k -=1
        # [1] 1 当链表长度正好为<=k 时，此时fast为none, 返回原串即可  error
        # <=k  时 应该返回     
        if not fast: 
            return head

        while fast.next: 
            fast = fast.next
            slow = slow.next

        # slow 指向倒数k个 的pre ; fast 为最后一个数字
        # 1 2 3   4 5
        fast.next = head
        ans = slow.next
        slow.next = None
        return ans


"""
S： 
    注意k 可能> 长度； 所以知道链表长度 循环；
"""
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return None

        head_len = 1
        tmp = head 
        # tmp 最后指向最后一个node
        while tmp.next :
            tmp = tmp.next
            head_len +=1
        if head_len == 1:
            return head

        tmp.next = head
        k %=head_len
        i = 0
        # 向后走len-k步 解链
        while i <head_len-k :
            tmp = tmp.next
            i +=1
        ans = tmp.next
        tmp.next = None
        return ans
        



if __name__ == '__main__':
    S = Solution()
    l = ListNode(1)
    l.next = ListNode(2)
    l.next.next = ListNode(3)
    #l.next.next.next = ListNode(4)
    #l.next.next.next.next = ListNode(5)
    #S.show(l)
    r = S.rotateRight(l,4)
    while r:
       print(r.val)
       r = r.next
   











"""
Q  ：  注意 题目是向右循环k次数，并不是末尾k个前置。所以我们需要遍历获取长度。
    1. 遍历获取长度，形成循环链表
    2. 向后走k 步，解开链表
"""