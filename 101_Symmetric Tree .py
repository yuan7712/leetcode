"""
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
But the following [1,2,2,null,3,null,3] is not:
    1
   / \
  2   2
   \   \
   3    3
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

"""
S1:
    判断树是否对称.
    1. 使用两个栈, 左右孩子分别  根左右  根右左 遍历即可.
    2. 
"""
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root :
            return True
        m_stack1 = [root.left]
        m_stack2 = [root.right]

        while m_stack1 and m_stack2:
            p  = m_stack1.pop()
            q  = m_stack2.pop()
            if not p and not q:
                continue
            if p and q and p.val ==q.val:
                m_stack1.append(p.right)
                m_stack1.append(p.left)

                m_stack2.append(q.left)
                m_stack2.append(q.right)
            else:
                return False
        return True


        