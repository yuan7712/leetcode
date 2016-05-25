"""
Given two binary strings, return their sum (also a binary string).

For example,
a = "11"
b = "1"
Return "100".

"""

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        i , j =  len(a)-1 ,len(b)-1
        ans = []
        my_sum = 0   #不使用pre记录进位，每次my_sum//2即可

        while i>=0 or j>=0:
            if i>=0 :
                my_sum += (ord(a[i])-ord('0'))
                i -=1
            if j>=0:
                my_sum += ord(b[j])-ord('0')
                j -=1
            ans.append(str(my_sum%2))
            my_sum //=2
        if my_sum :
            ans.append('1')
        ans.reverse()
        return ''.join(ans)


"""
S2:
    bin() : 将整数值转化为二进制字符串，以0b开头，所以return时[2:]
    int(a,2)  将a按照2进制解析转化为一个整数。
"""
class Solution2(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        return bin(int(a,2)+int(b,2))[2:]


if __name__ == '__main__':
    S =Solution()
    ss =S.addBinary('1010','1011')
    print(ss)