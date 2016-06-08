"""
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

层序遍历
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

"""
S1: 
    1.  要分层, 每次使用list记录下一层元素, 当前层遍历后 重置m_queue
    2.  没有使用队列, 因为访问每层后就重置queue
"""

class Solution1(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        m_queue = []
        ans = []
        if not root:
            return []
        m_queue.append(root)
        while m_queue: # 遍历一层
            now = []   #now level itrm
            tmp =[]  # val...
            for item  in  m_queue:
                tmp.append(item.val)
                if item.left:
                    now.append(item.left)
                if item.right:
                    now.append(item.right)
            ans.append(tmp)
            m_queue = now
        return ans

"""
S2:
   Stack 
   1. 每次pop 一个元素, 所以栈中保存item 所在 level
   2. 使用栈, 每次pop栈顶即可. 但是入栈时 先 右后左.  这样就能先左再右遍历
"""
class Solution2(object):
    def levelOrder(self, root):
        if not root:
            return []
        m_stack = [(root,0)]
        ans = []
        while m_stack:
            tmp ,level= m_stack.pop()
            if len(ans) <level+1:
                ans.append([])
            ans[level].append(tmp.val)
            if tmp.right:
                m_stack.append((tmp.right,level+1)) 
            if tmp.left:
                m_stack.append((tmp.left,level+1))
        return ans

"""
S3: Queue
    1. 和S2 类似,保存level 信息
    2. 队列
"""  
import  collections   
class Solution(object):
    def levelOrder(self, root):
        queue  =collections.deque([(root, 0)])
        ans = []
        while queue:
            node, level = queue.popleft()
            if node:
                if len(ans) < level+1: #新层 append
                    ans.append([])
                ans[level].append(node.val)
                queue.append((node.left, level+1))
                queue.append((node.right, level+1))
        return ans


"""
R:
    https://leetcode.com/discuss/51638/python-solutions-dfs-recursively-dfs-stack-bfs-queue
"""














if __name__ == '__main__':
    S =Solution()
    p1 = TreeNode(1)
    p2 = TreeNode(2)
    p3 = TreeNode(3)
    p1.right = p2
    p2.left  = p3
    ss = S.levelOrder(p1)
    print(ss)
