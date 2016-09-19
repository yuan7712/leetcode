"""
Given an integer (signed 32 bits), write a function to check whether it is a power of 4.

Example:
Given num = 16, return true. Given num = 5, return false.

Follow up: Could you solve it without loops/recursion?

"""

"""
S1:
   4的幂 对应的bit  只含有一个1, 而且只在偶数位置上出现.
   2的幂 对应的bit  只含有一个1, 可以在任意位置.
   1. 首先判断是不是2的幂  n&n-1
   2. 排除那些是2的幂不是4的幂,即1出现在奇数位置
        2： 0000 0010      1： 0000 0001
        8： 0000 1000      4： 0000 0100
        32: 0010 0000      16: 0001 0000
        128 1000 0000      64：0100 0000 
            由以上观察,在每4位bit中,不符合的数字 只在 1或3号位置，而4幂只在0 2 号位.  用0101 &  就能将 2 8 32 128 等筛除.
R： 
    https://discuss.leetcode.com/topic/42860/java-1-line-cheating-for-the-purpose-of-not-using-loops
"""
class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n>0 and (n&(n-1))==0 and n&0x55555555 !=0
        


"""
S2:
    **** leetcode 方法.
    1. 首先还是判断是否2的幂, n&(n-1)
    2. 然后区分2^2k  和2^2k+1 
       结论： 2^2k  满足： (num - 1) % 3 == 0
              4^k = (3+1)^k = 3^0*1^k*C(k,0) + 3^1*1^k-1*C(k,1)+....3^k*1^0*C(k,k) 
              4^k -1 = 3(...) 恰好整除3
              相反可以证明2^2k+1 恰好不是整除

R:
    https://discuss.leetcode.com/topic/42914/1-line-c-solution-without-confusing-bit-manipulations
"""
class Solution(object):
    def isPowerOfFour(self, n):
        return n>0 and (n&(n-1))==0  and (n-1)%3==0