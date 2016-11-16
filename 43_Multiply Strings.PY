"""
Given two numbers represented as strings, return multiplication of the numbers as a string.

Note:
The numbers can be arbitrarily large and are non-negative.
Converting the input string to integer is NOT allowed.
You should NOT use internal library such as BigInteger.

"""


"""
S1:
    模拟乘法  Pass
    1. 123 *45   先计算123*5 变为int 然后 123*4  sum
"""
class Solution1(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        def cal(num):  #计算数字list-> 数字 [4,2] ->24
            re = 0
            for i in reversed(num):
                re=re*10 +i
            return re

        ans = 0
        for i ,v in enumerate(reversed(num2)):   #short num2
            count = 0  #进位
            ans_t = []  #逆序
            for j,in reversed(num1):
                v1 = int(v)
                v2 = int(j)
                tmp = v1 * v2 +count
                ans_t.append(tmp%10)
                count = tmp//10
            if count :
                ans_t.append(count)
            ans += cal(ans_t)*(10**i)  # 
        return str(ans)

"""
S2:
    leetcode方法 
    123 * 45 for for  两层遍历,  不再计算 123*4  int值;  123*4-> 3*4  2*4  1*4  sum
T:
    0 * 0  
"""
class Solution(object):
    def multiply(self, num1, num2):
        ans = [0]*(len(num1)+len(num2))
        for i in range(len(num1)-1,-1,-1):
            for j in range(len(num2)-1,-1,-1):   #loc i+j,i+j+1
                ans[i+j+1] += int(num1[i]) * int(num2[j])
        for i in range(len(ans)-1,0,-1):
            ans[i-1] += ans[i]//10
            ans[i]%=10
        #if sum(ans) == 0:   #case 0*0 ->0
            #return '0'
        res = ''.join(str(e) for e in ans)
        res = res.lstrip('0')
        if len(res) == 0: #case 0*0 ->0
            return '0'
        return  res #lstrip 去除左边



if __name__ == '__main__':
    S =Solution()
    ss = S.multiply('12','12')
    print(ss)





        
