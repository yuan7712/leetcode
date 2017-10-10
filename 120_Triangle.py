"""
Given a triangle, find the minimum path sum from top to bottom. Each step you may move to ** adjacent numbers on the row below **.

For example, given the following triangle
[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

Note:
Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.


计算最短path; 只能相邻点移动；

相邻点：(i,j)  相邻点：  (i+1,j) (i+1,j+1)   题目要求下一行


"""




"""
S1:  DP  从下到上              时间o(n^2) 空间o(n)


1. 划分子问题 找到最优子结构;  2. 重叠子问题; 


    f(i,j) = min(f(i+1,j) f(i+1,j+1)) + (i,j)

    * 代码： 
            f(i,j)只依赖下一行，所以只要一维数组存储一行状态即可;
            从下向上

            for rows in n...0:
                for item in rows:
                    f(i,j) = min(f(i+1,j) f(i+1,j+1)) + (i,j)
            return f(0,0)
    * 复杂度：
            时间o(n^2) 空间o(n)



"""


class Solution1(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """

        if not triangle:
            return -1
        m = len(triangle)

        stat = triangle[-1][:]
        
        for i in range(m-2,-1,-1): #rows
            for j in range(len(triangle[i])):
                stat[j] = min(stat[j], stat[j+1])+triangle[i][j]

        return stat[0]






"""
S2:   DP 递归+cache 

      f(i,j) = min(f(i+1,j) f(i+1,j+1)) + (i,j)

"""

class Solution2(object):

    def minimumTotal(self, triangle):
        if not triangle:
            return -1;
        
        n = len(triangle[-1])   #需要使用二维数组
        cache = [[-1]*n for i in range(n)]


        return self.recur(triangle,cache,0,0)

    def recur(self,triangle,cache,i,j):
        """
        
        计算(i,j) 位置最优解

        """
        if i == len(triangle)-1:   # last rows
            cache[i][j] = triangle[i][j] 
            return triangle[i][j]
        if cache[i][j] != -1: #valid
            return cache[i][j]


        cache[i][j] = min(self.recur(triangle,cache,i+1,j),self.recur(triangle,cache,i+1,j+1)) + triangle[i][j]
        return cache[i][j]

        




if __name__ == '__main__':
    S =Solution2()
    ans = S.minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]])     #
    print(ans)
    