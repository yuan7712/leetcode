"""
Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.

 h和108_Convert Sorted Array to Binary Search Tree  类似, 只是 将数组-> 链表 不能随机访问

"""
# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


"""
S1:
    与108,类似,每次不能随机获取center,所以遍历获取. 复杂度高

"""

"""
S2:
    对S1改进; pass
A:
    1.和108 基本思路一致,还是使用递归;
        Ex:  1 2 3 4 5  ;当以3 为root ,分别创建左右子树, 创建右子树时 左子树12 已经pop;
            基于此我们不再首先确定 root, 而是首先创建左子树,每次New Node  pop List. 左子树创建完毕后pop root即可.
    2. 全局修改head, global 变量
    3. 为此 需要首先遍历list获取长度. 递归时传递子树长度即可.
T: 
    时间o(n) 空间o(log n)
"""
class Solution2(object):
    def sortedListToBST(self, heads):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        global head
        head = heads

        def genTree(nums):
            """
            nums 标记 node个数; nums >=0
            return : 创建该子树 长度nums
            """
            global head
            if nums == 0:
                return None
            if nums == 1:  # 可以del 不判断也可
                tmp = TreeNode(head.val)
                head = head.next 
                return tmp
            # case  nums > 1
            left_num ,right_nums = nums//2 , nums//2
            if not nums%2: #even
                left_num -= 1

            root = TreeNode(-1)  #modify  val latter

            root.left = genTree(left_num)
            root.val = head.val
            head = head.next

            root.right = genTree(right_nums)

            return root

        # 首先 获取List长度
        if not head:
            return None
        num = 0
        p = head
        while p:
            num+=1
            p = p.next

        return genTree(num)













if __name__ == '__main__':
    S = Solution()
    q1 = ListNode(1)
    q2 = ListNode(2)
    q3 = ListNode(3)
    q4 = ListNode(4)
    q1.next = q2
    q2.next = q3
    q3.next = q4
    ss = S.sortedListToBST(q1)
    print(ss.val)




