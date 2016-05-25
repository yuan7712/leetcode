class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        left ,right = 0,len(nums)-1
        while left<=right :    #最后返回时 如果没有找到 left指向的是比target大的数字，right指向的是比target小的数字
            mid = (left+right)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] >target :
                right =mid -1
            else :
                left = mid +1
        return left

if __name__ == '__main__':
    S = Solution()
    ss = S.searchInsert([3],2)
    print(ss)                        
        



"""
二分查找：  [1,2,2,4,4,4,4,5,6,7] 3

 当找不到时： 倒数第三步时，left right 分别指向2 3 位置，即【2,4】，继续移动指向3位置的4. 继续right 就会指向小于4的2。

  所以 当找不到时，left指向的始终是比target大的数字位置，right指向的是比target小的数字。 
  倒数第二步二者指向同一个位置(如果连续数字4 只能指向边缘某一个，不会是中间处)


变形：  33题
"""        