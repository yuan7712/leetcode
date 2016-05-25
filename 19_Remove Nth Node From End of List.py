# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int   Given n will always be valid.
        :rtype: ListNode
        """
        list_l = 0  #链表长度,不带头结点
        tmp = head
        while tmp:
            tmp = tmp.next
            list_l +=1
        h = ListNode(0)  #head
        h . next = head
        tmp = h
        i =0
        while i <list_l - n:
            tmp = tmp.next
            i += 1
        tmp.next = tmp.next.next

        return h.next

    def show (self,head):
        while head.next:
            head = head.next
            print(head.val)



class Solution2:
    # @param {ListNode} head
    # @param {integer} n
    # @return {ListNode}
    def removeNthFromEnd(self, head, n):
        if not head:
            print head
        fast = slow = head
        while fast and n != 0:   #一次遍历，是fast 在slow之前先走n步。slow为要del点得前驱
            fast = fast.next
            n -= 1
        if not fast:  #
            return head.next
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return head




if __name__ == '__main__':
    S = Solution()
    l = ListNode(1)
    l.next = ListNode(2)
    #l.next.next = ListNode(3)
    #l.next.next.next = ListNode(4)
    #S.show(l)
    ss = S.removeNthFromEnd(l,1)
    print(ss)             



"""
Q: 简单的链表操作，删除倒数N个点。不带头结点，此处自己创建head.

S2 ： 
     一次遍历不必首先判断list的长度，设置两个指针，间隔N。 当fast到达末尾时，slow即为所找的点。
"""    