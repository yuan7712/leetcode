"""
The gray code is a binary numeral system where two successive values differ in only one bit.

Given a non-negative integer n representing the total number of bits in the code, print the sequence of gray code. A gray code sequence must begin with 0.

For example, given n = 2, return [0,1,3,2]. Its gray code sequence is:

Note:
For a given n, a gray code sequence is not uniquely defined.

For example, [0,2,3,1] is also a valid gray code sequence according to the above definition.
格雷码转换
"""



"""
S1 . 利用公式G(N) = (B(n)/2) XOR B(n)
"""
class Solution1(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        ans = [0]*(2**n)

        for i in range(2**n):
            ans[i] = i//2 ^ i

        return ans


"""
S2
利用对称， 初始是 [0,1] 
n = 2 : 先生成 00 01  同时对称11 10  (因为返回十进制值 所以顺便计算累加)
"""
class Solution(object):
    def grayCode(self, n):

        """
        :type n: int
        :rtype: List[int]
        """
        if n == 0 :
            return [0]
        ans = [0,1]
        i =1
        while i < n: 
            tmp_len = 2**(i+1)   # 计算此次list 的长度
            tmp = [0]*tmp_len
            for j in range(len(ans)):      # 对称的使用原list 生成下一个 ，前面加0 或者1
                tmp[j] = ans[j]
                tmp[tmp_len-j-1] = ans[j]+ 2**i
            ans = tmp  #改变ans
            i +=1

        return ans














if __name__ == '__main__':
    S =Solution1()
    ss =S.grayCode(0)
    print(ss)

 

"""
 A :  题目生成格雷码 

 1. 利用维基百科 的公式
        （假设以二进制为0的值做为格雷码的0）
        G：格雷码 B：二进制码
        G(N) = (B(n)/2) XOR B(n)
        二进制码->格雷码（编码）：从最右边一位起，依次将每一位与左边一位异或(XOR)，作为对应格雷码该位的值，最左边一位不变(相当于左边是0)；
        格雷码-〉二进制码（解码）：从左边第二位起，将每位与左边一位解码后的值异或，作为该位解码后的值（最左边一位依然不变）
 2.  利用格雷码 生成时  上下对称 
        n = 1     0  1
        n = 2     00 01  | 11 10 
        n = 3     000 001 011 010 |110 111 101 100  
        能够发现左右对称， 所以我们可以依次递归操作， 每次叠加
 """       


















"""
Q: 
     格雷码： 在一组数的编码中，若任意两个相邻的代码只有一位二进制数不同，则称这种编码为格雷码（Gray Code）
"""