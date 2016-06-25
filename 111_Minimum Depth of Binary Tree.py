"""
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

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
A:
    1.  使用先序, 由于此先序遍历时 栈中 不是所有 父节点, 所以自行存取 深度;
    2.  使用深度减枝
T:
    也可以使用后序, 或者其余先序遍历, 使用len(栈) 即判断 深度.

"""
class Solution1(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root :
            return 0
        my_stack = [(root,1)]
        ans = 2**31 -1

        while my_stack:
            tmp = my_stack.pop()
            p ,depth = tmp[0],tmp[1]

            if p.left==None and p.right==None:
                ans = min(ans,depth)
            if p.right and depth<ans:
                my_stack.append((p.right,depth+1))
            if p.left and depth < ans:
                my_stack.append((p.left,depth+1))

        return ans


"""
S2:
    递归
A:
    1. 当叶子节点时候,返回1; 
    2. p的一侧为Null,时 此时应该返回Max, 
"""
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        MAX  =2 **31 -1
        def getMin(p):
            if not p :
                return MAX
            if p.left == None and p.right == None :
                return 1    
            left = getMin(p.left)
            right = getMin(p.right)
            return min(left,right)+1

        if not root :
            return 0
        return getMin(root)



"""
S3： 
    
   public static int minDepth(TreeNode root) {
    if (root == null)   return 0;
    if (root.left == null)  return minDepth(root.right) + 1;
    if (root.right == null) return minDepth(root.left) + 1;
    return Math.min(minDepth(root.left),minDepth(root.right)) + 1;
}
"""