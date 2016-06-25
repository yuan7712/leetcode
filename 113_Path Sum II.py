"""
Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

For example:
Given the below binary tree and sum = 22,
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
return
[
   [5,4,11,2],
   [5,8,4,5]
]

112 Path Sum 类似 .只是返回全部 可能path;
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

"""
S1:
    迭代，使用145_Binary Tree Postorder Traversal.py 中后序的通用遍历;
A:
    1. 此遍历中,栈中即 父节点Node
    2. 负数不必减枝
"""
class Solution1(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if not root :
            return []
        ans = []
        my_stack = []
        last =None 
        total = 0

        while root or my_stack:
            if root :   # 负数 没必要减枝
                my_stack.append(root)
                total+=root.val
                root = root.left
            else:
                root = my_stack[-1]
                if root.right ==None or root.right ==last:
                    if root.left ==None and root.right==None and total ==sum:
                        tmp = [i.val for i in my_stack]
                        ans.append(tmp)
                    last = my_stack.pop()  # visit
                    total -=last.val
                    root = None
                else:
                    root = root.right
        return ans





"""
S2:
    递归
T：
    1. 注意path 由于传递引用,当前Node使用后 pop
"""
class Solution1(object):
    def pathSum(self, root, sum):

        def dfs(p,total,path):
            if not p :
                return []
            total+=p.val
            if p.left == None and p.right == None and total ==sum:
                tmp = path[:]
                tmp.append(p.val)
                return [tmp]
            path.append(p.val)
            left = dfs(p.left,total,path)
            right = dfs(p.right,total,path)
            path.pop()  # 注意pop() , 
            left.extend(right)
            return left

        return dfs(root,0,[])



if __name__ == '__main__':
    S = Solution1()
    q1 = TreeNode(1)
    q2 = TreeNode(2)
    q3 = TreeNode(3)
    q1.left = q2
    q1.right = q3
    ss = S.pathSum(q1,3)
    print(ss)

