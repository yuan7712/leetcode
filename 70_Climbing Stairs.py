"""
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
"""



class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        i ,a ,b = 0,0 ,1   #a为前一个数  b 为后一个数

        while i < n:
            a ,b = b,a+b
            i +=1
        return b




if __name__ == '__main__':
    S = Solution()
    ss =S.climbStairs(3)
    print(ss)





"""
A : f(n) = f(n − 1) + f(n − 2)    f(1)=1  f(0)=0 ??
   # 1,1,2,3,5,8,
   1,2,3,5,8
    斐波那契数列


Q: f(0) 为1？ 当n=2 时 应该是2种 ,


A2:  
     可以使用公式 直接计算。
"""