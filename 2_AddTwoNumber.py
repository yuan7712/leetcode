# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


"""
S1 : 
 l1 l2 对应相加， 当其中任意一个为空 break; 然后继续将后续 非空串add
"""

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        rtype = ListNode(0)  #head
        r = rtype
        pre = 0 #carry
        while l1 and l2  :
            sum = l1.val+l2.val+pre
            pre = 0           
            if sum >9:
                sum -= 10
                pre = 1
            r.next = ListNode(sum)
            r = r.next
            l1 = l1.next
            l2 = l2.next
        if not l1 and not l2:
            if pre:
                r.next = ListNode(pre)
            return rtype.next
        if l1:
            l2= l1
        while l2:
            sum = pre + l2.val
            pre = 0
            if sum >9:
                sum -= 10
                pre = 1
            r.next = ListNode(sum)
            r = r.next
            l2 = l2.next
            if pre:
                r.next = ListNode(pre)
        return rtype.next


"""
S2: 
 与S1 相比较简洁。 将l1 l2 中对应数字相加 分为分别相加， 这样的话就不必考虑 l1 和l2 同时为非空。
"""
class Solution2:
    # @return a ListNode
    def addTwoNumbers(self, l1, l2):
        head = ListNode(0)
        l = head
        carry = 0
        while l1 or l2 or carry:   #last carry  也可单独判断
            sum, carry = carry, 0
            if l1:
                sum += l1.val
                l1 = l1.next
            if l2:
                sum += l2.val
                l2 = l2.next
            if sum > 9:
                carry = 1
                sum -= 10
            l.next = ListNode(sum)
            l = l.next
        return head.next





if __name__ == "__main__":
    l1 = ListNode(9)
    #l1.next = ListNode(4)
    #l1.next.next=None
    l2 = ListNode(9)
    l2.next = ListNode(1)
    #l2.next = ListNode(4)
    #l2.next.next=None
    s = Solution()
    r = s.addTwoNumbers(l1,l2)
    while r:
       print(r.val)
       r = r.next