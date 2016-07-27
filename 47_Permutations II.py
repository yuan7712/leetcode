"""
Given a collection of numbers that might contain duplicates, return all possible unique permutations.

For example,
[1,1,2] have the following unique permutations:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]

"""

"""
S1:
    迭代 --对46-S3修改
    46中[1,2,3]每次确定一个数字的位置, 上层[[1,2],[2,1]] 此层3分别插入不同位置
    1. 在此处重复元素时：
        [1,1,2,2]
         
"""
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
