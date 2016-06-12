"""
Given two binary trees, write a function to check if they are equal or not.

Two binary trees are considered equal if they are structurally identical and the nodes have the same value.

"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

"""
S1: 
    使用任意一种遍历 同时遍历 p q  即可
    非递归 先序
"""
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if not p and not q:
            return True
        m_stack =[]
        if p and q  :
            m_stack.append(p)
            m_stack.append(q)
        else:
            return False
        while m_stack:
            q = m_stack.pop()
            p = m_stack.pop()
            if p.val != q.val :
                return False
            if not p.right and not q.right:
                pass
            elif p.right and q.right  :
                m_stack.append(p.right)
                m_stack.append(q.right)
            else:
                return False

            if not p.left and not q.left:
                continue
            elif p.left and q.left :
                m_stack.append(p.left)
                m_stack.append(q.left)
            else:
                return False
        return True

"""
S1:
    len(S)
"""
class Solution1(object):
    def isSameTree(self, p, q):
        if not p and not q:
            return True
        m_stack =[]
        if p and q  :
            m_stack.append(p)
            m_stack.append(q)
        else:
            return False
        while m_stack:
            q = m_stack.pop()
            p = m_stack.pop()
            if p.val != q.val :
                return False
            if p.right and q.right  :
                m_stack.append(p.right)
                m_stack.append(q.right)
            if len(m_stack)%2 : return False
            if p.left and q.left :
                m_stack.append(p.left)
                m_stack.append(q.left)
            if len(m_stack)%2 : return False
        return True

"""
S2:
    ***
    先入栈p q 
"""
class Solution1(object):
    def isSameTree(self, p, q):
        stack = [(p,q)]
         while stack :
            x,y = stack.pop()
            if x == None and y ==None:
                continue
            if x == None or y == None:
                return False
            if x.val == y.val:
                stack.append((x.left,y.left))
                stack.append((x.right,y.right))
            else:
                return False
        return True


if __name__ == '__main__':
    S = Solution1()
    p1 = TreeNode(1)
    p2 = TreeNode(2)
    p3 = TreeNode(3)
    p1.right = p2
    p2.left  = p3

    p11 = TreeNode(1)
    p22 = TreeNode(2)
    p33 = TreeNode(3)
    p11.right = p22
    p22.left  = p33
    ss = S.isSameTree(p1,p11)
    print(ss)

        


