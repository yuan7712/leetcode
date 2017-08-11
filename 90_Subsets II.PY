"""
Given a collection of integers that might contain duplicates, nums, return all possible subsets.

Note: The solution set must not contain duplicate subsets.

For example,
If nums = [1,2,2], a solution is:

[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]

"""

"""
S1:
    迭代
    对78-S4 改进即可.
    [1,2,2] 
    1. 在每层添加该怎层元素时,如果该元素与之前数相同,则只需要对上层add 即组合添加即可.
        []
        [] [1]  --add 1
        [] [1] [2] [1,2] -- add 2
        [] [1] [2] [1,2] [2,2] [1,2,2] --add 2 ;此处只需要对上层添加的[2]  [1,2] 补充即可.
    2. 需要记录上层添加 集合数目;
T: 
    1. 预先对nums排序
    2. 此方法与leetcode类似
       https://discuss.leetcode.com/topic/3601/simple-iterative-solution/2
"""
class Solution1(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []
        nums.sort()
        ans = [[]]
        last = 2**31
        last_num = 0
        for i in nums: 
            if i != last :
                tmp = [k[:] for k in ans]
            else:  #add last_num 
                tmp = [ans[k][:] for k in range(len(ans)-last_num,len(ans))]
            last,last_num = i,len(tmp)
            [k.append(i) for k in tmp]
            ans.extend(tmp)
        return ans


"""
S2:
    迭代 -- leetcode 
    首先78中无重复数字时,每个数字只有两种状态,总的集合数目 2^n .但是如果出现重复数字时,不仅仅两种状态[1,2,2,2,3,3]
    此时可以将相同的数字看成一个组合[1,(2,2,2),(3,3)] 总数目：2*4*3   ;每个数字分别有2 4 3 中状态.
    所以基于此,我们对数字分组后,当添加该层数字时, 只需要对上一次层集合 分别添加不同状态个数该层数字即可.

    []
    [] [1]   --add 1
    [] [1] | [2] [1,2] | [2,2] [1,2,2] | [2,2,2] [1,2,2,2] --add 2 上层[] [1] 分别对它们添加1 2 3 个2 即可
    ...

T:
    1. python list extend(); 
        ans.extend(tmp) 由于tmp本身嵌套结构[[]...]; 所以extend后修改tmp仍会修改ans
        所以此处自行实现深度copy
R:
    https://discuss.leetcode.com/topic/4661/c-solution-and-explanation
"""
class Solution2(object):
    def subsetsWithDup(self, nums):
        if not nums: 
            return []
        nums.sort()

        ans = [[]]
        i = 0
        while i < len(nums) :   # 外层循环, 
            count = 0           # 计数,将重复数字整合
            for j in range(i,len(nums)):
                if nums[j] == nums[i]:
                    count+=1
                else: 
                    break

            # 对ans 每个开始分别添加 n<=count个数字
            tmp = [k[:] for k in ans]
            for k in range(count):  #循环分别添加 1 2 3 个2
                for m in tmp:
                    m.append(nums[i])
                ans.extend([k[:] for k in tmp])  # 深度copy tmp
            i += count
        return ans



"""
S3:
    递归 -- 与78-S2对应.
    稍加判断即可.
    [1,2,2]
    []
    [1]
        [1,2]
                [1,2,2]
        --2==2 pass
    [2]
        [2,2]

R:
    https://discuss.leetcode.com/topic/13543/accepted-10ms-c-solution-use-backtracking-only-10-lines-easy-understand/2
"""
class Solution(object):
    def subsetsWithDup(self, nums):
        ans = []
        path = []
        start = 0
        nums.sort()
        self.subs(nums,ans,start,path)
        return ans

    def subs(self,nums,ans,start,path):
        """
        nums : 原数组; ans: 总结果集 
        start: 起始位置.[1,2,3]  从2开始则求[2,3] subs
        path: 递归到此处path
        """
        tmp = path[:]
        ans.append(tmp)
        for i in range(start,len(nums)):
            # pass 掉重复的部分 [1,2,2] path[1] 此时只会和第一个2组合,第二个就不再组合  
            if i == start or nums[i] !=nums[i-1]:
                path.append(nums[i])
                self.subs(nums,ans,i+1,path)
                path.pop()
        return


"""
S4: 
    使用set 解决去重问题, 使用78中任一方法均可
"""


"""
S1 : 迭代 增量构造
S3:  递归  记录path, 模仿78-S3 也可以写类似dfs
                      http://www.cnblogs.com/TenosDoIt/p/3451902.html

S2： 此方法比较独特, 
与78中不一样. 78中二进制不适用.

"""
if __name__ == '__main__':
    S= Solution()
    ss =S.subsetsWithDup([1,2,2,2])
    print(ss)







