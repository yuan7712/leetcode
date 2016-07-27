"""
Given an unsorted integer array, find the first missing positive integer.

For example,
Given [1,2,0] return 3,
and [3,4,-1,1] return 2.

Your algorithm should run in O(n) time and uses constant space.

"""


"""
S1: 
     使用桶排序. 从前到后每次将数字放到对应下标的位置. 
     1. 忽略<=0 &&  数值过大的  数字.
     2. 再次遍历从前到后找 首个与下标不符的数字.

T: 
    1. swap. nums[i],nums[nums[i]-1]   error ,先将nums[i] 提出
    2. 使用while.  由于swap后 后面数字可能提前,所以保证交换后该数字 在对应位置,while
    3. while 中跳出判断,
                nums[i] >nums_len 、nums[i] <= 0、nums[i] == i+1 、nums[i] == nums[nums[i]-1] 
                最后一项注意： 防止[1,1] 死循环

"""
class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_len = len(nums)

        for i  in range(nums_len): 
            while nums[i] != i+1: 
                if   nums[i] > nums_len or nums[i] <= 0 or nums[i] == nums[nums[i]-1]:  # 最后判断  防止死循环
                    break
                tmp = nums[i]
                nums[i],nums[tmp-1] = nums[tmp-1],nums[i]   #swap

        for i in range(nums_len): 
            if nums[i] != i+1:
                return i+1
        return nums_len +1


"""
整合该即以上
    for i in range(nums_len): 
        if nums[i] > nums_len or nums[i] <= 0 or nums[i] == i+1: 
            continue
        # case  swap 
        while nums[i] != i+1: 
            if nums[i] > nums_len or nums[i] <= 0 or nums[i] == i+1 or  nums[i] == nums[nums[i]-1]:
                break 
            else: 
                swap ()
"""


if __name__ == '__main__':
    S =Solution()
    ss = S.firstMissingPositive([3,4,-1,1])
    print(ss)

