class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        nums_len = len(nums)
        left , right = 0,0
        pre = 2**31 -1
        ans =2**31-1

        for i in range(nums_len):
            if nums[i] == pre:
                continue
            pre = nums[i]
            left , right = i+1,nums_len-1
            while left < right :
                m_sum = nums[left]+nums[right]+nums[i]
                if abs(m_sum - target) < abs(ans-target):
                    ans = m_sum
                if m_sum < target :
                    left+=1
                    while left<right and nums[left]==nums[left-1]:
                        left +=1
                elif m_sum > target : 
                    right -=1
                    while left<right and nums[right]==nums[right+1]:
                        right -=1
                else :
                    return target
        return ans


if __name__ == '__main__':
    S =Solution()
    ss = S.threeSumClosest([1,1,1,0],100)
    print(ss)


        



"""
A: 15_3sum 变形

 题目假定只有一个符合要求，只要返回最接近target sum 即可。
    1. 在3sum 基础上只要记录ans 使之和 target abs 最小即可.

Q : 
    1. 为何left++  right-- 后保证不会缺少组合？
        当left++ 向右移动时，(sum<=target) 
        1 2 3 4 5 6 7 8 9  例如sum13 时候，right=9 left =1
        当left 向右时sum只会越来越接近13,1 2与 7 8 sum 必然比9 和3 小

    2. 同理right
"""        