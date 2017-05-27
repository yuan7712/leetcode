"""
Given a m x n grid filled with **non-negative** numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

和120 类似;

左上角到右下角： 只能右或者下

"""



"""
S1:  DP

    * 问题： 求解从左上角到右下角;
        f(i,j) 从(i,j)到右下角的最优path;   求解f(0,0)
        f(i,j) = min( f(i+1,j) f(i,j+1) ) + (i,j)

    * 代码： 
      
      6 5 4 3 2 1
      5 5 4 3 2 1
      4 4 4 3 2 1
      3 3 3 3 2 1
      2 2 2 2 2 1
      1 1 1 1 1 1

      迭代次序，从右下角开始;

    *  关于m*n矩阵 从右下角向左上角遍历

            1. 由于m!=n  每次应该是从右下角向西北方向的 45度对角线遍历
                对于(i,j)在分别向左 向上
            2. 最外层最少迭代次数min(m,n)
                 第i次循环起点  (m-1-i , n-1-i)
                 然后分别向左 向上

    * 划分问题为 f(i,j) 从(i,j)到(0,0)最优path 更好些;

    * 关于记录path,单独设置path矩阵; 记录该位置的状态


"""

class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int

        """

        m , n  = len(grid),len(grid[0])

        stat = [[2**30]*(n+1) for i in range(m+1)]  #m+1 * n+1 
        stat[m-1][n] = 0
        stat[m-2][n-1] = 0
        
        for i in range(min(m,n)):  # rows
            #left (m-1-i,n-1-i)
            for j in range(n-1-i,-1,-1):  # cal 
                stat[m-1-i][j] = min(stat[m-i][j], stat[m-1-i][j+1]) + grid[m-1-i][j]
            #up (m-i,n-i)
            for k in range(m-1-i,-1,-1): # cal(i,k)
                stat[k][n-1-i] = min(stat[k][n-i], stat[k+1][n-1-i]) + grid[k][n-1-i]

        print(stat)
        return stat[0][0]


    def minPathSum2(self, grid):
        """
              6 6 6 6 6 1
              5 5 5 5 5 1
              4 4 4 4 4 1
              3 3 3 3 3 1
              2 2 2 2 2 1
              1 1 1 1 1 1
        (i,j) 使用(i+1,j) (i,j+1) 所以没必要上面那样遍历;
        初始设置外围，然后依次每行遍历即可;
        """

        m , n  = len(grid),len(grid[0])
        stat = [[0]*n for i in range(m)]  #m+1 * n+1 
        stat[-1][-1] = grid[-1][-1] 

        # 设置外围
        for i in range(n-2,-1,-1): # last row
            stat[-1][i] = stat[-1][i+1] + grid[-1][i]
        for i in range(m-2,-1,-1):  #last colum
            stat[i][-1] = stat[i+1][-1] + grid[i][-1]

        # 遍历每行
        for i in range(m-2,-1,-1):
            for j in range(n-2,-1,-1):
                stat[i][j] = min(stat[i+1][j] , stat[i][j+1])+grid[i][j]

        return stat[0][0]






"""
S2: DP 递归+cache  
    
    S1 62ms  S2 95ms

    
"""
class Solution2(object):
    def minPathSum(self, grid):

        m,n = len(grid), len(grid[0])
        cache = [[-1]*n for i in range(m)]
        cache[-1][-1] = grid[-1][-1]
        return self.recur(grid,cache,0,0)




    def recur(self,grid,cache,i,j):
        """
        求(i,j) 到右下角的最短path

        """
        if cache[i][j]!= -1:
            return cache[i][j]
        if i == len(grid)-1:  #last rows
            cache[i][j] = self.recur(grid,cache,i,j+1) + grid[i][j]
            return cache[i][j]
        if j == len(grid[0])-1:
            cache[i][j] = self.recur(grid,cache,i+1,j) + grid[i][j]
            return cache[i][j]

        cache[i][j] = min(self.recur(grid,cache,i,j+1) , self.recur(grid,cache,i+1,j) )  + grid[i][j]
        return cache[i][j]




if __name__ == '__main__':
    s = Solution2()
    ans = s.minPathSum([[1,2,3,4]])
    print(ans)