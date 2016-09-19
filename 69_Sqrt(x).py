"""
Implement int sqrt(int x).

Compute and return the square root of x.
 开平方
"""

"""
S1:
    二分, 对于n>=0 sqrt(n) <= n/2+1   #n^2 < (n/2+1)^2

R： 
    http://www.cnblogs.com/AnnieKim/archive/2013/04/18/3028607.html 
"""
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        未判断 负数 0 error ==
        """
        left,right = 1,x//2+1
        while left <= right:
            mid = (left+right)//2
            if x/mid == mid:
                return mid
            elif x/mid > mid:
                left = mid+1
            else:
                right = mid-1
        return right    #返回较小一侧数



"""
S2:
    leetcode  牛顿迭代  --？？  未看
R：
    https://discuss.leetcode.com/topic/24532/3-4-short-lines-integer-newton-every-language
    http://www.cnblogs.com/AnnieKim/archive/2013/04/18/3028607.html 

"""
class Solution(object):
    def mySqrt(self, x):
        r = x
        while r*r > x:
            r = (r + x/r) / 2
        return r

if __name__ == '__main__':
    S =Solution()
    ss = S.mySqrt(1)
    print(ss)

