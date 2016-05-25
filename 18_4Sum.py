class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        nums_len = len(nums)
        pre1 , pre2 = 2**31-1,2**31-1
        left , right = 0,0
        ans = []
        for i in range(nums_len-3):
            if nums[i] == pre1:
                continue
            pre1 = nums[i]
            pre2 = 2**31-1
            for j in range(i+1,nums_len-2):
                if nums[j] == pre2:
                    continue
                pre2 = nums[j]
                left ,right = j+1,nums_len-1
                while left<right:
                    my_sum = nums[i]+nums[j]+nums[left]+nums[right]
                    if my_sum < target : #left->
                        left += 1
                    elif my_sum > target: #right <-
                        right-= 1
                    else : #append ans
                        ans.append((nums[i],nums[j],nums[left],nums[right]))
                        left +=1
                        while left<right and nums[left]==nums[left-1]:
                            left +=1
                        right -=1
                        while left<right and nums[right]==nums[right+1]:
                            right-=1
        return ans




if __name__ == '__main__':
    S = Solution()
    ss =S.fourSum([1, 0 ,-1, 0 ,-2, 2],0)
    print(ss)








"""
A ： 
    和3sum类似 O(n^3) 分别固定前两个(同时防止重复数字)，最后两位数之和夹逼。
    

Q: Runtime: 1384 ms ,耗时长
"""