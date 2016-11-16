"""
S1: 
    1. 使用数组记录
    2. 或者不记录 将123 -> 321 
"""
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        L = [] #存放int
        if x < 0:
           return False
        while x:
            L.append(x%10)
            x = x//10
        left ,right = 0,len(L)-1
        while left <=right and L[left]==L[right]:
        	left  += 1
        	right -= 1
        if left <=right :
        	return False
        else:
        	return True


class Solution2:
    # @param {integer} x
    # @return {boolean}
    def isPalindrome(self, x):
        if x < 0:
            return False
        div = 1
        while x / div >= 10:  
            div *= 10
        while x != 0:
            q = x // div
            r = x % 10
            if q != r:
                return False
            x = (x % div) // 10  #舍高低位
            div /= 100
        return True


        
if __name__ == "__main__":
    s = Solution()
    ss = s.isPalindrome(-12321)
    print(ss)                   





"""
T: 负数为非回文
S2: 
   S2中12321 一次while中取出最高位和最低位比较。高位取值需要知道总的位数。即div;比较1，1后div 降2位，舍去高低位。

"""    