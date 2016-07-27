"""
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.
For example,

Consider the following matrix:

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
Given target = 5, return true.

Given target = 20, return false.

"""


"""
S1: 
   每行依次折半,但是列数每次不是全部列, 
   例如查找5,第一次找到4 7 ; 下次在第二行折半 只需在 2-5即可.
   使用column 定每行 high 上界

T: 
    此种解法 当我们查找30 时候,则需要对每行折半
"""
class Solution1(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        row , column = len(matrix), len(matrix[0])

        for i in range(row) : 
            low , high = 0,column-1
            while low <= high : 
                mid = (low+high)//2
                if matrix[i][mid] == target:
                    return True 
                elif matrix[i][mid] > target:
                    high = mid -1
                else : 
                    low = mid +1
            # high <=target;
            column = low   #列数
        return False


"""
S2: 
    每次与右上角元素比较：
    target == 15 ： return True
    15 <target  : row +=1, 1-14 忽略
    15 > target : column-=1 19-30 忽略

T： 
   此种方法每次能够越减元素
R：
    https://discuss.leetcode.com/topic/20064/my-concise-o-m-n-java-solution

"""
class Solution(object):
    def searchMatrix(self, matrix, target):
        if not matrix: 
            return False
        row , column = 0, len(matrix[0])-1

        while column >=0 and row <len(matrix):
            if target == matrix[row][column]:
                return True
            elif target < matrix[row][column]:
                column -=1
            else:
                row +=1
        return False
