"""
Given a non-negative number represented as an array of digits, plus one to the number.

The digits are stored such that the most significant digit is at the head of the list.
"""



class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        pre = 1 # 表示进位 初值为1

        for i in range(len(digits)-1,-1,-1):
            now_sum = digits[i]+pre
            if now_sum >= 10:
                digits[i] = now_sum -10
                pre = 1
            else : 
                digits[i] = now_sum
                pre = 0
        if pre == 1:
            digits.insert(0,1)
        return digits




"""
S2 :  因为只是+1， 只有当999 时候才会产生进位， 而当末尾！=9 时候 +1 直接返回即可

"""


class Solution2(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        for i in range(len(digits)-1,-1,-1):
            if digits[i] ==9:
                digits[i]=0
            else :
                digits[i]+=1
                return digits

        digits.insert(0,1)
        return digits

        




if __name__ == '__main__':
    S = Solution2()
    ss = S.plusOne([9,9,6])
    print(ss)            





"""
给一个数字存放在list中，+1 返回。 此题是2_Add Two Numbers 的简化。

"""        