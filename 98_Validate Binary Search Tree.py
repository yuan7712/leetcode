"""
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.

判断是否合法 二叉查找树
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


"""
S1:
    处理叶子节点时 [2147483647] 

    将Max Min 分别取更大 小  可以pass
"""
class Solution1(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        MAX = 2**31 -1   # 
        MIN = -MAX -1

        def f(r):
            if not r:
                return (0,MAX,MIN)   #(tag,Min,Max)
            t_l = f(r.left)
            t_r = f(r.right)
            if t_l[0] or t_r[0]:
                return (1,MAX,MIN)   # error
            if t_l[2]<r.val and r.val<t_r[1]: #true
                return (0, min(r.val,t_l[1]),max(r.val,t_r[2]))
            else:
                return (1,MAX,MIN)
                
        return not f(root)


"""
S2:
    Pass
A：
    和S1 相比return时 返回 Node即可.
"""
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def f(r):
            if not r:
                return (0,None,None)  #(tag,min max)
            t_l = f(r.left)
            t_r = f(r.right)
            if t_l[0] or t_r[0]:
                return (1,None,None)
            if (not t_l[2] or t_l[2].val<r.val ) and (not t_r[1] or r.val<t_r[1].val):
                t_min = t_l[1] if t_l[1] else r
                t_max = t_r[2] if t_r[2] else r
                return (0,t_min,t_max)
            else:
                return (1,None,None)
        return  not f(root)[0]
