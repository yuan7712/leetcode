"""
Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

For example,
If n = 4 and k = 2, a solution is:

[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]

"""



"""
S1:
    递归
"""
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        ans = []
        start = 0
        nums = [i+1 for i in range(n)]
        self.pers(nums,ans,k,start)
        return ans

    def pers(self,nums,ans,k,start):
        if k == 1 :
            return [[nums[i]] for i in range(start,len(nums))]



if __name__ == '__main__':
    S =Solution()
    ss = S.combine(4,2)
    print(ss)

