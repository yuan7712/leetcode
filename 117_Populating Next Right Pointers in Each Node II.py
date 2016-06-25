"""
Follow up for problem "Populating Next Right Pointers in Each Node".

What if the given tree could be any binary tree? Would your previous solution still work?

Note:

You may only use constant extra space.
For example,
Given the following binary tree,
         1
       /  \
      2    3
     / \    \
    4   5    7
After calling your function, the tree should look like:
         1 -> NULL
       /  \
      2 -> 3 -> NULL
     / \    \
    4-> 5 -> 7 -> NULL
与116 一样; 117 树的结构不只是满二叉树，可以是任意类型.  o(1) space

"""
# Definition for binary tree with next pointer.
class TreeLinkNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

"""
S1:
A:
    1. 和116类似,分层处理
    2. 由于不是满二叉树,所以必须记住 处理Next的最后一个node  pre
    3. 由于对每层的 第一个Node 单独处理, 代码较乱
"""
class Solution1(object):
    def connect(self, root):
        """
        :type root: TreeLinkNode
        :rtype: nothing
        """
        while root:  #一层一层处理
            while root and root.left==None and root.right == None:  #跳过叶子node
                root = root.next

            if not root:  #全部叶子node return
                return 
            if root.left  and root.right:   # 处理第一个Node; first 记录下一个层 首个Node;pre记录最后访问node
                root.left.next = root.right
                first = root.left
                pre = root.right
            elif root.left:
                first  = root.left
                pre = root.left
            else:
                first = root.right
                pre = root.right
            root = root.next

            while root :  # 处理该层之后的Node,和以上处理第一个Node一致
                if root.left == None and root.right == None:  #跳过叶子节点
                    root = root.next
                    continue
                if root.left and root.right:
                    pre.next = root.left
                    root.left.next = root.right
                    pre = root.right
                elif root.left:
                    pre.next = root.left
                    pre = root.left
                else:
                    pre.next = root.right
                    pre = root.right
                root = root.next
            root = first
        return 



"""
S2:
    修改S1,为每行添加header, 整合了第一个Node 的特例
T：
    1. 记住，root = root.next  多次提交error
    2. 每层开始处 初始设置 pre. first
"""
class Solution2(object):
    def connect(self, root):

        first = TreeLinkNode(0)  #header
        first.next = root

        while first.next:
            root = first.next   # root 为每层的开始
            first.next = None  # 断开
            pre = first
            while root:
                if root.left==None and root.right==None:  #pass 叶子点
                    root = root.next
                    continue
                if root.left and root.right:
                    pre.next = root.left
                    root.left.next = root.right
                    pre = root.right
                elif root.left:
                    pre.next = root.left
                    pre = root.left
                else:
                    pre.next = root.right
                    pre = root.right
                root = root.next
        return


"""
S3：
    leetcode, 整合while
R：
    1. https://leetcode.com/discuss/3339/o-1-space-o-n-complexity-iterative-solution
"""
class Solution(object):
    def connect(self, root):
        first = TreeLinkNode(0)  #level header
        pre = first
        while root :
            while root:
                if root.left :
                    pre.next = root.left
                    pre = root.left
                if root.right:
                    pre.next = root.right
                    pre = root.right
                root = root.next
            root = first.next
            first.next = None
            pre = first


if __name__ == '__main__':
    S =Solution()
    q1= TreeLinkNode(1)
    q2 = TreeLinkNode(2)
    q3 = TreeLinkNode(3)
    q4 = TreeLinkNode(4)
    q5 = TreeLinkNode(5)
    q1.left = q2
    q1.right = q3
    q2.left = q4
    q4.right = q5
    S.connect(q1)




