"""
3sum 
防止重复元组
"""
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        pre ,nums_len = 2**31-1 ,len(nums)
        left ,right = 0,0
        ans = []
        ans_pre = 2**31-1
        for i in range(len(nums)):
            if nums[i] == pre :
                continue
            pre = nums[i]
            ans_pre = 2**31-1
            left ,right = i+1,nums_len-1
            target = -1 * (nums[i])
            while left<right:
                if nums[left]+nums[right] < target :
                    while left< right and nums[left]+nums[right] <= target:   #此处必须添加 nums[left]+nums[right] <= target  防止00113 匹配sum为2时right向左忽略11
                        if nums[left]+nums[right] == target and nums[left]!= ans_pre:
                            ans.append([nums[i],nums[left],nums[right]])
                            ans_pre = nums[left]
                            left+=1
                            right-=1
                            break
                        left +=1
                elif nums[left]+nums[right] > target :
                    while left< right and nums[left]+nums[right] >= target:
                        if nums[left]+nums[right] == target and nums[left]!= ans_pre:
                            ans.append([nums[i],nums[left],nums[right]])
                            ans_pre = nums[left]
                            left+=1
                            right-=1
                            break
                        right-=1
                elif nums[left]!= ans_pre:
                    ans.append([nums[i],nums[left],nums[right]])
                    ans_pre = nums[left]
                    left+=1
                    right-=1
                else :
                    left+=1
                    right-=1
        return ans








"""
改进
"""
class Solution2(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()  #首先排序
        pre ,nums_len = 2**31-1 ,len(nums)  #pre记录上一个开始元素。
        left ,right = 0,0
        ans = []
        for i in range(nums_len):
            if nums[i] == pre :
                continue
            pre = nums[i]
            left ,right = i+1,nums_len-1
            target = -1 * (nums[i])
            while left<right:
                if nums[left]+nums[right] < target :  #当sum>target  left 的值应该变大，所以跳过重复数字，指向下一个大数
                    left+=1
#                    while left<right and nums[left]==nums[left-1]:
#                        left +=1
                elif nums[left]+nums[right] > target : #移动right指向下一个小数字
                    right -=1
#                    while left<right and nums[right]==nums[right+1]:
#                        right -=1
                else : #已经sum = target ,入ans, 移动left right
                    ans.append([nums[i],nums[left],nums[right]])
                    left +=1
                    while left<right and nums[left]==nums[left-1]:
                        left +=1
                    right -=1
                    while left<right and nums[right]==nums[right+1]:
                        right -=1

        return ans



if __name__ == '__main__':
    S = Solution2()
    ss = S.threeSum([-4,-2,1,-5,-4,-4,4,-2,0,4,0,-2,3,1,-5,0])
    print(ss)





"""
A : 1. 首先排序，然后依次固定每个开头，在剩余元素中找到 sum 为target 元素。
    2. 找剩余两个元素和时， 使用夹逼 从两边逼近，当sum>target  左边向右移动即可。
    3. sum = target  记录元素，同时防止重复出现。


S1： 1. 当找和为定值两个元素，会在此处一直while 直到找到。
     2. 重复元素判断 使用记录前驱元素判断


S2： 1. 每次判断sum 和target时只要移动 left 指向下一个larger数字即可，不必同S1 找到解。
     2. 找到 ans  后左右同时移动，全部指向下一个不同数字 防止 重复。
     3. ***


"""