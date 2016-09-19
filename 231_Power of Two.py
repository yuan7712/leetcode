"""
Given an integer, write a function to determine if it is a power of two.

"""


"""
S1:

"""
class Solution1(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        tmp = 1
        while tmp <=n:
            if tmp==n:
                return True
            tmp*=2
        return False

"""
S2:
    2^n  bit中只有一位是1 其余全是0, 只要判断只有一个1即可.  n&n-1
    n：  0000100....
    n-1  000001111..
         n&n-1 == 0
R:
    https://discuss.leetcode.com/topic/17857/using-n-n-1-trick/15
"""

class Solution(object):
    def isPowerOfTwo(self, n):
        #return n > 0 and not (n & n-1)
        if n<=0:
            return False
        return (n&(n-1))==0