"""
Given numRows, generate the first numRows of Pascal's triangle.

For example, given numRows = 5,
Return

[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]

杨辉三角
"""

"""
S1:
    
"""
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        ans = [[] for i in range(numRows)]

        for i in range(numRows):
            for j in range(i+1):
                if j == 0 or j == i:
                    ans[i].append(1)
                else:  #  sum ans[i-1]  [j-1]  [j]
                    ans[i].append(ans[i-1][j-1]+ans[i-1][j])
        return ans


"""
leetcode 
resultset = [[1]* (i+1) for i in range(numRows)]
    for i in range(numRows):
        for j in range(1,  i):
            resultset[i][j] = resultset[i-1][j-1] + resultset[i-1][j]

    return resultset

"""
if __name__ == '__main__':
    S = Solution()
    ss = S.generate(0)
    print(ss)

