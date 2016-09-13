"""
Given a set of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

The same repeated number may be chosen from C unlimited number of times.

Note:
All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
For example, given candidate set [2, 3, 6, 7] and target 7, 
A solution set is: 
[
  [7],
  [2, 2, 3]
]
 找到所有sum = target 组合. 元素可以复用. 全部正数.
"""



"""
S1:
    dfs 
    dfs([2,3,6,7],7) = dfs([],[2,3,6,7],7) + dfs([2],[3,6,7],5) +dfs([2,2],[3,6,7],3)+dfs([2,2,2],[3,6,7],1) 
    分别放0  1 2 3 个2... 依次. 记录path

T:  
    lintcode [2,2,3] Error.  leetcode未验证重复数字
    Error Case : [2,2,3],7   -> [[2, 2, 3], [2, 2, 3], [2, 2, 3]]
    重复元素问题

    关于path记录, 不修改path,传入新的副本,无须pop.  path[2,2,3]
    self.dfs(candidates,ans,path+[candidates[start]]*i,j,target-i*candidates[start])
    if target == 0:  
        ans.append(tmp)
        return 
"""
class Solution1(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        ans = []
        self.dfs(candidates,ans,[],0,target)
        return ans 

    def dfs(self,candidates,ans,path,start,target):
        if target == 0:  #[[],[3,3],[4]] ->[3,3,4]
            tmp = []
            for i in path:
                tmp.extend(i) 
            ans.append(tmp)
            return
        if start>=len(candidates) or candidates[start] > target :  #先判断target==0
            return   
        j = start+1  #next  重复元素问题
        while j < len(candidates) and candidates[j]==candidates[j-1] :
            j +=1
        i = 0
        while i * candidates[start] <=target:
            path.append([candidates[start]]*i)
            self.dfs(candidates,ans,path,j,target-i*candidates[start])
            path.pop()
            i+=1
        return

"""
S2:
    leetcode dfs
    *** 此未验证 带有重复元素
    dfs([2,3,5,7],7) = dfs([2],[2,3,5,7],5) +dfs([3],[3,5,7],4)+dfs([5],[5,7],2)+dfs([7],[7],0)
    此方法分别选择以 2 3 5 7 开始的ans递归.
    path 每次传递新的数组, 所以无须pop恢复.
R: 
    https://discuss.leetcode.com/topic/23142/python-dfs-solution
    https://discuss.leetcode.com/topic/7698/java-solution-using-recursive
"""
class Solution2(object):
    def combinationSum(self, candidates, target):
        res = []
        candidates.sort()
        self.dfs(candidates, target, 0, [], res)
        return res
    
    def dfs(self, nums, target, index, path, res):
        if target < 0:
            return  # backtracking
        if target == 0:
            res.append(path)
            return 
        for i in range(index, len(nums)):
            self.dfs(nums, target-nums[i], i, path+[nums[i]], res)


"""
S3:
    leetcode DP迭代
    *** 未验证重复元素
    [2,3,5,7] , 7 此种方法会保存target 1-7 的result
    target = 1:  []
             2:  [2]
             3:  [3]
             4:  [2,2]
             5:  [2,3]  # 此种方法分别计算target=i result.使用之前的记录.
            target = 5, 我们分别添加2 3 4 5 分别需要result(5-2)  result(5-3)  result(5-4)  result(5-5).  我们只要将2 3 4 5分别与之前result组合即可.
    注意:
          target=5   2+result(3) -[2,3] 和 3+result(2)-[3,2]  重复 
             此处可以加以判断使result中増序, 如[3,2] 此种  丢弃即可.
R：
    https://discuss.leetcode.com/topic/8200/iterative-java-dp-solution
"""
import copy
class Solution(object):
    def combinationSum(self, candidates, target):
        candidates.sort()
        dp  = [[] for i in range(target+1)]  # dp[i]   target=i  result. dp[0]=[[]]
        dp[0].append([])
        for i in range(1,target+1):  # form 1 to target
            for j in candidates:   # add j   so match dp[i-j]  result==i-j
                if j > i :
                    break
                else:  #dpi-j] +j
                    tmp = copy.deepcopy(dp[i-j])
                    for k in tmp :
                        if len(k)==0 or k[-1]<= j:   # asc  保证result中増序 防止重复
                            k.append(j)
                            dp[i].append(k)
        return dp[-1]




        

if __name__ == '__main__':
    S= Solution()
    ss = S.combinationSum([2,3],5)
    print(ss)
