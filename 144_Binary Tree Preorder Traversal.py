# -*- coding: utf-8 -*-
"""
Given a binary tree, return the preorder traversal of its nodes' values.
先序遍历二叉树
T: leetcode 输入按照完全二叉树  [1,null,2,3...]
"""

#Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

"""
S1: 
    先序遍历： 根 左 右
    1. visit root
    2. right push
    3. 转 left
"""
class Solution1(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root :
            return []
        m_stack = []
        ans = []
        m_stack.append(root)

        while m_stack:
            p = m_stack.pop()
            ans.append(p.val)
            # 先right 后 left ; 这样才能先序 根左右
            if p.right : 
                m_stack.append(p.right)
            if p.left:
                m_stack.append(p.left)
        return ans

"""
S2:

"""
class Solution2(object):
    def preorderTraversal(self, root):
        if not root :
            return []
        m_stack = []
        ans = []
        while root or m_stack:
            if root :
                m_stack.append(root)
                ans.append(root.val)
                root = root.left
            else:
                root = m_stack.pop().right
        return ans


"""
S3:

"""
class Solution(object):
    def preorderTraversal(self, root):
        if not root :
            return []
        m_stack = []
        ans = []
        while root or m_stack:
            if root:
                m_stack.append(root)
                root = root.left
            else :
                root = m_stack[-1]











if __name__ == '__main__':
    S =Solution()
    p1 = TreeNode(1)
    p2 = TreeNode(2)
    p3 = TreeNode(3)
    p1.right = p2
    p2.left  = p3
    ss = S.preorderTraversal(p1)
    print(ss)



