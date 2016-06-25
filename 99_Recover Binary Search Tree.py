"""
Two elements of a binary search tree (BST) are swapped by mistake.

Recover the tree without changing its structure.

Note:
A solution using O(n) space is pretty straight forward. Could you devise a constant space solution?

"""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
"""
A:
    1. 题目中 二叉搜索树  中序遍历一定増序, 但是中序遍历増序不一定是 二叉搜索树.
    2. 只交换了两个节点.
            原来中序:  1,2,3,4,5,6,7
            swap:  1,6,3,4,5,2,7 
             2 6交换后,导致中序遍历 不再递增,所以只要找到 这两个node 交换val即可

"""

"""
S1: 
    中序递归
    1. 记录pre
    2. 主要是从递增的中序遍历中找到两处反常, 
        first 和second 点
R:
    1. https://leetcode.com/discuss/13034/no-fancy-algorithm-just-simple-and-powerful-order-traversal

"""
class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        def inOrder(p):
            global first,second,pre
            if not p :
                return 
            inOrder(p.left)
            if first == None and pre.val> p.val:   # 记录 first 应该是pre
                first = pre
            if first !=None and pre.val>p.val:  # 记录 second 应该是当前node
                second = p
            pre = p
            inOrder(p.right)

        global first,second,pre
        first,second = None,None
        pre = TreeNode(-1*2**31)
        inOrder(root)
        print(first.val)
        print(second.val)
        first.val, second.val = second.val,first.val  #swap
        return 


"""
S2:
    如果要使用o(1) 空间,可以使用 中序的Morris 遍历.

"""


"""
S3:
    中序迭代
"""
class Solution(object):
    def recoverTree(self, root):

        m_stack = []
        p = root
        first,second, = None,None
        pre = TreeNode(-1*2**31)

        while p or m_stack:
            while p :
                m_stack.append(p)
                p = p.left
            p = m_stack.pop()  #visit
            if first == None and pre.val> p.val:
                first = pre
            if first and pre.val > p.val:
                second = p
            pre = p
            p = p.right
        first.val, second.val = second.val,first.val  #swap
        return 

if __name__ == '__main__':
    S = Solution()
    q1 = TreeNode(3)
    q2 = TreeNode(1)
    q3 = TreeNode(2)
    q1.left =q2
    q1.right = q3

    ss =S.recoverTree(q1)
    print(ss.left.val)




