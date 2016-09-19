"""
Your task is to calculate ab mod 1337 where a is a positive integer and b is an extremely large positive integer given in the form of an array.

Example1:

a = 2
b = [3]

Result: 8
Example2:

a = 2
b = [1,0]

Result: 1024

"""

"""
S1:  
    ****
    bin(1337) = 0b10100111001  b是一个很大的数字.
    快速幂取余
    公式：  a^b%c=(a%c)^b%c    #二项式拆分即可得出
            (a*b)%c = ( a%c * b%c )%c
    题目中b是一个很大的数,使用list存放.[1,2,3] -> 1*100 +2*10+3
    a^b %c = a^(x0+x1*10+x2*100+...) %c  = (a^x0 %c * (a^10)^(x1+10*x2+100*x3+...) %c ) %c
                                         = (a^x0 %c * ((a^10) %c)^(x1+10*x2+100*x3+...) %c  )%c
        由以上. 对b从低到高依次a^Xi %c 累乘.  a = (a^10)%c 开始下次迭代.

T： ***
    此处b是以10进制list给出. 如果直接给出b int, 我们也可以依次将b->  b/2  迭代计算. O(log b)时间.  #如R中

R：
    http://www.cnblogs.com/PegasusWang/archive/2013/03/13/2958150.html
    https://discuss.leetcode.com/topic/50489/c-clean-and-short-solution   # leetcode  递归实现, 复杂.
"""

class Solution(object):
    def superPow(self, a, b):
        """
        :type a: int
        :type b: List[int]
        :rtype: int
        """
        tmp = 1
        aa = a
        c = 1337
        for i in reversed(b):  #逆向遍历
            tmp *= (aa ** i )%c
            # tmp %= 1337
            aa = (aa**10)%c 
        return tmp%c



"""
S2:
    leetcode 方法：

R：
    https://discuss.leetcode.com/topic/50458/1-liners-other-with-explanations

"""
# 递归  python pow(a,b,c) == (a**b)%c
def superPow(self, a, b):
    return pow(a, b.pop(), 1337) * pow(self.superPow(a, b), 10, 1337) % 1337 if b else 1



"""
S3:
    迭代 正向
    ****
    : For example for a5347, the above computes a5, then a53, then a534, and then finally a5347. 
     And a step from one to the next can be done like a5347 = (a534)10 * a7
R： 
    https://discuss.leetcode.com/topic/50458/1-liners-other-with-explanations
"""
def superPow(self, a, b):
    result = 1
    for digit in b:
        result = pow(result, 10, 1337) * pow(a, digit, 1337) % 1337
    return result


if __name__ == '__main__':
    S =Solution()
    ss = S.superPow(2,[3,2,1])
    print(ss)
