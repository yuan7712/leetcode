"""
Given a set of distinct integers, nums, return all possible subsets.

Note: The solution set must not contain duplicate subsets.

For example,
If nums = [1,2,3], a solution is:

[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]

"""


"""
S1: 
    递归  --增量构造

    [1,2,3] =>[1]+ {[],[2],[3],[2,3]}

T: 
    注意在python 中各种问题
    1.  ans 涉及双层嵌套, 不能简单[:]浅层copy, 应该深度copy,  或者调用相应函数
    2. list 操作  append  extend 不返回值,原地操作 返回None

R: 
    leetcode 多种方法
    https://discuss.leetcode.com/topic/19110/c-recursive-iterative-bit-manipulation-solutions-with-explanations/2
    http://www.cnblogs.com/TenosDoIt/p/3451902.html    #与此中S2类似
"""
class Solution1(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []
        if len(nums) ==1:
            return [[],nums]
        sub = self.subsets(nums[1:])
        #ans = sub[:]   #此处需要深度copy 不能简单 sub[:]
        ans = [i[:] for i in sub]
        [i.append(nums[0]) for i in sub]   #i.append(0) 返回值 None
        ans.extend(sub)   # extend 原地操作, 返回None
        return ans

"""
S2: 
    递归 
    []
    [1]  
        [1,2] 
            [1,2,3] 
        [1,3]
    [2]
        [2,3]
    递归分别计算从每个开始的,先将1push, 以1开头弄完后pop
R:
    https://discuss.leetcode.com/topic/13543/accepted-10ms-c-solution-use-backtracking-only-10-lines-easy-understand

"""
class Solution2(object):
    def subsets(self, nums):
        ans = []
        path = []
        start = 0
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
            path.append(nums[i])
            self.subs(nums,ans,i+1,path)
            path.pop()
        return



"""
S3: 
    递归 -- 位向量  dfs
    与S2 类似, 只是在递归时 
            S3： [1,2,3]   分为选or 不选1, 记录path
            S2:  [1,2,3]   分为选1 or 2 or 3 .记录path
    [1,2,3] 总共2^3 = 8 种, 即可以记录每个元素是否被选择.

            1:      1
                  Y/ \N
            2:    2   2
                 / \ / \
            3:  3  3 3  3
               /\ /\ /\ /\
    1. 递归一直向下, 设置T F 传递
    2. 当到达最末层时, add result

T: 
    1. ans stat 全局修改
R: 
    http://www.cnblogs.com/TenosDoIt/p/3451902.html    #于此中S1类似dfs

"""
class Solution3(object):
    def subsets(self, nums):
        if not nums:
             return []
        ans = []
        step = 0
        stat = [False]* len(nums)
        self.subs(nums,ans,stat,step)
        return ans

    def subs(self,nums,ans,stat,step):
        """
        ans : 最终结果集
        stat： 各个数值是否被选 T or F.  list
        step:  层数, 到达末尾层, out result

        """
        if len(nums) == step:
            tmp = [nums[i] for i in range(len(nums)) if stat[i]]
            ans.append(tmp)
            return ans
        stat[step] = False
        self.sub(nums,ans,stat,step+1)
        stat[step] = True
        self.sub(nums,ans,stat,step+1)
        return ans


"""
S4: 
    迭代 --按照S1 方法迭代

T : 
    每次保存上次集合.添加本层元素即可
"""
class Solution4(object):
    def subsets(self, nums):
        if not nums:
            return []
        ans = [[]]

        for i in nums:
            tmp = [k[:] for k in ans]
            [k.append(i) for k in tmp]
            ans.extend(tmp)
        return ans


"""
S5: 
    Bit Manipulation 二进制法
    [1,2,3] 子集: 每个元素有取或不取 两种状态.  总共2^3种.
    1. 使用0-7 的二进制分别表示 每种组合. 000 -111
    2. 每次将二进制中非0位取出, 111 ->  [1,2,3]
"""
class Solution5(object):
    def subsets(self, nums):
        if not nums : 
            return []
        ans = []
        nums_len = len(nums)
        for i in range(2**nums_len):
            tmp = []
            # 判断二进制非0
            for j in range(nums_len):
                if 1 << j & i : 
                    tmp.append(nums[j])
            ans.append(tmp)
        return ans


"""
S6: 
    Bit Manipulation 二进制法
    与S4 一样.  也是将各个状态表示为 int 的每一位.
    1. 与S4 相比, 内外层循环改变. 
    2. 判断某位是否为1 , 位运算即可

    [], [], [], [], [], [], [], []
    
    [], [1], [], [1], [], [1], [], [1]   #从0-7 判断在0号位是否为1; add 1
    
    [], [1], [2], [1, 2], [], [1], [2], [1, 2]  # 从0-7 判断第1位是否为1
    
    [], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]  #从0-7 判断第3位是否为1     
R:
    https://discuss.leetcode.com/topic/19110/c-recursive-iterative-bit-manipulation-solutions-with-explanations/2

"""

class Solution6(object):
    def subsets(self, nums):
        if not nums: 
            return []
        nums_len = len(nums)
        ans = [[] for i in range(2**nums_len)]
        for i in range(nums_len):
            # 当 i =0 判断首位是否为1; 0-7 对应8中状态，7最后一位1 所以add 1
            for j in range(2**nums_len):    
                if j >> i & 1:   #判断该位
                    ans[j].append(nums[i])
        return ans 









        




"""
S1: 增量
S4：  S1 增量迭代

S3：dfs  S2 类似
S5 S6 ：二进制

"""



if __name__ == '__main__':
    S =Solution()
    ss =S.subsets([1,2,3])
    print(ss)