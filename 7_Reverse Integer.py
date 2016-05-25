class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        flag = 0
        MAX = (2 ** 31 - 1)/10  #题目中越界限制。python可以处理大数
        if x <0 :
            flag = 1
            x = abs(x)
        sum = 0
        while x :
            if sum>MAX:
                return 0
            sum = sum *10 + x%10
            x = x //10
        if flag :
            return -sum 
        return sum


if __name__ == "__main__":
    s = Solution()
    ss = s.reverse(123456789123456789)
    print(ss)



"""
Q : python 中支持大数操作当超过Max时会自动转换为大数运算。
    此处限制溢出，所以判 sum/10 和Max/10，>214748364.7  必error
T:  正负数，处理还可以
		if x < 0:
           return -1 * self.reverse(-x)
"""    