"""
Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

对102 修改将 返回值 reverse即可.

"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
"""
S1:
    修改102 add reverse
    1. 可以对102 其余方法修改...
"""
class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ans = []
        m_queue = []
        if not root:
            return ans
        m_queue.append(root)
        while m_queue:
            tmp = []
            levle = []
            for item in m_queue:
                tmp.append(item.val)
                if item.left:
                    levle.append(item.left)
                if item.right:
                    levle.append(item.right)
            ans.append(tmp)
            m_queue = levle
        ans.reverse()    #reverse  无返回值, 原地操作
        return ans



if __name__ == '__main__':
    S =Solution()
    p1 = TreeNode(1)
    p2 = TreeNode(2)
    p3 = TreeNode(3)
    p1.right = p2
    p2.left  = p3
    ss = S.levelOrderBottom(p1)
    print(ss)

