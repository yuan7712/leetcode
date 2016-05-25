class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        nums_l = len(nums)
        i = 0
        while i < nums_l :
            nums[ans] = nums[i]
            ans += 1
            i += 1
            while i <nums_l and nums[i]==nums[i-1] :
                i += 1
        return ans



class Solution2(object):
    def removeDuplicates(self, nums):
        new_len = 0
        for num in nums:
            if new_len < 1 or num > nums[new_len - 1]:
                nums[new_len] = num
                new_len += 1
        return new_len




if __name__ == '__main__':
    S = Solution()
    ss = S.removeDuplicates([])
    print(ss)    




"""
 一次遍历，记录sum ,遇到不同数值时前置。(将当前数字和前序比较)
S2 中， 是将当前数字和 new_len 标记的数字比较
"""