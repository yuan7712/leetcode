"""
Given a binary tree, flatten it to a linked list in-place.

For example,
Given

         1
        / \
       2   5
      / \   \
     3   4   6
The flattened tree should look like:
   1-2-3-4-5-6
Hints:
If you notice carefully in the flattened tree, each node's right child points to the next node of a pre-order traversal.

将二叉树 转换为链表.  前序遍历
"""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

"""
S1: 
    前序非递归  修改 使用栈

    挂载right 时，可以先将左右 全部入栈 ,然后挂载栈顶.
    或者 记录pre ,每次出栈 挂载. 此时需单独处理root 或建头结点
"""
class Solution1(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        
        if not root :
            return
        m_stack =[]
        m_stack.append(root)

        while m_stack:
            p = m_stack.pop()

            if p.right:
                m_stack.append(p.right)
            if p.left:
                m_stack.append(p.left)
            p.left = None
            if m_stack:      # 入栈后挂载
                p.right = m_stack[-1]
            # else  不写也行 最后一个必然None
        return


"""
S2:
    前序Morris 修改 .o(1)空间

    1. 向左转时, 将p的前驱.right 指向p.right; (这样当左子树遍历后 直接转右子树)
    2. Moris 中p点会两次访问,并修改前驱.right为原样Null. 但是此处只需设置p.left为null即可.
         这样也就不必第二次访问p 前驱.

R：
    144 pre 遍历
    https://leetcode.com/discuss/13054/share-my-simple-non-recursive-solution-o-1-space-complexity

"""
class Solution(object):
    def flatten(self, root):
        if not root :
            return 
        p = root

        while p:
            if not p.left:  # turn right
                p = p.right
            else:
                tmp = p.left
                while tmp.right:  # 找到pre.  
                    tmp = tmp.right
                tmp.right = p.right  # 将pre的后继挂载好
                pp = p
                p = p.left # 转向左
                pp.left = None # 左子树设置为null, 
                pp.right = p  # 根左 设置后继
        return 



