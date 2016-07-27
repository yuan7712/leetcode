"""
Sort a linked list using insertion sort.

插入排序 :  每次将一个待排序的记录，按照关键字的带下插入到之前已经排好序的子序列中。

直接插入：边比较边找位置。
折半插入：折半查找位置 + 移动     [顺序存储]
希尔： 改变增量递减->1; 对每次增量保证子序列増序(1+i,1+2i,1+3i);  [顺序存储]

"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


"""
S1: 
    直接插入排序 
    leetcode  TLE [1-4999 递增序列]
    1. 添加tail 判断,如果大于末尾数字 直接add 即可。 
"""
class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        ans =ListNode(-1* (2**31))
        tail = ans
        while head: 
            tmp = head 
            head = head.next
            if tmp.val >= tail.val:
                tail.next = tmp
                tmp.next = None
                tail = tail.next
                continue 

            pre = ans 
            while pre.next and pre.next.val <= tmp.val: 
                pre = pre.next
            tmp.next = pre.next
            pre.next = tmp
        return ans.next

        




