"""
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place, do not allocate extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1

"""

class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        
        nums_len  = len(nums)
        i  = nums_len-1
        while i-1>=0 and nums[i]<=nums[i-1]:  #找到第一个 反串
            i -=1
        if i ==0 :  #321
            nums.reverse()
            return nums
        #687432  i->8. 从此之后找到比6大的min 即7
        my_next= i #记录下次选取的值 7
        now = i-1
        i +=1
        while i <nums_len:
            if nums[i]-nums[now]>0 and nums[i]-nums[now] < nums[my_next]-nums[now]:
                my_next = i
            else :
                i+=1
        #将 now my_next  互换
        nums[now] , nums[my_next] = nums[my_next],nums[now]
        #print(nums[now] ,"", nums[my_next], '', now , '', my_next)
        # 由于不能再分配内存，所以只能自己实现局部排序
        #part = sorted(nums[now+1:nums_len])
        #print(part)
        #nums[now+1:nums_len] = part

        for j in range(nums_len-1,now,-1):
            for i in range(now+1,j):
                if nums[i]>nums[i+1]:
                    nums[i],nums[i+1] = nums[i+1],nums[i]

        return nums








if __name__ == '__main__':
    S = Solution()
    ss = S.nextPermutation([1,5,1])
    print(ss)





"""
T:   1. 提交时将return nums-> return

A :  [6,8,7,4,3,2] ->[7,2,3,4,6,8]
     找到该序列的下一个后继。
     1. 从后向前找到到第一个降序的对， 如 6,8 
     2. 修改6 处的值，使用之后的比6大的最小值 即7，替换。
     3. 将7 之后的数字排序。升序


Q： 1. 对7之后的排序，题目不允许再次分配空间，所以不能题目中sorted分片;自己简单实现冒泡 .(C++ 中有局部排序)  
    2. 题目中不允许返回值， 只要修改序列即可 return 即可。
    3. L34 找比6 大的最小值 不能为6 `if nums[i]-nums[now]>0 and` 即此处不能`=`  [1,5,1] Error

"""