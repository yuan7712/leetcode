"""


Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
the contiguous subarray [4,-1,2,1] has the largest sum = 6.

#求解最长字串(只要求值);  DP


"""




"""

S1: dp

 动态规划两个核心：  1. 划分子问题 找到最优子结构;  2. 重叠子问题;


最长字串都是以某位置为终点(或者起点);   所以可以将问题看做为  求以各个索引终止的最长的字串;  求出后o(n)遍历该数组即可；

s[-2,1,-3,4,-1,2,1,-5,4]; 

求以末尾结尾的 最长字串：  划分为子问题： 以4结尾 和 4单独作为字串；  【符合条件1  可以求出以4结尾的最长字串】

 2. 递推式： 以s[n]结尾的最长串  只需要知道 s[n-1]结尾的最长信息即可；

  f[n] = max(s[n] , s[n-1]+s[n])

 3. 存储： 如果仅仅是求以s[n]结尾的最长字串，那么只要 一个变量记录前驱即可;  
 但是此处 我们需要了解的是  任意位置结尾的 最长字串,  **所以采用n长数组记录**

4. 或者可以将求  这些不同位置结尾的最大值 合并到递推过程中， 这样也不必存储数组;



"""



class Solution1(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
       
        last  =  - (2**31-1)  
        ans = last    # MIN Int

        for i in nums:
            last = max(i+last , i)  # end with i;  last end with i-1
            ans = max(last,ans)

        return ans

    def maxSubArrayWithPath(self, nums):

        last  =  - (2**31-1)  
        ans = last    # MIN Int
        begin ,end  = -1,-1

        for i in range(0,len(nums)):
            tmp = max(nums[i]+last , nums[i])  # end with i;  last end with i-1
            if ans < tmp :   # update
                ans = tmp
                end = i
                if tmp == nums[i] :
                    begin = i

            last  = tmp

        print(str(begin) + "  ---->  "+ str(end))

        return ans




"""

S2: leetCode  非DP


和上面的DP 思路类似； 理解方式不一样而已。。。

还是可以把for(i in nums) 视为每次遍历该数字时，记录以该数字结尾的最大字串和;
     sum <=0 ： 即记录以i结尾最长字串和为i;    和S1 中  max(i+last ,i) 一样


R： https://discuss.leetcode.com/topic/7447/o-n-java-solution

"""


class Solution2(object):
    def maxSubArray(self, nums):

        ans  = - (2**31-1)   # min
        su = 0   # sum
        for i in nums:
            if su <= 0 :  # 以i结尾的最长序列为 i
                su = i
            else : 
                su += i
            ans = max(ans,su)
        print(ans)
        return ans





"""
S3:  暴力求解：

S3.1 :   求最长字串和, 最暴力的就是遍历所有case;  o(n^3) 【找到两个边界[i,j] 然后sum(i,j)】

S3.2 :   对3.1 稍做优化,空间换取时间; o(n^2) ; 【依然双层循环定边界[i,j], 计数使用空间换取时间; 创建一维数组m[i]记录0-i处累加和; 这样sum(i-j)复杂度变为o(1)】 


S3.3 :    基于3.2 继续改进;  o(n);
          3.2 中使用双层循环确定[i,j]复杂度过高;

          对于以j位置结尾的字串, total[j] 已经记录了sum(0...j) , 现在只要求出 以0开始的最小前缀和,  那么我们就能确定j位置为结尾的字串最大和；
          [0,1,2,3,....j]  

          而求最小前缀完全可以在遍历过程中迭代执行，没必要分配空间;

   
"""

class Solution3(object):
    def maxSubArray3_2(self, nums):
        """
        超时
        """


        if not nums :
            return -1

        total = [0]*len(nums)
        total[0] = nums[0]   
        for i in range(1,len(nums)):    # totoal[i] = sum(nums[0]...nums[i])   [0,i]
            total[i] = total[i-1] + nums[i]
        
        ans = -(2**31-1)
        for i in range(len(nums)):     #[i,j]
            for j in range(i,len(nums)):
                ans = max(ans,(total[j] - total[i] + nums[i]))  # sums([i,j])

        return ans
    

    def maxSubArray3_3(self, nums):

        total = [0]*len(nums)
        total[0] = nums[0]   
        for i in range(1,len(nums)):    # totoal[i] = sum(nums[0]...nums[i])   [0,i]
            total[i] = total[i-1] + nums[i]

        min_pre = 0
        ans =  -(2**31-1)
        for i in total: 
            tmp  = i - min_pre
            ans = max(ans,tmp)
            min_pre = min(min_pre,i)
        return ans 






"""
 
 1. DP S1
 2. 普通优化 ： S3 3.3
 
"""


if __name__ == '__main__':
    s = Solution3()
    print(s.maxSubArray3_3([-2,1,-3,4,-1,2,1,-5,4]))
    #import sys   
    #print( sys.maxsize)  2**63-1  py3;  py2:maxint
    