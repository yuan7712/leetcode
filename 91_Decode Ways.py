"""
A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given an encoded message containing digits, determine the total number of ways to decode it.

For example,
Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12).

The number of ways decoding "12" is 2.

"""




"""
S1:  递归+cache

    1. 划分子问题 找到最优子结构;  2. 重叠子问题; 

    f(0,n)  : 即求解0-n位置 所有解码可能性;
            f(0,n) = f(0,k) + f(k,n)   # 只是此处k最多会选择两种;  判断条件稍多;


    * case : 
            "10001": 此种属于error case;
            "0" : 单独处理此case;

    * 复杂度：

            f(0,n) = f(1,n) +f(2,n) ... 会形成一个满二叉树：不使用cache复杂度就是  指数级别;  2^n

            使用cache: f(i,n) 只会计算一次. while中也是固定迭代次数, 所以总体o(n^2) ??




"""
class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s or s[0]=='0': 
            return 0
        statCache = [-1] * len(s)
        return self.recur(s,statCache,0)


    def recur(self,s,statCache,start):
        """
        递归求解从start起始位置的 decode 可能次数;

        终止条件:  12 :  "12" 本身 0-27 所以递归dfs(2)此时应该返回1;
        中途包含0处理： 10.. 20..  分割线只能在0后面分割, 不可能有0开头的串.
                        所以while中对于当前数值如果是0 直接break；  这样可以处理'012' 此种case;

        return decode nums s[start:]

        """

#        if s[start] == '0':  # pass '0...'
#            tmp = self.recur(s,statCache,start+1)
#            statCache[start] = tmp
#            return tmp
#        if start == len(s)-1 :
#            return 1
        if start == len(s) :
            return 1
        if statCache[start] != -1:   #cache
            return statCache[start]

        i = start
        tmp = 0
        ans = 0
        while i < min(len(s) ,start+2) :   # del case  "10..."  "20..."
            tmp = tmp*10 + int(s[i])
            if 0 < tmp < 27:
                ans +=self.recur(s,statCache,i+1)
            else:                           #"01" return 0
                break
            i+=1
        statCache[start] = ans
        return ans
        






"""
S2:   非递归  从下到上  DP;  时间o(n)  空间o(1)

            f(0,n) = f(0,k) + f(k,n)   # 只是此处k最多会选择两种;  判断条件稍多;

    * 代码： 
            stat[n] == f(k,n)

            for i in n-1 ... 0:
                (i,i) + f(i+1)
                (i,i+1) +f(i+1)

    * 复杂度： 时间o(n)  空间o(n)   其实stat数组中只是使用到后序两个状态; 
            所以可以只存储stat[i]  stat[i+1]  空间就是o(1)

"""

class Solution(object):
    def numDecodings(self, s):

        if not s :
            return 0
        n = len(s)
        stat  = [0]*(n+1)
        stat[-1] = 1   # match all 
        stat[-2] = 0 if s[-1] == '0' else 1  # 单独处理最后两个，省去for中循环

        for i in range(n-2,-1,-1):
            if s[i] == '0':   #"012...."
                stat[i] = 0
                continue
            stat[i] += stat[i+1]  # [1,9]
            if 0 < int(s[i:i+2]) < 27: # [10,26]
                stat[i] += stat[i+2]

        return stat[0]










if __name__ == '__main__':
    S = Solution()
    ans = S.numDecodings("1")
    print(ans)

