"""
Given an integer, write a function to determine if it is a power of three.

Follow up:
Could you do it without using any loop / recursion?

不允许使用循环
"""

"""
S1:
    leetcode 使用%
    32位数 最大的3幂数是 3**19
R:
    https://discuss.leetcode.com/topic/36150/1-line-java-solution-without-loop-recursion
"""
class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # 3**19 =1162261467 
        return n>0 and 1162261467%n == 0
        

"""
S2:
    from leetcode
T:
    If N is a power of 3:

            It follows that 3^X == N
            It follows that log (3^X) == log N
            It follows that X log 3 == log N
            It follows that X == (log N) / (log 3)
            For the basis to hold, X must be an integer.
    但是由于log 3 浮点数精度问题,(log N) / (log 3) 可能不是一个整数, 但是如果与这附近整数相距很小则认为正确.


R:
    https://discuss.leetcode.com/topic/33949/simple-java-solution-without-recursion-iteration
"""
public boolean isPowerOfThree(int n) {
  double a = Math.log(n) / Math.log(3);
  return Math.abs(a - Math.rint(a)) <= 0.00000000000001;
}