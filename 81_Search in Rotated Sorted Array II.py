class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        left ,mid ,right = 0,0,len(nums)-1
        while left <= right :
            mid = (left+right)//2
            if nums[mid] == target:
                return True
            if nums[left]<nums[mid] :    # 左侧一定増序
                if target< nums[mid] and target>= nums[left]:  #转向左侧连续区域
                    right = mid -1
                else :    #转向右侧， 可能包含 枢纽点
                    left = mid +1
            elif nums[left]==nums[mid] :  # 不能判断 左右那个増序， left++
                    left = mid +1
            else :  #左侧非连续 递增。 右侧为递增
                if target > nums[mid] and target <= nums[right] :   # 属于右侧
                    left = mid + 1
                else: # 不属于右侧只能向左
                    right = mid -1

        return False



if __name__ == '__main__':
    S = Solution()
    ss = S.search([1,1,3,1],3)
    print(ss)            






"""
Q : 此题和33 题目相比 ，主要是要处理重复数字问题  [1,1,1,3,1,1,1]  [1,1,1,1,3,3,3,1]  
 
   基本思路与33一致， 判断mid 后选择向左还是向右。
   1. 当 nums[left]<nums[mid]  无疑 左侧为増序
   2. 当 nums[left] >nums[mid]  右侧为増序
   3. 当 nums[left]= nums[mid]  ：  此时主要判断 如何 选择向左还是向右.

        此时我们无法判断左侧还是右侧是増序(只能遍历一侧，此种不可行)； 
        所以此处因为left = mid ，所以可以将left 一步步向右 直到左侧増序 或者右侧増序 (L20)

 

Error : 
        [1,1,3,1],3
        [1,3,1,1,1]3
"""