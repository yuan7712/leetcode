"""
Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

For example:
Given the below binary tree and sum = 22,
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \      \
        7    2      1
return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.

求给定Tree 中root->leaf path sum=22 ; 存在or 不存在

"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

"""
S1:

A：
    1.  前序遍历, 栈中每个node保存 当前sum.    由于最后只要返回True False 所以没必要保存全部父节点
    2.  注意Node.val 可能<0  所以不可减枝

"""
class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root :
            return False
        my_stack = [(root,root.val)]

        while my_stack:
            tmp = my_stack.pop()
            p,total = tmp[0],tmp[1]

            if p.left ==None and p.right == None and total ==sum:
                return True
            if p.right : # and total < sum  可能出现负数 不能减枝
                my_stack.append((p.right,total+p.right.val))
            if p.left : #and total< sum 
                my_stack.append((p.left,total+p.left.val))
        return False

"""
S2:
    递归

bool hasPathSum(TreeNode* root, int sum) {
    if (!root) return false;
    sum -= root->val;
    if (!root->left && !root->right) return sum == 0;
    return hasPathSum(root->left, sum) || hasPathSum(root->right, sum);
}
"""

