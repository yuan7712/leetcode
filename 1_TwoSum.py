# error twoSum([3,3,4],6) ,nums.index应该从后向前，自己定义方法。N2
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i ,value in enumerate(nums):
            if (target - value) in nums:
                index = nums.index(target - value )
                if i!=index :
                    if(i<index):
                        return [i,index]
                    else:
                    	return [index,i]



#R2，使用Map,保存value和index 映射。
class Solution2:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        map = dict()
        size = len(num)
        for x in range(size):
            map[num[x]] = x
        for x in range(size):
            idx1 = x
            idx2 = map.get(target - num[x])
            if idx2:
                return idx1 , idx2 




if __name__ == "__main__":
    s = Solution()
    ss = s.twoSum([3,3,4],6)
    print(ss)