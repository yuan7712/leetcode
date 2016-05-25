"""
Given an array of integers, every element appears twice except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

"""


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans  = 0

        for i in nums:
            ans ^=i
        return an





"""
Q : 此题是要找出不是两次出现的数字。唯一。

A ： 使用异或， 当两个数字异或后就会变为0，所以能够将偶数个数字消除，最后返回单数个的数字

T :  
    异或： 1 0 ->1
           1 1 ->0
           0 0 ->0
           0 1 ->1

    a^b  异或运算

O ： 137 题

"""