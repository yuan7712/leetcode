"""
Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You must do this in-place without altering the nodes' values.

For example,
Given {1,2,3,4}, reorder it to {1,4,2,3}.

"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        # 判断none  return
        if not head :
            return
        # 计数
        list_len = 0
        p = head
        while p : 
            list_len +=1
            p = p.next
        # 分段
        p = head
        i = 1 
        while i < (list_len+1)//2:   #数前一半,记住将前一半最后一个next置为none
            p = p.next
            i +=1
        tmp = p
        p = p.next
        tmp.next = None
        # p 指向了剩余的开头
        my_head = ListNode(0)  #head 指向后半部分
        while p : 
            tmp = p
            p = p.next
            tmp.next = my_head.next
            my_head.next = tmp
        # 合并
        p , q = head , my_head.next
        while q :
            tmp = q
            q = q.next
            tmp.next = p.next
            p.next = tmp
            p = tmp.next

        return head







if __name__ == "__main__":
    l1 = ListNode(1)
    l1.next = ListNode(2)
    l1.next.next=ListNode(3)
    l1.next.next.next=ListNode(4)
    s = Solution()
    r = s.reorderList(None)
    while r:
       print(r.val)
       r = r.next





"""
Q : 题目是要讲1-2-3-4-5-6 =>    1-6-2-5-3-4  

    1. 遍历求长度，将前后两部分 拆分 再次组合。

"""