"""
Given a sorted array of integers, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

For example,
Given [5, 7, 7, 8, 8, 10] and target value 8,
return [3, 4].

"""



"""
S1: 
    1. 折半找value
    2. 左右扩展

"""
class Solution1(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        loc = self.binarySearch(nums,target)
        if loc == -1 : 
            return [-1,-1]
        left , right  = loc , loc 
        while left >=0 and nums[left] == nums[loc]: 
            left -= 1
        while right <= len(nums)-1 and nums[right] == nums[loc]:
            right +=1
        return [left+1,right-1]

    def binarySearch(self,nums,key):
        """
        折半查找 
        """
        low , high = 0,len(nums)-1 
        while low <= high : 
            mid = (low+high)//2   # int mid = low + ((high - low) >> 1);
            if nums[mid] == key:
                return mid
            elif nums[mid] > key : 
                high = mid -1
            else: 
                low = mid + 1
        return -1


"""
S2: 
    [5, 7, 7, 8, 8, 10] 在找8边界时, 分别找8左边界和9左边界.(对折半查找稍微修改,mid变化)

R: 
    https://discuss.leetcode.com/topic/6327/a-very-simple-java-solution-with-only-one-binary-search-algorithm
    https://discuss.leetcode.com/topic/5891/clean-iterative-solution-with-two-binary-searches-with-explanation/2

"""
class Solution(object):
    def searchRange(self, nums, target):
        left , right = 0,len(nums)-1
        ans = [-1,-1]
        if not nums: 
            return ans
        # 找 target 左边界
        while left < right : 
            mid = (left+right)//2  # mid偏左
            if nums[mid] <target : 
                left = mid+1
            else:  # 即使== 时 right 逐步退
                right = mid
        if nums[left] != target: 
            return ans
        ans[0] = left

        # 找右边界
        right = len(nums)-1
        while left < right:  #left 左边界
            mid = (left+right)//2 +1   # mid 偏右 [5,5,5] 否则死循环；因为==时设置left不动
            if nums[mid] > target:
                right = mid -1
            else: 
                left = mid
        ans[1] = right
        
        return ans
 

