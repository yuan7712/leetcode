"""
Given an array with n objects colored red, white or blue, sort them so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note:
You are not suppose to use the library's sort function for this problem.

click to show follow up.

Follow up:
A rather straight forward solution is a two-pass algorithm using counting sort.
First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then 1's and followed by 2's.

Could you come up with an one-pass algorithm using only constant space?

"""


"""
S1: 
    [0,0,1,2,1,2,0,0,2,1]
    分别使用三个指针分割红白蓝. red 指向红色top; white指向白色top,blue 指向blue top.
    1. 在指针移动中主要移动 白 蓝 两个指针.
            白： 
                case 白 ： white ++ 
                case 蓝 ： swap(white,blue)  #未知 白 or 红 所以不++
                case 红 ： swap(white,red)  white ++  red ++; 
            蓝： 
                case 蓝： bule --
                case 白蓝 swap(blue,white) bule--
"""
class Solution1(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not nums: 
            return 
        nums_len  = len(nums)
        red,white,blue = -1,0,nums_len-1   #  red 表示红色top; white 表示白色top next; blue表示 blue top next;

        while white <= blue: 
            while white <= blue and nums[blue] == 2 : 
                blue -= 1
            while white <=blue and nums[white] == 1:  #white -> case white
                white +=1
            if white <= blue and nums[white] == 0 :  # white -> case red 
                red +=1 
                nums[red],nums[white] = nums[white],nums[red]
                white +=1 
            elif white <= blue  :    # white ->  case  blue
                nums[white],nums[blue] = nums[blue] ,nums[white]
                blue -= 1
        return 


"""
S2： 
    S1简化
    1. 只判断white; 对于blue 由white判断后 swap;
"""
class Solution2(object):
    def sortColors(self, nums):
        nums_len = len(nums)
        red,white,blue = -1,0,nums_len-1

        while white <= blue :
            if nums[white] == 1 :   #case white 
                white +=1
            elif nums[white] == 0 : # case red 
                red +=1 
                nums[red],nums[white] = nums[white],nums[red]
                white +=1 
            else :  # case blue
                nums[white],nums[blue] = nums[blue] ,nums[white]
                blue -=1
        return



"""
S3: 
    提示： 使用计数排序, 另分配数组长度为3,第一次遍历 记录 0  1 2 的个数。
    然后第二次填充对应个数即可.
"""


"""
S4: 
    此方法使用三个指针分别记录 r w b top;  即表示 <= 0、1、2的个数

   1.  [1,2,2,2,1... ]
       如上当前判断最后一个1; b指向最后一个2,w指向左侧1;
       将1移向左侧, 分别将2 向右移动一个即可. -> [1,2,2,2,2...] -> [1,1,2,2,2...]
       0,1,2 移动同理
R: https://discuss.leetcode.com/topic/675/anyone-with-one-pass-and-constant-space-solution/3
"""
class Solution(object):
    def sortColors(self, nums):
        r ,w, b = -1,-1,-1

        for i in nums:
            if i == 0:  # 将红 白 蓝 栈顶分别向右移动一个即可
                r += 1
                w += 1
                b += 1
                nums[b],nums[w],nums[r] = 2,1,0
            elif i ==1:
                b += 1
                w += 1
                nums[b],nums[w] = 2,1
            else:
                b += 1
                nums[b] = 2
        return 






if __name__ == '__main__':
    S =Solution()
    ss = S.sortColors()
    print(ss)

