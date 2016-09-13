"""
Follow up for "Unique Paths":

Now consider if some obstacles are added to the grids. How many unique paths would there be?

An obstacle and empty space is marked as 1 and 0 respectively in the grid.

For example,
There is one obstacle in the middle of a 3x3 grid as illustrated below.

[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
The total number of unique paths is 2.

Note: m and n will be at most 100.
 和62 相比添加obstacles
"""




"""
S1:
    DFS  --TLE 超时
    对62 dfs 添加判断
    dfs(m,n) = dfs(m-1,n)+dfs(m,n-1)   if obstacleGrid[i][j]! = 1 
"""
class Solution1(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        k = len(obstacleGrid)
        j = len(obstacleGrid[0])
        return self.dfs(obstacleGrid,k,j)
    def dfs(self,obstacleGrid,m,n):
        """
        3*3  m 3-1  n 3-1
        """
        if m ==1 and n ==1 :  # obstacleGrid[0][0]必然0, &&
            return 1
        k = len(obstacleGrid)
        j = len(obstacleGrid[0])
        if m <1 or n < 1 or obstacleGrid[k-m][j-n] == 1 :
            return 0
        return self.dfs(obstacleGrid,m-1,n) + self.dfs(obstacleGrid,m,n-1)

"""
S2:
    DP
    修改62-S4
    [0,0,0]
    [0,1,0]
    [0,0,0]
    使用一维数组, 由于含有障碍,不能像62-dp从2开始. 应遍历每个dp[i][j] 
    初值： dp[i][j] 考虑上面和前面dp,对于第一行初始时dp应设置0. 
        dp[i][0] 需考虑前面元素,所以dp数组长度+1. 
"""
class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        此处默认obstacleGrid[0][0] = 1 未判断
        """
        k = len(obstacleGrid)
        p = len(obstacleGrid[0])
        dp = [0]*(p+1)  #dp[i][0]
        dp[1] = 1  #dp[0][0]入口.如果设置dp[0]=1 则会影响所有dp[i][0]的值
        for i in range(1,k+1):
            for j in range(1,p+1):
                if obstacleGrid[i-1][j-1] == 1:
                    dp[j] = 0
                else:
                    dp[j] = dp[j]+dp[j-1]
        return dp[-1]


if __name__ == '__main__':
    S = Solution()
    ss = S.uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]])
    print(ss)
