"""
Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.


Example 1:

Input: k = 3, n = 7

Output:

[[1,2,4]]

Example 2:

Input: k = 3, n = 9

Output:

[[1,2,6], [1,3,5], [2,3,4]]

#使用[1,2,3,4,5,6,7,8,9] sum= target 每个数字只能使用1次, 由k个数组成.
** 等价于77 Combinations  求C n k .  + 判断sum
"""



"""
S1:
   77-S2 dfs 加sum 判断.  
"""
class Solution1(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        ans = []
        self.dfs(ans,[],1,k,n)
        return ans

    def dfs(self,ans,path,begin,k,n):
        """
        end = 9
        """
        if 10-begin < k :
            return 
        if k == 0 :
            if sum(path) == n :
                ans.append(path[:])
            return 
        path.append(begin)
        self.dfs(ans,path,begin+1,k-1,n)
        path.pop()
        self.dfs(ans,path,begin+1,k,n)
        return

"""
S2: 
    简化
R: 
    https://discuss.leetcode.com/topic/37962/fast-easy-java-code-with-explanation
"""
class Solution(object):
    def combinationSum3(self, k, n):
        ans = []
        self.dfs(ans,[],1,k,n)
        return ans

    def dfs(self,ans,path,start,k,target):
        """
        start: 起始位置 序列[1,2,3,4,5,6,7,8,9] start=i dfs之后序列
        k: 需要数字个数
        target: 目标sum
        """
        if k < 0 or target<0:
            return
        if k == 0 and target == 0 :
            ans.append(path[:])
            return 
        for i in range(start,10):
            path.append(i)
            self.dfs(ans,path,i+1,k-1,target-i)
            path.pop()
        return 

if __name__ == '__main__':
    S =Solution()
    ss =S.combinationSum3(3,9)
    print(ss)



