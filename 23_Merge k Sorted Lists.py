"""
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

`Hard`
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

"""
S1: 
   与两个链表合并类似，每次从K个中选择min,
    1. 每次讲数值大小相同的一次性选择，下标存入pos, [未超时] ;

"""
class Solution1(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        ans = ListNode(0)  #head
        p = ans
        MAX = 2**31
        while lists:
            MIN = ListNode(MAX)
            pos = []
            for i in range(len(lists)):
                if lists[i] and lists[i].val < MIN.val:
                    MIN = lists[i]
                    pos = [i]
                elif lists[i] and lists[i].val == MIN.val:
                    pos.append(i)
            if not pos :  #pos 存放找到的min值
                break
            for k in pos:
                tmp = lists[k] 
                lists[k] = lists[k].next
                tmp.next = None
                p.next = tmp
                p = p.next
        return ans.next



"""
S2:
   1. 使用标准库，heapq, 堆排序,每次从k个数字中选择min,使用堆排序。

R:  https://discuss.leetcode.com/topic/23140/108ms-python-solution-with-heapq-and-avoid-changing-heap-size
"""

from heapq import heappush, heappop, heapreplace, heapify
class Solution2(object):
    def mergeKLists(self, lists):
        ans = ListNode(0)
        p  = ans
        h = [(n.val,n) for n in lists if n ]
        heapify(h)  #初始化堆
        while h:
            val , n = h[0]  # min
            if n.next == None:
                heappop(h) #del 此列
            else: 
                heapreplace(h,(n.next.val,n.next))
            p.next = n
            p = p.next
        return ans.next





"""
S3:
    使用21. Merge Two Sorted Lists;  归并排序。
    
R： https://discuss.leetcode.com/topic/2780/a-java-solution-based-on-priority-queue/4   
"""
class Solution2(object):
    def mergeKLists(self, lists):
        if len(lists) == 0:
            return None
        while len(lists) >1:
            if len(lists)%2  :
                lists.append(None)
            tmp = []
            for i in range(len(lists)//2):
                a = self.mergeTwoLists(lists[2*i],lists[2*i+1])
                tmp.append(a)
            lists = tmp
        return lists[0]


    def mergeTwoLists(self, l1, l2):
        header = ListNode(0)
        p = header
        while l1 and l2:
            if l1.val< l2.val:
                tmp = l1
                l1 =l1.next
            else:
                tmp = l2
                l2 = l2.next
            p.next = tmp
            p = p.next
        if l1 ==None :
            l1 = l2
        p.next = l1
        return header.next




if __name__ == '__main__':
    S =Solution()
    p1 = ListNode(1)
    p2 = ListNode(2)
    p4 = ListNode(4)
    p3 = ListNode(3)
    p5 = ListNode(5)
    p1.next = p2
    p2.next = p4
    p3.next = p5
    ss = S.mergeKLists([p1,p3])
    print(ss.val)




    
