"""
Given a binary tree, return the postorder traversal of its nodes' values.
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


"""
后序遍历：
         后序相比前中 复杂, 左右根,  因为当从孩子返回根时必须区分从左还是右返回; 左则转右 右则pop visit根.
         两种方法
S1:      使用栈记录每个node访问情况, 转左 右时 判断是否已经访问node,防止重复访问
S2:      设计栈结构时，增加该node push时  是从左边还是右边push.
S3:      左右根, 所以我们只要记住last访问点,判断 p.right==last 即可知  是否从右边上升.
"""




"""
S2:
    1. push 一直向左， 标记从left 入栈 tag=0
    2. 此时判断是左还是右侧上升.
            case right:  直接pop 父节点即可
            case left：  转向right 并且设置父点tag==1
"""
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        m_stack = []
        ans = []
        if not root : 
            return []
        p = root

        while p or m_stack:
            while p :
                m_stack.append([p,0])   #push add info from left(tag==0)
                p = p.left
            # p == null 栈顶为其父点. 可能左或右上升. 如果右侧上升 直接pop即可. (右子树单支 递归)
            while m_stack and m_stack[-1][1] == 1 :
                tmp = m_stack.pop()[0]
                ans.append(tmp.val)  # visit
            # 转向right, 修改父点 为从右侧tag. 
            if m_stack:   # turn  right  
                m_stack[-1][1] = 1   # tag = 1
                p  = m_stack[-1][0].right   # p可能null
        return ans

        














"""
S3: 
    1. p 一直向左
    2. 如果p 右子树非空  转右即可.
    3. p 为叶子节点; (此时栈顶是其父点)  此时判断是否可以退栈    然后转向父节点右子树
        退栈 case 1:  m_stack[-1].right == last   last 点是从右子树上升 一直递归
             case 2:  m_stack[-1].right == None   此时父点右子树null, pop即可
"""
class Solution3(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        m_stack = []
        ans = []
        last = None   # last visit

        if not root :
            return []

        p = root 
        while p or m_stack:

            while p.left:    # left->
                m_stack.append(p)
                p = p.left

            if p.right: # 转右子树
                m_stack.append(p)
                p = p.right
            else: 
                ans.append(p.val)  # visit
                last = p
                 # pop  退栈
                while m_stack and (m_stack[-1].right == last or m_stack[-1].right == None):
                    last = m_stack.pop()
                    ans.append(last.val)
                if m_stack :  # 转右
                    p = m_stack[-1].right
                else:
                    p = None # over
        return ans


if __name__ == '__main__':
    S =Solution()
    p1 = TreeNode(1)
    p2 = TreeNode(2)
    p3 = TreeNode(3)
    p1.right = p2
    p2.left  = p3
    ss = S.postorderTraversal(p1)
    print(ss)
   


