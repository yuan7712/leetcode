"""
Implement pow(x, n).
x**n
"""


"""
S1:
    x^n = (x^2)^n/2    n%2==0
        = (x^2)^n//2*x  n%2==1
T:
    error case:   
    1. 34.00515,-3 
       负数处理：
          -3//2 = -2  3//2 = 1
          为统一将-3 ->3    设置flag 或者return myPow(x,-n)
    3. 2.00000 ,-2147483648    # x = x**2 Line 16: OverflowError: (34, 'Numerical result out of range')
       32bit最小负数 -2147483648 
           将x = x**2  -> x*=x AC  INF    (但是本地依然不能计算大数)
    4. 关于-2147483648取反. python 本身有大数处理 所以不会error. 
           java.  java 使用如下逻辑 -2147483648  *-1 = -2147483648 [补码取反+1]  可能造成死循环, 应该加以判断
                if (n < 0) 
                        return 1 / (x * myPow(x, -(n + 1)));    #统一+1 排除min 也可.

"""
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n ==0 :
            return 1
        if n<0: #负数
            #if n == -2147483648:
                #return 1/x *1/self.myPow(x,2147483647)
            return 1/self.myPow(x,-1*n)
        ans = 1
        while n>0:
            if n%2 == 1:
                ans *= x
            x = x*x
            n = n//2
        return ans


"""
S2:
    递归 
https://discuss.leetcode.com/topic/21837/5-different-choices-when-talk-with-interviewers
    double myPow(double x, int n) { 
        if(n==0) return 1;
        if(n<0){
            n = -n;
            x = 1/x;
        }
        return n%2==0 ? myPow(x*x, n/2) : x*myPow(x*x, n/2);
    }

"""



if __name__ == '__main__':
    S =Solution()
    ss = S.myPow(2,10)
    print(ss)
