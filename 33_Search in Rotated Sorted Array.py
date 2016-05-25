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
                return mid
            if nums[left]<=nums[mid] :    #左侧为连续片段   ||| 此处= 号，必须包含 如果没有else 中右侧将不一定是连续的升序。
                if target< nums[mid] and target>= nums[left]:  #转向左侧连续区域
                    right = mid -1
                else :    #转向右侧， 可能包含 枢纽点
                    left = mid +1
            else :  #左侧非连续 递增。 右侧为递增
                if target > nums[mid] and target <= nums[right] :   # 属于右侧
                    left = mid + 1
                else: # 不属于右侧只能向左
                    right = mid -1

        return -1








if __name__ == '__main__':
    S = Solution()
    ss = S.search([4,5,6,7,1,2,3,4],4)
    print(ss)            






"""
 Q： 此题是35 二分查找的变形。找到返id 没有返-1 。不同之处是该 序列被pivot 分割为了左右两块。4 5 6 7 0 1 2 (被3分割，但左右依然升序)

Q2 :  此题目中并不允许 重复元素出现。 ss = S.search([1,3,1,1,1],3)
       此时 mid 为1 left 1 但是左侧就不能保证是升序序列， 主要就是由于重复元素造成。 81题解决。

 A ： 依然使用left 和 right  关键即 调整 位置， 转向左侧还是右侧。
        mid 将 串分割只有两种可能 ：1. 左侧是连续升序 2. 右侧是连续升序 (或者全部升序)
        所以首先判断 左侧 还是右侧升序连续；其次判断 应该选左还是选右边 (必须使用连续升序区间判断， 因为非连续区间判断无意义)
        [ 如6 为mid 找3 456 连续 如果在此区间该往此边  否则右侧]


Error: 

    [3,1] 1 
    该测试失败，主要是L14 中没有添加= ，导致else即右侧 不一定是升序。应该讲= 放到左侧 ，

"""