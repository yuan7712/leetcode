"""
Given inorder and postorder traversal of a tree, construct the binary tree.

 中 后 -> Tree
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

"""
S1:
     和 105_Construct Binary Tree from Preorder and Inorder Traversal  类似.
    传递index

"""
class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        def bTree(i_s,i_e,p_s,p_e):
            if i_s<=i_e:
                root = TreeNode(postorder[p_e])
                i  = inorder.index(postorder[p_e])
                left_len = i-i_s
                right_len = i_e - i

                root.left = bTree(i_s,i-1,p_s,p_s+left_len-1)
                root.right = bTree(i+1,i_e,p_s+left_len,p_e-1)

                return root
            return None

        return bTree(0,len(inorder)-1,0,len(postorder)-1)


if __name__ == '__main__':
    S =Solution()
    ss = S.buildTree([1,2],[2,1])




