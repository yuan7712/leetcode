# -*- coding: utf-8 -*-
"""
Given a binary tree, return the preorder traversal of its nodes' values.
先序遍历二叉树
T: leetcode 输入按照完全二叉树  [1,null,2,3...]
"""

#Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

"""
S1: 
    visit 当前node 后将其右孩子入栈
    1. visit root
    2. right push
    3. 转 left
"""
class Solution1(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root :
            return []
        m_stack = []
        ans = []
        m_stack.append(root)

        while m_stack:
            p = m_stack.pop()
            ans.append(p.val)  #visit
            # 先right 后 left ; 这样才能先序 根左右
            if p.right : 
                m_stack.append(p.right)
            if p.left:
                m_stack.append(p.left)
        return ans

"""
S2:
    使用栈 非递归. visit当前node后 将自己也入栈.
    和S1 类似只是出栈不一样. 
    1. visit  root  并且将root入栈 (而S1 visit root 后 root 不进栈而是root.right 进栈)一直向左,
            栈 中存放的全部是 已经visit的node
    2. 当到了左侧尽头时， 将栈顶pop ,转右即可.

"""
class Solution2(object):
    def preorderTraversal(self, root):
        if not root :
            return []
        m_stack = []
        ans = []
        while root or m_stack:
            if root :
                m_stack.append(root)
                ans.append(root.val)  # visit & push
                root = root.left
            else:
                root = m_stack.pop().right  #pop & turn right
        return ans


"""
S3:
    前 中 后序 通用代码;  模拟递归栈的出栈策略.
    1. visit node 时, 栈中为 根->此node   path
"""
class Solution3(object):
    def preorderTraversal(self, root):
        if not root :
            return []
        m_stack = []
        ans = []
        last = None # last pop
        while root or m_stack:
            if root:
                m_stack.append(root)
                # pre
                ans.append(root.val)
                root = root.left
            else :
                root = m_stack[-1]
                #inorder
                #if root.right == None or root.right!=last:
                    #ans.append(root.val)
                if root.right == None or root.right == last:
                    last = m_stack.pop()
                    # post order 
                    #ans.append(last.val)
                    root = None
                else:
                    root = root.right
        return ans




"""
S4:
Morris
    前序Morris和中序类似,详看中序;
    只有一处不同 p visit 的位置. 前序应该在转向左侧时 visit; 中序是返回父点时 visit (左根右).

    T: 
    1. 这三种Morris 代码基本一致.

    2. 前序Morris 为了不改变原树结构, 会两次访问root, 如果可以毁坏树结构,
     完全可以一次访问, 具体看 114_ Flatten Binary Tree to Linked List
"""
class Solution4(object):
    def preorderTraversal(self, root):
        if  not root :
            return []
        ans = []
        p  = root
        while  p:
            if not p.left:
                ans.append(p.val)  #左子树null  visit
                p = p.right
            else:
                tmp = p.left
                while tmp.right and tmp.right!=p:
                    tmp = tmp.right
                if tmp.right == p:  # 第二次访问 
                    tmp.right = None
                    p = p.right
                else:  # 第一次访问 建立线索
                    tmp.right = p
                    ans.append(p.val)   # 转向左子树时候  visit
                    p = p.left
                    

        return ans





"""
创建二叉树模块，输入完全二叉树结构，0单元不占， Null 用'#' 表示; 返回root
"""
class Create(object):
    def createTree(self,nodes):
        if len(nodes) <=1 :
            return None

        for i in range(len(nodes)-1,-1,-1):
            if nodes[i] == '#':
                tmp = None
                nodes[i] = tmp
            else:
                tmp = TreeNode(nodes[i])
                nodes[i] = tmp
                if 2 * i < len(nodes):
                    tmp.left = nodes[2*i]
                if 2 * i +1 <len(nodes):
                    tmp.right = nodes[2*i+1]
        return nodes[1]



if __name__ == '__main__':
    S =Solution1()
    p1 = TreeNode(1)
    p2 = TreeNode(2)
    p3 = TreeNode(3)
    p1.right = p2
    p2.left  = p3

    C = Create()
    cc = C.createTree([0,4,3,5,1,2,6,7])
    ss = S.preorderTraversal(cc)
    print(ss)


"""
S: 
    先序遍历  根 左 右 
    1. 递归遍历
    2. 非递归  使用栈.
        2.1 ： S1
        2.2 :  S2
        2.3 :  S3  模拟递归. 前中后 通用.
        T:  与中序类似 他们只是栈 pop 策略不同.

    3. Morris  不使用栈 S4
"""

