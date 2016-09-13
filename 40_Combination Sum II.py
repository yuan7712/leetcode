"""
Given a collection of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

Each number in C may only be used once in the combination.

Note:
All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
For example, given candidate set [10, 1, 2, 7, 6, 1, 5] and target 8, 
A solution set is: 
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
# 与38相比, C中可能重复,但是每个数字只能使用一次, 相比38更简洁.
"""

"""
S1:
    dfs
    元素重复问题 [1,1,2,5,6,7] target = 8 
    case : [1,7] [1,7]  [1,2,5] [1,2,5]
T: 
    [1,1,2,5,6,7]
        dfs([1],[1,2,5,6,7],7)  dfs([1],+[2,5,6,7],7)  dfs([2],[5,6,7],6)....  
        其中第二个必然会和第一个ans 重复.  第二种已经包含到第一种中,故Pass
            dfs([1,1],[2,5,6,7],6)...
        所以只要不和前一个一样就dfs, start除外
"""
class Solution1(object):
    def combinationSum2(self, candidates, target):
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
        if target == 0:
            ans.append(path)
            return
        if target<0:
            return
        for i in range(start,len(candidates)):  #add c[i]
            if i == start or candidates[i] != candidates[i-1]:  # i==start 而不是i==0
                self.dfs(candidates,ans,path+[candidates[i]],i+1,target-candidates[i])
        return


"""
S2:
    DP 类比38-S3  
    ***  当target 比较大时, 会非常低效, result 从target=1...n 记录
    [1,1,2,3,5,6,7] target = 8 
    由于每个元素只能使用一次, 所以每次add 一个元素, 
    add 1 ：  result[1]=(1)
    add 1 :   result[1]=(1)  result[2]=(1,1)
    add 2 :   result[1]=(1)  result[2]=[(1,1) (2)]  result[3] = (1,2)
    ... 如此一直到末尾
T： 
    此解法中, 关于重复元素,使用set()解决....
R:
    https://discuss.leetcode.com/topic/5777/dp-solution-in-python

"""
class Solution2(object):
    def combinationSum2(self, candidates, target):
        candidates.sort()
        table = [None] + [set() for i in range(target)]  #table[i]  target=i  result.  使用set 防止重复元素对
        for i in candidates:  #依次add 每个元素
            if i > target:
                break
            for j in range(target - i, 0, -1):  #当add 2时,target=8.  分别将2 试着添加到result= 0...6  table中
                table[i + j] |= {elt + (i,) for elt in table[j]}
            table[i].add((i,))    
        ans = map(list, table[target])  #{(2, 6), (1, 1, 6), (1, 2, 5), (1, 7)}   
        return list(ans)   #map 返回Iterable   list显示

"""
S3: 
    转换为90-Subset2[带重复元素的子集].  求出所有子集 sum==target  ans.append
    可以对90-S1 S2 稍加修改即可.
R:
    http://www.cnblogs.com/ganganloveu/p/4167175.html

"""



if __name__ == '__main__':
    S =Solution()
    ss = S.combinationSum2([10, 1, 2, 7, 6, 1, 5] ,8)
    print(ss)