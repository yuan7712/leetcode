"""
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
For example,

Consider the following matrix:

[
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
Given target = 3, return true.

"""


"""
S1: 
    分两步,每步均使用折半
    1. 定位行
    2. 从改行查找

"""
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        low , high = 0,len(matrix)-1
        # <= target
        while low <= high: 
            mid = (low + high)//2
            if matrix[mid][0] == target : 
                return True 
            elif matrix[mid][0] >target:
                high = mid -1
            else:
                 low = mid+1
        # high,指向<= target 所在行
        left ,right = 0,len(matrix[high])-1
        while left <= right:
            mid = (left+right)//2
            if matrix[high][mid] == target:
                return True
            elif matrix[high][mid] >target:
                right = mid -1
            else:
                left = mid +1
        return False



"""
S2: 
    直接折半,不分两步; 计算总的数字个数, 按照数字个数获取索引
first , last = 0, m*n
int mid = first + (last - first) / 2;
int value = matrix[mid / n][mid % n];

"""