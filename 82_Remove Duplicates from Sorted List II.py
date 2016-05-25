"""
Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

For example,
Given 1->2->3->3->4->4->5, return 1->2->5.
Given 1->1->1->2->3, return 2->3.

"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None



"""
S : 
 还是 和83 一样删除，为方便加头结点.
  依次遍历, 跳过重复元素, 遇到合适的 add
  
"""
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        my_head = ListNode(0) # head
        p = my_head

        while head:
            if head.next==None or head.val != head.next.val: #add
                tmp = head
                head = head.next
                tmp.next = p.next
                p.next = tmp
                p = p.next
            else:  # 重复
                my_val = head.val
                while head and head.val ==my_val:
                    head = head.next
        return my_head.next





if __name__ == "__main__":
    l1 = ListNode(1)
    #l1.next = ListNode(2)
    #l1.next.next=ListNode(2)
    #l1.next.next.next=ListNode(3)
    #l1.next.next.next.next=ListNode(4)
    s = Solution()
    r = s.deleteDuplicates(no)
    while r:
       print(r.val)
       r = r.next






"""
Q :  删除重复数字， 重复数字不保留

"""