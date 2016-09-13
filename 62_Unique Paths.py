"""
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?


Note: m and n will be at most 100.

"""


"""
S1:
    数学公式
    只要求最后的path数目.
    只能向右R和向下D走.m*n矩形, 需要向右m-1步, 向下n-1步. 即C m+n-2  m-1 . 排列组合.

"""
class Solution1(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # 未判断0,0
        j = m+n-2
        s ,k= 1,1
        for i in range(1,m):
            k*=i
            s *= j
            j-=1
        #res = res * (a - i + 1) / i;  防止乘法溢出
        return s/k

"""
S2:
    dfs -- TLE  超时
    每步选择R或者D 
    dfs(m,n) = dfs(m-1,n)+dfs(m,n-1)   m or n ==1  return 1

"""
class Solution2(object):
    def uniquePaths(self, m, n):
        if m ==1 or n ==1 :
            return 1
        return self.uniquePaths(m-1,n) + self.uniquePaths(m,n-1)


"""
S3:
    dp 
    dp[i][j] = dp[i-1][j] + dp[j-1][i] 
    if i or j ==1 : dp[i][j] = 1

"""
class Solution3(object):
    def uniquePaths(self, m, n):
        """
        m 行 n 列
        """

        dp = [[1]*n for i in range(m)]
        for i in range(1,m):
            for j in range(1,n):
                dp [i][j] = dp[i-1][j]+dp[i][j-1]
        return dp[m-1][n-1]


"""
S4: 
    dp 改进
    由S3可知 dp[i][j] = dp[i-1][j] + dp[j-1][i]  
        当我们在计算dp[i][j]时,只和上一行dp 和前一个元素有关,所以不必二维数组,一维数组保存上一行dp即可.
    1  2  3  4  5
  1 1  1  1  1  1
  2 1  ?  ?  ?  ?
  3 1  ?  ?  ?  ??
R:
    http://www.cnblogs.com/TenosDoIt/p/3704091.html
    https://discuss.leetcode.com/topic/15265/0ms-5-lines-dp-solution-in-c-with-explanations
"""
class Solution(object):
    def uniquePaths(self, m, n):
        """
        m 行 n列
        """
        dp = [1]*n   #初始第一行1 dp[0][j] = 1
        for i in range(1,m):
            for j in range(1,n):
                dp [j] = dp[j]+dp[j-1]
        return  dp[n-1]



if __name__ == '__main__':
    S =Solution()
    ss =S.uniquePaths(3,2)
    print(ss)