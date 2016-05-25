"""
You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

Follow up:
Could you do this in-place?
"""



"""
S1
题目中要求不能 申请空间， 所以 S1此方法不可行
"""

class Solution1(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        a = []
        len_l = len(matrix)
        j = 0
        # 矩阵逆置  副对角线
#        for i in range(len_l):
#            a.append([])
#            for row in reversed(matrix):
#                a[i].append(row[len_l-1-i])

        # 矩阵逆置 使用 生成式 ， 与上述 效果等同
        a = [[row[len_l-1-i] for row in reversed(matrix)] for i in range(len_l)]
        # 沿着水平 翻转
        while j < len_l//2 :
            a [j] ,a[len_l-1-j] =  a[len_l-1-j],a [j]
            j +=1

        return a






"""
S2 ：
 不能申请空间， 所以原地逆置 for for 即可
"""

class Solution2(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        len_l = len(matrix)-1
        j = 0
        for i in range(len_l):
            for j in range(len_l-i):
                matrix[i][j] ,matrix[len_l-j][len_l-i] =matrix[len_l-j][len_l-i], matrix[i][j]
        
        while j < len(matrix)//2 :
            matrix [j] ,matrix[len_l-j] =  matrix[len_l-j],matrix [j]
            j +=1

        return matrix



"""
S3:
首先翻转 再主对角转置 
但是返回的list 元素是tuple。 S4 使用map 转化为了list
42ms 可以通过
[(7, 4, 1), (8, 5, 2), (9, 6, 3)]
"""
class Solution3:
    def rotate(self, A):
        A[:] = zip(*A[::-1])
        return A
     
"""
S4: 
44 ms list 转化list 耗时
不必要使用map
"""
class Solution4:
    def rotate(self, matrix):
        #matrix[:] = map(list, zip(*matrix[::-1]))
        matrix[:] = list(zip(*matrix[::-1]))
        return matrix








if __name__ == '__main__':
    S = Solution3()
    ss =S.rotate([[1,2,3],[4,5,6],[7,8,9]])
    print(ss)





"""
Q: 将矩阵顺时针旋转90度。 

    ** ： 能够看做首先按照副对角线逆置， 然后按照水平线 翻转。 (或者先水平翻转然后主对角线转置)

    1. 不能额外分配空间, 原地转置， 注意   matrix[i][j] ,matrix[len_l-j][len_l-i] 


S2：  运行时间长


T ： 
    1. 将A 翻转： 
        A： 自己for 循环翻转
        B： A.reverse()
        C:  A[::-1]
    2. 主对角线翻转：
        A:  for for 两层循环
        B： 对A 简化为 列表生成式
        C： 使用zip() 
    3. 副对角线 转置： 
        A: 自己定义方法 for for

"""


