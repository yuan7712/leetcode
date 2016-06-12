"""
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

判断是不是 平衡二叉树

"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None



"""
S1:
    递归判断.
    分别计算左右子树高度, 如果相差>1  返回 -1(表示不平衡) 否则返回 子树高度  
"""
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def cal_height(root):
            if not root : 
                return 0
            l = cal_height(root.left)
            r = cal_height(root.right) 
            if l == -1 or r == -1 or abs(l-r)>1 : 
                return -1
            else:
                return max(l,r)+1


        if cal_height(root) < 0 :
            return False
        else:
            return True


