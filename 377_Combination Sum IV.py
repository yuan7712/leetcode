"""
Given an integer array with all positive numbers and no duplicates, find the number of possible combinations that add up to a positive integer target.

Example:

nums = [1, 2, 3]
target = 4

The possible combination ways are:
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)

Note that different sequences are counted as different combinations.

Therefore the output is 7.
Follow up:
What if negative numbers are allowed in the given array?
How does it change the problem?
What limitation we need to add to the question to allow negative numbers?

# 和39 combinations 相比, 元素顺序不同  也是不同组合.

"""


"""
S1: 
    未通过
    39-S2  修改dfs后依然从头开始选择数字即可
T：
    超时：[1,2,4] 32 -> 39882198 [Finished in 120.9s]
"""
class Solution1(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int   返回数目即可
        """
        #ans = []
        nums.sort()
        return self.dfs(nums,target)
        

    def dfs(self,nums,target):
        if target < 0:
            return 0
        if target == 0:
            #ans.append(path)
            return 1
        ans = 0
        for i in range(0,len(nums)):  # 修改起始位置为0
            ans+=self.dfs(nums,target-nums[i])
        return ans

"""
S2:
    AC  ***
    dfs 递归中会出现许多重复性计算 
    dfs(nums,target1) 添加map 如果map存在则不再递归
T:
    DFS 中使用dict缓存加速
R：
    https://discuss.leetcode.com/topic/52255/java-recursion-solution-using-hashmap-as-memory
"""
class Solution(object):
    def combinationSum4(self, nums, target):
        nums.sort()
        my_cict = {}
        return self.dfs(nums,target,my_cict)
        
    def dfs(self,nums,target,my_cict):
        if target < 0:
            return 0
        if target == 0:
            #ans.append(path)
            return 1
        if my_cict.get(target, -1) !=-1:  #exist
            return my_cict[target]
        ans = 0
        for i in range(0,len(nums)):  # 修改起始位置为0
            ans+=self.dfs(nums,target-nums[i],my_cict)
        my_cict[target] = ans
        return ans


"""
S3:
    DP 
    模仿39-S3,不同之处:39 故意使 组合増序 防止重复元素.此处不限重复 去除限制即可.

    [1,2,4] target = 32
    target = 1: [1]    1
             2: [1,1] [2]   2 == 1+target[1] , 2+target[0] [1+1]
             3: [1,1,1] [1,2] + [2,1]  3 == 1+target[2] ,2+target[1]  [3=2+1]
             4: [1,1,1,1] [1,1,2] [1,2,1] +[2,1,1] [2,2] +[4]   6== 1+target[3] ,2+target[2],4+target[0]

"""
class Solution3(object):
    def combinationSum4(self, nums, target):
        nums.sort()  # sort 在内层循环j>i 时就不再继续向后, 否则修改内层if判断
        dp = [1]+[0]*target   #dp[i]  target=+1 result 个数
        for i in range(1,target+1):  
            for j in nums:
                if j > i :
                    break
                else:
                    dp[i]+=dp[i-j]
        return dp[-1]


"""
S4:
    与S3 类似DP
    dp[i+num] += dp[i]

T： 
    [1,2,4] target=32 
    target[0] + 1,2,4   修改 target[1] [2]  [4]
    target[1] + 1,2,4   修改 target[2] [3]  [5]
    ....
R:
    https://www.hrwhisper.me/leetcode-combination-sum-iv/
"""
class Solution4(object):
    def combinationSum4(self, nums, target):
        dp = [1] + [0] * target
        for i in range(target + 1):
            for x in nums:
                if i + x <= target:
                    dp[i + x] += dp[i]
        return dp[target]



if __name__ == '__main__':
    S =Solution()
    ss =S.combinationSum4([1,2,4],7)
    S1 =Solution3()
    ss1 =S1.combinationSum4([1,2,4],7)
    print(ss)
    print(ss1)