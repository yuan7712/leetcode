"""
Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


"""
S1:
    递归即可.
Q:  
    提交 提示 `?` 

    时间o(n) 空间o(log n)
    
"""
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """


        def genTree(start,end):
            """
            递归生成Tree, 每次选取(start+end)//2 为root
            """
            if start > end:
                return None
            #center = (start+end)//2     优化 防止java...溢出,
            center = start + (end-start)//2
            root = TreeNode(nums[center])
            root.left = genTree(start,center-1)
            root.right = genTree(center+1,end)
            return root

        return genTree(0,len(nums)-1)


