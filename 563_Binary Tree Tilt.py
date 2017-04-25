# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.cal(root)[0]

    def cal(self,root):
        if root is None:
            return(0,0)   # tile sum
        left = self.cal(root.left)
        right = self.cal(root.right)
        return (left[0]+right[0]+abs(left[1]-right[1]),left[1]+right[1]+root.val)


if __name__ == '__main__':
