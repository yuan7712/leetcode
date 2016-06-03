"""
Implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:
isMatch("aa","a") → false
isMatch("aa","aa") → true
isMatch("aaa","aa") → false
isMatch("aa", "a*") → true
isMatch("aa", ".*") → true
isMatch("ab", ".*") → true
isMatch("aab", "c*a*b") → true

"""


"""
S1: 
    递归暴力求解. python超时;java 可通过
    case: 
         "aaaaaaaaaaaaab"
         "a*a*a*a*a*a*a*a*a*a*c"

A:  
    正则匹配;  .匹配一个任意字符。* 匹配>=0 个之前的字符; .比较好处理,此处主要是*处理。(即*该匹配几个之前的字符)

    递归 
    p 长度 0 1 >=2  三种
        len(p) ==0 :   return s==p
        len(p) ==1 :   此时只要判断p[0]==s[0]  (注意对p[0]='.' 处理)
        len
        (p) ==2 :   此时判断p[1]是否为* ; 
                p[1]!=* :  同len(p) ==1 时逻辑一致,
                p[1] == *:  *之前字符和s可以匹配; * 可以匹配>=0个。分情况只要一种True即可
                        match(s,p[2:]) 匹配0个
                        match(s[1:],p) 匹配>=1个
    注意:
        1. 递归中s非空的判断，防止越界。

R: 
    http://www.cnblogs.com/zuoyuan/p/3781773.html
    http://blog.csdn.net/linhuanmars/article/details/21145563

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
            if not p_l:   #len(p) == 0
                return s_l == p_l
            if  p_l == 1  or p[1] !='*': #len(p) ==1  or len(p)>=2  and p[1]!=*
                if s_l and (p[0] =='.' or s[0]==p[0]) :
                    return match(s[1:],p[1:])     
                else :
                    return False     
#            elif p[1] !='*':  #len(p) >=2 
#                return p[0] == s[0] and match(s[1:],p[1:])
            else :  #len(p) >= 2  & p[1] ==*  
#                if not s_l:
#                    return match(s,p[2:])
                if not s_l or (p[0] != s[0] and p[0]!='.'): #match 0
                        return match(s,p[2:])
                else : # s or s++
                    return match(s,p[2:]) or match(s[1:],p)  # 匹配0 个或者>=1 个
        return match(s,p)



"""
S1  java 实现 通过
"""

"""
import java.util.regex.Matcher;

public class Solution {

    public boolean isMatch(String s, String p) {
        char[] as = s.toCharArray();
        char[] ap = p.toCharArray();
        return iMatch(as, ap, 0, 0);
    }

    public boolean iMatch(char[] s, char[] p, int s_b, int p_b) {
        
        if (p_b == p.length) {
            return s_b == s.length;
        }
        if (p_b == p.length-1 || p[p_b+1] != '*') {
            if (s_b <s.length  && (p[p_b] == '.' || s[s_b] == p[p_b])) {
                return iMatch(s, p, s_b + 1, p_b + 1);
            } else
                return false;
        } else {
            if(s_b >=s.length || (p[p_b] != '.' && s[s_b] != p[p_b])){
                return iMatch(s, p, s_b , p_b + 2);
            }
            else{
                return iMatch(s, p, s_b , p_b + 2) || iMatch(s, p, s_b+1 , p_b);
            }

        }
    }
    public static void main(String[] args) {
        // TODO Auto-generated method stub
       Solution s = new Solution();
       System.out.println(s.isMatch("aaaaaaaaaaaaab","a*a*a*a*a*a*a*a*a*a*c"));
    }

}
"""



"""
S2、S3:
    动态规划
R:
    http://blog.csdn.net/linhuanmars/article/details/21145563
    http://www.cnblogs.com/zuoyuan/p/3781773.html
"""



"""
动态规划：
    S1递归实现中出现许多的重复计算,动态规划就是讲我们计算过的历史信息保存下来,等到用的时候直接使用,不用重新计算。

步骤：
    1. 确定递推量
    2. 推导递推式
    3. 计算初始条件

A：
    1. 创建二维数组dp , dp[i][j] 表示s[i]之前和p[j]之前是否能匹配.
    2. 递推:   外层s内层p; 对p分情况
                2.1 p！='*' : dp[i][j]  由dp[i-1][j-1]和当前s[i]==p[j] 决定. (p为. 包含此中)
                2.2 p == '*' : 
                            case A: 判 dp[i][j-1]; 如果True, 则True;   即此p[j] * 匹配之前的字符一次。(s[i-1]已经和之前匹配再加*也无妨)
                            case B: 判 dp[i][j-2];   即 * 匹配之前字符0次,
                            case C: 判 dp[i-1][j];   即 * 匹配之前字符多次. (s[i-1]已经能匹配到*,如果s[i]==p[j-1] 即再匹配一个相同字符即可)

                            以上三种case 只要一种符合即返回True;
    3. 初始条件：
                3.1 : 为了计算方便,将dp数组 行列各加一维. 这样dp[i][j] 表示s[i-1]和p[j-1]之前的元素能否匹配。(包括i-1)
                3.2 : 关于越界： 
                        case 2.1 :   dp[i][j]=dp[i-1][j-1]  当i = 1 时候会用到dp[0] 其余时刻不会越界.
                                     所以处理dp[0]即可.(含义：s 空时能匹配到p那个位置 p: a*b*c*d*) 
                                     dp[0][i]=dp[0][i-2]
                        case 2.2 : 
                                    case A:  dp[i][j-1]  不越界. 当j=1即p[0]='*' dp[i][0] = False;  (p[0]为*必然False)
                                    case B:  dp[i][j-2]  j=1时，此处判dp[i][-1] =False (i>=1 默认均为False 此处python 逆序索引，java则自行判断即可)
                                    case C:  dp[i-1][j]  i=1 时 等价于 case2.1 处理dp[0] 即可。

"""
class Solution2:
    def isMatch(self, s, p):
        dp=[[False for i in range(len(p)+1)] for j in range(len(s)+1)]
        dp[0][0]=True
        for i in range(1,len(p)+1):
            if p[i-1]=='*':
                if i>=2: # i = 1 即p[0]=='*' 此时必然False 不能匹配。(此处也可直接判断偶数位置* 即可)
                    dp[0][i]=dp[0][i-2]

        for i in range(1,len(s)+1):
            for j in range(1,len(p)+1):
                if p[j-1]=='.':  #case 2.1
                    dp[i][j]=dp[i-1][j-1]
                elif p[j-1]=='*':  #case 2.2
                    dp[i][j]=dp[i][j-1] or dp[i][j-2] or (dp[i-1][j] and (s[i-1]==p[j-2] or p[j-2]=='.'))
                else: #case 2.1 
                    dp[i][j]=dp[i-1][j-1] and s[i-1]==p[j-1]
        return dp[len(s)][len(p)]



"""
S3:
    类比S2实现,调换遍历顺序，外层p内层S;

A:
    2. 递推： 因为S相对不变,我们主要处理p中的*,所以对p字符分类. dp[i][j]
            case 2.1 p!='*':   判 dp[i-1][j-1]
            case 2.2 p == * :
                            case A : dp [i][j-1] (即* 已经匹配s[j-1] 如果s[j]恰好为 *之前匹配的 则 True) ,即*匹配多次
                            case B : dp[i-1][j] p[i-1]  已能匹配s[j], 即*之前匹配1次  
                            case C ：dp[i-2][j] p[i-2]  能匹配到s[j], 即*之前的匹配0次即可. 
    3. 初值:   行列各加一维
            case 2.1 : dp[i-1][j-1] 处理dp[i][0]  而i=1 时 dp[0][j] 默认都为False
            case 2.2 :   
                         dp[i][j-1] : j=1 dp[i][0] 已处理 
                         dp[i-1][j] ：i=1 dp[0][j]= False  即p[0]=*
                         dp[i-2][j] : i=1 dp[-1][j] False  i=2 False(p空不能匹配到s[1])

"""
class Solution3(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        dp = [[False for i in range(len(s)+1) ] for j in range(len(p)+1)] 
        dp [0][0] = True
        for i in range(1,len(p)+1):
            if p[i-1] == '*' and i>=2:
                dp[i][0] = dp[i-2][0]


        for i in range(1,len(p)+1):
            if p[i-1] == '.':
                for j in range(1,len(s)+1):
                    dp[i][j] = dp[i-1][j-1]
            elif p[i-1] !='*':
                for j in range(1,len(s)+1):
                    dp[i][j] = dp[i-1][j-1] and p[i-1]==s[j-1]
            else: # case *
                for j in range(1,len(s)+1):
                    dp[i][j] = (dp[i][j-1] and (p[i-2] =='.' or p[i-2]==s[j-1])) or dp[i-1][j]or dp[i-2][j]

        return dp[len(p)][len(s)]



if __name__ == '__main__':
    S = Solution3()
    s1 =S.isMatch('aaaaaaaa','a*')
    s2 = S.isMatch("aaaaaaaaaaaaab","a*a*a*a*a*a*a*a*a*a*c")
    print(s2)


         
         