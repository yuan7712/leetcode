"""
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

For example,
Given the following matrix:

[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
You should return [1,2,3,6,9,8,7,4,5].

"""


"""
S1:
    外层循环次数
    内层执行一次右下左上. 
    注意： 当每次内层for 没有遍历到元素时  直接break;  所以添加if判断
T:
    case : [[1],[2],[10]] 
"""
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if len(matrix) == 0:
            return []
        m ,n = len(matrix),len(matrix[0])  #row,colum
        ans = []
        for i in range(m//2+1):  #
            if i == n-i:
                break
            for r in range(i,n-i): #right   last [i][n-i-1]
                ans.append(matrix[i][r])
            if i+1 == m-i :
                break
            for d in range(i+1,m-i): #down last [m-i-1][n-i-1]
                ans.append(matrix[d][n-i-1])
            if n-i-2 == i-1:
                break
            for l in range(n-i-2,i-1,-1):#left   last [m-i-1][i]
                ans.append(matrix[m-i-1][l])
            if m-i-2 == i:
                break
            for u in range(m-i-2,i,-1):#up  last [i+1][i]
                ans.append(matrix[u][i])
        return ans

if __name__ == '__main__':
    S = Solution()
    ss =S.spiralOrder([
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
])
    print(ss)



