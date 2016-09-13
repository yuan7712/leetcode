 #coding=utf-8
"""
Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

For example,
If n = 4 and k = 2, a solution is:

[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
等价于C n k
"""



"""
S1:
    递归
     C(n,k)=C(n-1,k-1)+C(n-1,k)
    [1,2,3,4]  n = 4  k=2
        -> [1] per(2,4,1)   #转化为[2,3,4] n=3 k =1 返回后每个ans add 1即可
        -> per[2,3,4] n = 2 k=2  # 转化为[2,3,4] 取2个数字
        ==  当末层k=1 时 返回集合
    边界：
        注意begin end k 合法性.  即当k>n 时return None
"""
class Solution1(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        begin,end = 1,n
        ans = self.pers(begin,end,k)
        return ans

    def pers(self,begin,end,k):
        """
        begin ,end   起始结束的数字
        k, 要选择数字个数
        """
        if end-begin+1 < k :    #k >n  无解
            return []
        if begin <= end and k == 1 :
            return [[i] for i in range(begin,end+1)]
        ans = self.pers(begin+1,end,k-1)
        [m.append(begin)  for m in ans]
        ans.extend(self.pers(begin+1,end,k))
        return ans



"""
S2:
    ***dfs递归 -- 与S1 递归方法一致.
    C(n,k)=C(n-1,k-1)+C(n-1,k)
    记录path, dfs
T：
    类比78 -S2
R： 
    http://www.cnblogs.com/TenosDoIt/p/3461555.html    #S1
    https://siddontang.gitbooks.io/leetcode-solution/content/backtracking/combination.html
"""
class Solution2(object):
    def combine(self, n, k):
        ans = []
        self.dfs(ans,[],1,n,k)
        return ans

    def dfs(self,ans,path,begin,end,k):
        if end -begin+1 < k:   #无解 参数
            return 
        if k == 0:  #add
            ans.append(path[:])
            return
        path.append(begin)
        self.dfs(ans,path,begin+1,end,k-1)
        path.pop()
        self.dfs(ans,path,begin+1,end,k)
        return 

"""
S3:
    递归
    [1,2,3,4,5]  n=5 k=3 
    和S1 S2 递归稍微不一样.
    [1]+ dfs([2,3,4,5],2)    #选以1开始 + dfs 递归
    [2]+ dfs([3,4,5],2)   #选以2开始,除去1 + 递归
    [3]+ dfs([4,5],2)    #选以3开始 + 递归
    --- 4 之后不再选择, 不可能
T： 
    此可以类比S2 , dfs记录path即可.
R:
    http://www.cnblogs.com/TenosDoIt/p/3461555.html    #S2
"""
class Solution(object):
    def combine(self, n, k):
        ans = []
        self.dfs(ans,[],1,k,n)
        return ans

    def dfs(self,ans,path,start,k,n):
        if k < 0 :
            return
        if k == 0 :
            ans.append(path[:])
            return 
        for i in range(start,n+1):
            path.append(i)
            self.dfs(ans,path,i+1,k-1,n)
            path.pop()
        return 

"""
S4:
    非递归  --TLE 超时
    --Error
    --较复杂, 对78 加以限制.
    78 subset 是求出所有子集, 而此题是求长度为k 的子集. 
    78 + k限制即可
"""
class Solution4(object):
    def combine(self, n, k):

        ans1 = [[]]
        for i in range(1,n+1):
            tmp = [p[:] for p in ans1]
            [p.append(i) for p in tmp]
            ans1.extend(tmp)
        ans = [m[:] for m in ans1 if len(m)==k]
        return ans









"""
此题和 78 Subsets 类似 
    [1,2,3] 
    78 求全部子集
    77 求k长子集
"""
if __name__ == '__main__':
    S =Solution()
    ss = S.combine(4,4)
    print(ss)

