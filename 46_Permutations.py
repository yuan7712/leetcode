"""
Given a collection of distinct numbers, return all possible permutations.

For example,
[1,2,3] have the following permutations:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]

"""

"""
S1: 
    递归
    不同数字,排列组合 n!种
    1. 如果使用切片,递归则会造成较大运算,[1,2,3] 当此次选择1 后递归[2,3]... 这样较复杂,所以使用stat数组表示每个元素被选中状态
    2. 注意 当到达末尾层次时 return [[]]

T:
    [1,2,3]   stat:[T,T,T]

    1. [F,T,T]   --[1,2,3] [1,3,2] 
                [F,F,T]     --[2,3]
                            [F,F,F]     --[[3]]
                [F,T,F]     --[2,3]
                            [F,F,F]     --[[3]]                  
    2. [T,F,T]
    3. [T,T,F]


"""
class Solution1(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        stat = [True for i in range(len(nums))]  #和nums对应 表示每个元素是否可被选择
        ans = self.pers(nums,stat,0)
        return ans

    def pers(self,nums,stat,step):
        """
        nums : 原数组, 不修改
        stat : 和nums对应bool,表示每个元素是否被选中
        step : 层次, 当到了末层后直接 返回[[]]
        该函数 对nums 中的非F项, 返回所有组合. 如果到达末层则返回[[]]
        """
        if step == len(nums):     # 此处如果末层返回[]则 return后不能add元素. [3]
            return [[]]
        ans = []
        for i in range(len(nums)):
            if stat[i] == True:   #从前到后依次使用每个数值, 并标记为 False. 使用完毕后 重置True
                stat[i] = False
                tmp = self.pers(nums,stat,step+1)
                [k.append(nums[i]) for k in tmp]
                ans.extend(tmp)
                stat[i] = True
            else: 
                pass
        return ans


"""
S2: 
    递归 -- leetcode方
法    此方法较巧妙,通过swap,每次确定第N个数字,当此种组合输出后,swap还原. 
    例： [1,2,3]  swap(1,2)->[2,1,3] 此时2 确定继续判断[1,3]组合. 待2开头全部组合输出后,swap(1,2)->[1,2,3]; 继续swap(1,3)计算以3开头

    当到达末层时 将此事数组中数字全部输出即一个组合. 然后swap恢复原样,以备下次swap.
R： 
    https://discuss.leetcode.com/topic/5881/my-elegant-recursive-c-solution-with-inline-explanation
"""
class Solution2(object):
    def permute(self, nums):
        ans = []
        start = 0
        self.pers(nums,start,ans)
        return ans

    def pers(self,nums,start,ans):
        """
        nums : 此函数会对nums数组修改, 
        start: 表示当前从第几个数字开始. [1,2,3,4] start = 1 表示1已确定. 只要分别swap(2,2) (2,3)(2,4)即可.
               start 到达末层时： 直接输出即为一种组合. start=4   [1,2,3,4]
        ans: 全局结果集
        """
        if start == len(nums):  #末层
            ans.append(nums[:])
            return 
        for i in range(start,len(nums)): #start之后的位数还未确定, nums[start]分别选择之后的几个候选.使用完毕后还原swap
            nums[start] , nums[i] = nums[i], nums[start]
            self.pers(nums,start+1,ans)  #确定nums[start],继续判断下一位 start+1
            nums[start] , nums[i] = nums[i], nums[start]  # 还原
        return 


"""
S3: 
    迭代
    [1,2,3]此种方法是一个数字一个数字来确定. 
    1. 首先确定1 -> [1] 一种
    2. 确定2 -> [2,1] [1,2]  2种. 2能放到[1]两个位置
    2. 确定3 -> 3对于上面的2种,每种有3个位置  共6种. 分别放到不同位置即可

    基于以上, 分为两步, 分别对上层的每种组合([1,2] [2,1]), 在该层将此层数字添加到不同位置.->[3,1,2] [1,3,2] [1,2,3]  ...(另3种)

R: 
    https://discuss.leetcode.com/topic/6377/my-ac-simple-iterative-java-python-solution/2
"""
class Solution(object):
    def permute(self, nums):

        pre = [[]]
        for i in range(len(nums)):
            tmp = []
            for j in pre:
                for k in range(len(j)+1):  #[1,2,3] 长度为1, add 4 时可以放4个位置
                    tmp.append(j[0:k]+[nums[i]]+j[k:]) #不同位置insert
            pre = tmp   #保留上层状态, 下层继续迭代
        return pre



if __name__ == '__main__':
    S= Solution()
    ss =S.permute([1,2,3])
    print(ss)

















