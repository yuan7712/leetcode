"""
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

与111 MIN 一样

"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

"""
S1:
    迭代

"""
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root :
            return 0
        my_stack = [(root,1)]
        ans = 0

        while my_stack:
            tmp = my_stack.pop()
            p ,depth = tmp[0],tmp[1]

            if p.left == None and p.right == None:
                ans = max(depth,ans)
            if p.right:
                my_stack.append((p.right,depth+1))
            if p.left:
                my_stack.append((p.left,depth+1))

        return ans


"""
S2:
    递归
    修改111_Minimum Depth of Binary Tree.py  即可
"""

