"""
Given an integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

For example,
Given n = 3,

You should return the following matrix:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]

与54相反
"""

"""
S1:
    修改54  去掉if即可 等判断
"""
class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        ans = [[0]*n for i in range(n)]
        num = 1
        for i in range(n//2+1):  #
            for r in range(i,n-i): #right   last [i][n-i-1]
                ans[i][r] = num
                num+=1
            for d in range(i+1,n-i): #down last [m-i-1][n-i-1]
                ans[d][n-i-1]=num
                num+=1
            for l in range(n-i-2,i-1,-1):#left   last [m-i-1][i]
                ans[n-i-1][l]=num
                num+=1
            for u in range(n-i-2,i,-1):#up  last [i+1][i]
                ans[u][i]=num
                num+=1
        return ans


if __name__ == '__main__':
    S = Solution()
    ss = S.generateMatrix(3)
    print(ss)