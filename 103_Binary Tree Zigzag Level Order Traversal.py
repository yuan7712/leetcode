"""
Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

之 形遍历; 第一行右->左  二行 左->右 ...

"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

"""
S1:
    1. 修改102 ; 每层添加reverse tag即可.
"""
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        m_queue = []
        ans = []
        reverse = False
        # flag = 1
        if not root:
            return []
        m_queue.append(root)
        while m_queue: # 遍历一层
            now = []   #now level itrm
            tmp =[]  # val...
            for item  in  m_queue:
                tmp.append(item.val)
                if item.left:
                    now.append(item.left)
                if item.right:
                    now.append(item.right)
            # 或者使用 flag   翻转. 
            #ans+=[tmp[::flag]]
            #flag*=-1
            if reverse:
                tmp.reverse()
            reverse = not reverse
            ans.append(tmp)
            m_queue = now
        return ans