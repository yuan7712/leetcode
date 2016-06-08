"""
 创建二叉树,  输入完全二叉树[...] 0 号单元不占
"""

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


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


class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        m_stack = []
        ans = []
        p = root

        while p or m_stack:
            while p :
                m_stack.append(p)
                p = p.left
            p = m_stack.pop()
            ans.append(p.val) #visit
            p = p.right
        return ans

if __name__ == '__main__':
    C = Create()
    cc = C.createTree([0,4,3,5,1,2,6,7])
    S = Solution()
    SS = S.inorderTraversal(cc)
    print(SS)



