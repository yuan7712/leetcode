"""
Given preorder and inorder traversal of a tree, construct the binary tree.
前中 -> Tree

"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

"""
S1 :
     递归实现;  未通过
     Memory Limit Exceeded 
T: 
    1. MLE   主要是由于 python slice 造成的.
"""
class Solution1(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """

        def bTree(preo,ino):
            if preo:
                root = TreeNode(preo[0])
                i = ino.index(preo[0])
                left_len = i
                right_len = len(ino) - i -1
                root.left = bTree(preo[1:left_len+1],ino[0:i])
                root.right = bTree(preo[left_len+1:],ino[i+1:])
                return root
            else:
                return None

        return bTree(preorder,inorder)



"""
S2:
   不slice 使用传递index.  Pass 
"""
class Solution2(object):
    def buildTree(self, preorder, inorder):

        def bTree(p_s,p_e,i_s,i_e):
            if p_s <= p_e:
                root = TreeNode(preorder[p_s])
                i = inorder.index(preorder[p_s])
                left_len  = i-i_s
                right_len = i_e -i
                
                root.left = bTree(p_s+1, p_s+left_len, i_s,i-1)
                root.right = bTree(p_s+left_len+1,p_e,i+1,i_e)
                return root
            return None
        return bTree(0,len(preorder)-1,0,len(inorder)-1)




"""
S3:
    递归改进.  leetcode pass
    只需要判断inorder. 构造root.right 时 ,preorder 左侧已经del 
    1. 此方法即 只需要slice inorder 即可.

R： https://leetcode.com/discuss/28773/a-python-recursive-solution
"""
class Solution3(object):
    def buildTree(self, preorder, inorder):
        if inorder:
            root = TreeNode(preorder.pop(0))
            inorderIndex = inorder.index(root.val)
            root.left = self.buildTree(preorder, inorder[:inorderIndex])
            root.right = self.buildTree(preorder, inorder[inorderIndex+1:])
            return root





        
