"""
Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in place.

click to show follow up.

Follow up:
Did you use extra space?
A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?

"""



"""
O(m + n) space  分别记录每行每列是否置0
"""
class Solution1(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])  # 行列

        flag_m = [0]*m
        flag_n = [0]*n

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    flag_n[j] ,flag_m[i] = 1,1

        for i in range(m) :
            if flag_m[i] ==1:
                matrix[i] = [0]*n
        for j in range(n):
            if flag_n[j] ==1:
                for k in range(m):
                    matrix[k][j]=0

        return matrix



"""
S2: 
    1. 可以对S1 改进，o(m)空间
    2. 设置长度m list 表示该列是否置0
    3. 首先每行遍历 如果元素0 置此行为0 并且设置 对应列 标记
    4. 刷新列

T : 1. 此种比上一个快些
"""

class Solution2(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])

        flag_n = [0]*n #列标记
        flag_m = 0

        for i in range(m):
            flag_m =0
            for j in range(n):
                if matrix[i][j]==0:
                    flag_m,flag_n[j] = 1,1
            if flag_m :
                matrix[i] = [0]*n

        for j in range(n):
            if flag_n[j] ==1:
                for k in range(m):
                    matrix[k][j]=0
        return matrix

        




"""
S3: 
Q :  如果要使用 常数空间， 可以考虑 将S2 中的列状态保存设置到 第一行中，复用第一行

    1. 首先处理第一行， flag 记录此行是否 置0；非0的数字不动。
    2. 从2-n 行 使用S2 即可
    3. 最后 处理第一行 是否置0

T ： beats 99%

"""

class Solution3(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])

        flag_1 = 0
        flag_i = 0 #标记第i 行是否置0

        #先处理第一行
        for i in range(n):
            if matrix[0][i]==0:
                flag_1 =1 # 此行置0

        for i in range(1,m):
            flag_i = 0
            for j in range(n):
                if matrix[i][j] == 0:
                    flag_i=1 #此行置0
                    matrix[0][j]=0 #使用0 表示列 置0
            if flag_i :
                matrix[i] = [0]*n

        #处理列
        for j in range(n):
            if matrix[0][j] ==0:
                for k in range(m):
                    matrix[k][j]=0

        # 单独处理一行
        if flag_1 :
            matrix[0] = [0]*n

        return matrix





if __name__ == '__main__':
    S= Solution2()
    ss =S.setZeroes([[0,1,2,3],[1,2,0,3],[0,2,3,9],[2,9,4,4],[4,2,3,4]])
    print(ss)



