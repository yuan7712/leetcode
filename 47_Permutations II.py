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
    迭代  --未完成
    --对46-S3修改
    46中[1,2,3]每次确定一个数字的位置, 上层[[1,2],[2,1]] 此层3分别插入不同位置.
    [1,1,1,2,2,3,3] 
    1. 在此将相同数字划分为一组.[(1,1,1),(2,2),(3,3)]
        []
        [1,1,1]   -- add 1 到[]中, 只有一种
        [...] 10种可能,  add[2,2] 到[1,1,1];  即如何将[2,2]放到4个空格处
                        a + b + c + d = 2  => 共有10种
        [...] --add [3,3]

Q: 
    1. 在将[2,2] add 到[1,1,1]的4个位置时, 未找到合适方法.

"""
class Solution1(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        return None
 


"""
S2: 
    递归 

"""
class Solution(object):
    def permuteUnique(self, nums):
 