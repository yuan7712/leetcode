"""
Given an integer n, generate all structurally unique BST's (binary search trees) that store values 1...n.

For example,
Given n = 3, your program should return all 5 unique BST's shown below.

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3

"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
"""
S1:
    要将所有的结构输出.

    按照94_Unique Binary Search Trees 中的DP 解法改进.

    1. DP 数组存放 n 时,所有可能的树
    2. 计算n 时 所有树时, 以1...n 分别为root 创建树.
            1 2 3 4 5 n=5 
            当以3 为root 时, 左子树 右子树 分别有  dp[j-1] dp[i-j] 种情况。
            新建root Node.
            root.left  直接挂在左边 dp 中的深拷贝 即可
            root.right  需要进行offset. (dp 数组中只有1 2 形成的结构, 现在我们需要 4  5 形成结构，只需偏移即可)

R:
https://leetcode.com/discuss/9790/java-solution-with-dp
"""

import copy   # 深度copy
class Solution1(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        def changeVal(root,offset):
            """
            遍历树,对每个node val+= offset
            """
            if not root:
                return None
            m_stack = [root]
            while m_stack:
                p = m_stack.pop()
                p.val+=offset
                if p.right:
                    m_stack.append(p.right)
                if p.left:
                    m_stack.append(p.left)
            return root


        if not n : 
            return []
        dp = [[] for i in range(n+1)]   #存放n时刻 所有可能Tree
        dp[0] = [None]
        dp[1] = [TreeNode(1)]

        for i in range(2,n+1):
            for j in range(1,i+1):               
                for ii in range(len(dp[j-1])):
                    for jj in range(len(dp[i-j])):
                        tmp = TreeNode(j)
                        tmp.left = copy.deepcopy(dp[j-1][ii])  #深度copy, 左子树没必要偏移.
                        tmp.right = copy.deepcopy(dp[i-j][jj])  # change val
                        if tmp.right:
                            changeVal(tmp.right,i)  #偏移i 即可
                        dp[i].append(tmp)  #add
        return dp[n]


"""
S2:  
    递归求解.
    和DP 相比要快很多,但是此处 子树存在被重复使用情况. 如果OJ 判断时 删除Node 则不能Pass.
A:
    1. 递归,核心 依次选取每个数字为root,递归创建左右子树, return.

T:
    1.  1 2 3 4 5  ; 递归当以3 创建root,左右创建子树, left 返回两个 right返回两个. 但是他们均会被重复使用.

    
R:
https://leetcode.com/discuss/10254/a-simple-recursive-solution
"""
class Solution(object):
    def generateTrees(self, n):
        global NUM   # 判断 创建Node 总数.
        NUM = 0
        def genTree(start,end):
            global NUM
            ans = []
            if start>end:
                ans.append(None)
                return ans
            if start == end:
                NUM +=1
                ans.append(TreeNode(start))
                return ans
            # 依次选择 为root
            for i in range(start,end+1):
                left  = genTree(start,i-1)
                right = genTree(i+1,end)
                for m in left:
                    for n in right:
                        NUM+=1
                        root = TreeNode(i)
                        root.left = m
                        root.right = n
                        ans.append(root)
            return ans

        if n ==0:
            return []
        ans = genTree(1,n)
        print(NUM)
        return ans




if __name__ == '__main__':
    S =Solution()
    ss = S.generateTrees(4)
    print(len(ss))