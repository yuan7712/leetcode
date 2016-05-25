"""
A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

Return a deep copy of the list.

"""



# Definition for singly-linked list with a random pointer.
class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None



"""
Error : 
    题目理解不对；对random 指向理解不对 
    此题实现的是对链表的深度复制，random 指向新的node, 
        所以使用递归，依次复制.

"""
class Solution1(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """

        def my_copy(head):
            if not head : 
                return None

            my_head = RandomListNode(0)  #head
            p  = my_head #末尾

            while head :
                tmp = RandomListNode(head.label) #copy
                tmp.random = my_copy(head.random)
                p.next = tmp
                p = p.next
                head = head.next

            p.next = None
            return my_head.next


        ans = my_copy(head)
        return ans


# 递归输出
    def my_show(head):
        if not head :
            print("None")
        while head:
            my_show(head.random)
            print(head.label)
            head = head.next






"""
S:
    1->2(4)->3(2)->4(None)->5     [()中表示random的值，代表指向该list某一个点] 
    目标： copy 此list;  (包括random 中的指向)

    3件事 分配新的node   node见val和next   node的random

    1. 1 2 3 4 5  变为 1 1 2 2 3 3 4 4 5 5 
    2. copy random (这样才比较对random值好 定位)
    3. 拆分list 


T : 注意 ： 原来串的顺序不能变，所以拆分串时要注意保留原串样子；

"""



class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        my_head = head

        while my_head : #1 2 -> 1 1 2
            tmp = my_head.next
            my_head.next = RandomListNode(my_head.label)
            my_head.next.next = tmp
            my_head = tmp

        # 1 1 2 2 3 3 4 4 5 5   
        # 处理random

        my_head = head
        while my_head:  #一次pass 两个
            if  not my_head.random :  #none
                my_head.next.random = None
            else : 
                my_head.next.random = my_head.random.next

            my_head = my_head.next.next

        # 处理random 完毕， 拆分
        ans = RandomListNode(0)  #HEAD
        p = ans
        my_head = head 
        while my_head:  #挂head.next
            tmp = my_head.next
            my_head.next = tmp.next
            p.next = tmp
            p = p.next
            my_head = my_head.next
        p.next  = None

        return ans.next





if __name__ == '__main__':
    l1 = RandomListNode(1)
    l1.next = RandomListNode(2)
    l1.next.next = RandomListNode(3)
    l1.next.random = l1

    S =Solution()
    r = S.copyRandomList(l1)
    while r:
        print(r.label)
        if  r.random:
            print(r.random.label)
        r = r.next












"""
Q : 
    注意对random  的理解：each node contains an additional random pointer which could point to any node in the list or null.
random 是指向 该list 中的任意一个node 或者none; 不是指向新的node;

"""