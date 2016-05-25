class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        new_len = 0
        new_i_sum = 0  #新list中i数字个数
        for num in nums :
            if new_len < 1 or num > nums[new_len - 1]:  #当开始处或者 大数字 add
                nums[new_len] = num
                new_len += 1
                new_i_sum = 1
            elif num == nums[new_len - 1] and new_i_sum <2:
                nums[new_len] = num
                new_len += 1
                new_i_sum +=1
        return new_len




class Solution2(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        new_len = 0
        new_i_sum = 0  #新list中i数字个数
        i = 0
        while i < len(nums):
            nums[new_len] = nums[i]
            new_i_sum =1
            new_len+=1
            i +=1
            while i < len(nums) and nums[i]==nums[i-1]:
                if new_i_sum <2:
                    nums[new_len] = nums[i]
                    new_len +=1
                    new_i_sum+=1
                i+=1
        return new_len

if __name__ == '__main__':
    S = Solution2()
    ss = S.removeDuplicates([1,1,2,2,2,2])
    print(ss)



"""
 与26题相比，只需要判断重复数字个数即可，此处允许两个数字重复。
"""