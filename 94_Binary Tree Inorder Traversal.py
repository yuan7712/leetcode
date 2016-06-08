"""
Given a binary tree, return the inorder traversal of its nodes' values.
中序遍历
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

"""
S1: 
    中序遍历：  左 根 右 ;  使用栈： 时间o(n)  空间o(n)
    p ： 一直向左 直到 null; 
    visit 
    转右子树
"""
class Solution1(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        m_stack = []
        ans = []
        p = root

        while p or m_stack:
            while p :
                m_stack.append(p)
                p = p.left
            p = m_stack.pop()
            ans.append(p.val)
            p = p.right
        return ans



class Solution(object):
    def inorderTraversal(self, root):
        







if __name__ == '__main__':
    S = Solution()
    p1 = TreeNode(1)
    p2 = TreeNode(2)
    p3 = TreeNode(3)
    p1.right = p2
    p2.left  = p3
    ss = S.inorderTraversal(p1)
    print(ss)
