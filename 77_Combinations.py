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
    [1,2,3,4]  n = 4  k=2
        -> [1] per(2,4,1)   #转化为[2,3,4] n=3 k =1 返回后每个ans add 1即可
        -> [2,3,4] n = 2 k=2  # 转化为[2,3,4] 取2个数字
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
            return None
        if begin <= end and k == 1 :
            return [[i] for i in range(begin,end+1)]
        ans = self.pers(begin+1,end,k-1)
        [m.append(begin)  for m in ans]
        if end-begin>=k :
            ans.extend(self.pers(begin+1,end,k))
        return ans



"""
S2:
    http://www.cnblogs.com/TenosDoIt/p/3461555.html
    https://siddontang.gitbooks.io/leetcode-solution/content/backtracking/combination.html
"""



if __name__ == '__main__':
    S =Solution()
    ss = S.combine(3,3)
    print(ss)

