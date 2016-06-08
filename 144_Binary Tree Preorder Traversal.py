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
    先序遍历： 根 左 右
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
            ans.append(p.val)
            #  先序 查看此时栈中node
            fa = [i.val for i in m_stack]
            print((p.val,fa))
            # 先right 后 left ; 这样才能先序 根左右
            if p.right : 
                m_stack.append(p.right)
            if p.left:
                m_stack.append(p.left)
        return ans

"""
S2:

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
                ans.append(root.val)
                #  先序 查看此时栈中node 
                fa = [i.val for i in m_stack]
                print((root.val,fa))

                root = root.left
            else:
                root = m_stack.pop().right
        return ans


"""
S3:

"""
class Solution(object):
    def preorderTraversal(self, root):
        if not root :
            return []
        m_stack = []
        ans = []
        last = None # last pop
        while root or m_stack:
            if root:
                m_stack.append(root)
                #  先序 查看此时栈中node
                #fa = [i.val for i in m_stack]
                #print((root.val,fa))

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
    S =Solution2()
    p1 = TreeNode(1)
    p2 = TreeNode(2)
    p3 = TreeNode(3)
    p1.right = p2
    p2.left  = p3

    C = Create()
    cc = C.createTree([0,4,3,5,1,2,6,7])
    ss = S.preorderTraversal(cc)
    print(ss)



