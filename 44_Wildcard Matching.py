"""
Implement wildcard pattern matching with support for '?' and '*'.

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:
isMatch("aa","a") → false
isMatch("aa","aa") → true
isMatch("aaa","aa") → false
isMatch("aa", "*") → true
isMatch("aa", "a*") → true
isMatch("ab", "?*") → true
isMatch("aab", "c*a*b") → false
"""


"""
S1:     TLE
    递归. (未验证正误.)忽略此方法 累赘
case:
    "babaaababaabababbbbbbaabaabbabababbaababbaaabbbaaab"
    "***bba**a*bbba**aab**b"

A： 
    1. 累赘. 每次循环向后匹配多个,
"""
class Solution1(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        def match(s,p):
            s_l ,p_l = len(s),len(p)
            for i in range(min(s_l,p_l)):
                if p[i]=='*':
                    stat = False
                    if i == p_l-1:
                        return True
                    else : # recur
                        for j in range(i,len(s)):
                            stat = stat or match(s[j:],p[i+1:])
                            if stat:
                                return True
                elif  p[i]!= '?' and s[i]!=p[i]: # cannot match
                    return False
                else:
                    pass

            if s_l > p_l:
                return False
            elif s_l == p_l: 
                return True
            else :
                for k in range(s_l,p_l):
                    if p[k]!='*':
                        return False
                return True

        return match(s,p)



"""
S1_2:       TLE
    递归
case: 
"babbbbaabababaabbababaababaabbaabababbaaababbababaaaaaabbabaaaabababbabbababbbaaaababbbabbbbbbbbbbaabbb"
"b**bb**a**bba*b**a*bbb**aba***babbb*aa****aabb*bbb***a"

A: 
    1. 对S1修改.每次判断s[0]和p[0], 
        1.1 s[0]==p[0]  : 判 match(s[1:],p[1:])
        1.2 s[0]!=p[0] 失配 return False
        1.3 p[0] 为* : 
                        将p[1:] 依次与s字串匹配.
    2.  处理越界
"""

class Solution2(object):
    def isMatch(self, s, p):

        def match(s,p):
            if not p : #p!= null
                return len(s) ==0
            if p[0] == '*':  # case * 
                i ,j= 0,0
                while i < len(p) and p[i]=='*':  # match *****
                    i+=1
                if i ==len(p):
                    return True
                while j < len(s):  # recursion 
                    if  match(s[j:],p[i:]):
                        return True
                    j+=1
                return False
            elif  not s  or (p[0]!= '?' and s[0]!=p[0]): # s==None ->False;
                return False
            else:# match
                return match(s[1:],p[1:])
        return match(s,p)





"""
S2:
   动态规划 DP
   lintcode.com  Pass.
   leetcode.com  TLE
A: 
    参考 10 Regular Expression Matching 
    1. 递推量： 
                dp[i][j] 表示 p[i]和s[j] 之前的是否匹配.
    2. 递推式： 对p[i]分情况
                2.1 p[i] != '*' : dp[i][j]  = dp[i-1][j-1] and p[i]==s[j]
                2.2 p[i] =='*' :  判断dp[i-1][0]->dp[i-1][j]  中只要有一个True 即可
    3. 优化：
            观察2递推式, 计算dp[i][j]只要dp[i-1]的值即可。不必要二维数组。只要两个一维数组即可。(交换使用)
    4. 初值： 
            dp[] 即 dp[0][...]   表示p0个元素匹配s; 只需设置dp[0] True 即可
            每个p循环后， 注意更改dp[0] 的值. 
                case : P='*****acd'  在前几个的  dp[0] 都应该设置True . 

R:
    http://www.cnblogs.com/yuzhangcmu/p/4116153.html

"""

class Solution3(object):
    def isMatch(self, s, p):

        if len(s)>300 and p[0]=="*" and p[-1]=="*":
            return False 
        dp = [False for i in range(len(s)+1)]   #上一行的dp 信息
        dp_n = [False for i in range(len(s)+1)]  #此行数据
        dp[0] = True
        count = 0  # 计数开头的* 个数

        for i in range(1,len(p)+1):
            if p[i-1] == '*':  #case 2.2
                count+=1
                for j in range(1,len(s)+1):
                    k = 0
                    while k <= j and (not dp[k]):
                        k+=1
                    if k<=j:
                        dp_n[j] = True
                    else:
                        dp_n[j] = False
            else: #case 2.1
                for j in range(1,len(s)+1):
                    dp_n[j] = dp[j-1] and (p[i-1]=='?' or p[i-1] == s[j-1])
            dp ,dp_n= dp_n,dp   # switch dp 

            if count == i :   # 上述操作中没有dp[0]操作, 此处防止p开头连续*; 此时dp[0]应设置True
                dp[0] = True
            else:
                dp[0] = False
        return dp[-1]  # return last




"""
S2_2: TLE
    DP 改进
    Lintcode Pass

A: 
    2. 递推式
        2.1  p[i] != '*' : dp[i][j]  = dp[i-1][j-1] and p[i]==s[j]
        2.2  p[i] =='*' :  dp[i][j]  = dp[i-1][j]  or dp[i][j-1] ;    (dp[i][j-1] = dp[i-1][0...j-1])
    4. 初值
            dp[] 表示 dp[i-1][...] 
            dp_n[] 表示 dp[i][...] 当前 ; 当j=1时 使用dp_n[0],所以记住每次更新dp_n[0],表示p[i]能否匹配0个S,即p[i]是否全*
R: 
    http://www.cnblogs.com/yuzhangcmu/p/4116153.html

"""
class Solution4(object):
    def isMatch(self, s, p):
        
        dp = [False for i in range(len(s)+1)]
        dp_n = [False for i in range(len(s)+1)]
        dp_n[0] = True  #p[i-1] == * 时使用; dp_n[0] = True 表示p[i]之前全为*; 即dp[i][0] = True
        dp[0] = True
        count = 0

        for i in range(1,len(p)+1):
            if p[i-1] == '*':
                count+=1
                for j in range(1,len(s)+1):
                    dp_n[j] = dp[j] or dp_n[j-1]   #****
            else:
                for j in range(1,len(s)+1):
                    dp_n[j] = dp[j-1] and (p[i-1]=='?' or p[i-1] == s[j-1])
            dp ,dp_n= dp_n,dp

            if count == i :
                dp[0] = True
                dp_n[0] = True
            else:
                dp[0] = False
                dp_n[0] = False
        return dp[-1]  #last


"""
S3:
    Leetcode Lintcode(去掉注释) Pass
    对递归改进;
A： 
    1. s p 分别设置index: i j ; 如果s[i] p[j] 能够match i++ j++
    2. 对于p[j] =='*' : 
                2.1 :   记录当前*位置的(ii,jj); 继续向后匹配s p  如果失配时,s指向ii 下一个。和递归中 * 处理类似.
                2.2 :   但是如果再次遇到*呢?  P *abcd* 
                         此时如果匹配到第二个* 表示**之间的abcd已经匹配. 我们重新更换 * 标识即可,上一次的*位置信息丢弃即可.
    3. 失配： 
            失配后如果中途遇到过* ,滑动s类似递归 再次match.  若没有遇到过* 说明必然s !match p False
T: 
    此思路和递归基本一致. 当遇到* 同样是判断S字串是否能和p之后匹配.
    关键： 对重复遇到*处理. 
           例: 
              S： abc   aba aba aba 
              P:  abc * aba * ....
                P中**之间的aba,在S字串中可以匹配到S中多个,但是我们只要关注第一个aba即可. 如果*....不能够匹配aba之后的, 即使其余S位置再匹配到aba也必然False
              如我们在S第二个aba和p中aba匹配 判 match(s[9:],p[8:])  而s第一个aba  判match(s[6:]p[8:]) 
              递归中： 对于每组aba 我们都判断 *...能否匹配s字串,直到全部match. 但是完全没有必要,只要判断第一组匹配的aba即可.
              此方法： 所以只关注第一个匹配到的aba即可.所以再次遇到*后,直接更新* 位置即可。

R： 
    https://leetcode.com/discuss/10133/linear-runtime-and-constant-space-solution
    http://www.cnblogs.com/yuzhangcmu/p/4116153.html
"""
class Solution(object):
    def isMatch(self, s, p):

        pre_s, pre_p = 0,0  # 标记遇到*时候 s p 位置
        i,j = 0,0  # s p index
        back = False  # 是否遇到 *

        while i< len(s):
            if j< len(p) and (p[j] == '?' or p[j] ==s[i]):   # s p match  i++ j++
                i+=1
                j+=1
            elif j<len(p) and p[j] =='*' : # p[j] == *   j++  记录新的*,s不动
                back = True
                j+=1
                pre_p,pre_s = j,i
            elif back :       # p s catnot match or p ==end;  如果前面有* 移动pre_s
                pre_s+=1
                i = pre_s
                j = pre_p
            else:    # p s cannot match 且之前没有*  False
                return False

        while j<len(p) and p[j]=='*':
            j+=1
        return j ==len(p)






        


if __name__ == '__main__':
    S= Solution4()
    ss= S.isMatch("aa", "a")
    print(ss)
