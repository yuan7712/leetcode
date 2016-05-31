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
        len(p) ==2 :   此时判断p[1]是否为* ; 
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
S2:
    动态规划

"""

class Solution2(object):
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
                    dp[i][j] = (dp [i][j-1] and (p[i-2] =='.' or p[i-2]==s[j-1])) or dp[i-1][j]or dp[i-2][j]

        return dp[len(p)][len(s)]


class Solution3:
    def isMatch(self, s, p):
        dp=[[False for i in range(len(p)+1)] for j in range(len(s)+1)]
        dp[0][0]=True
        for i in range(1,len(p)+1):
            if p[i-1]=='*':
                if i>=2:
                    dp[0][i]=dp[0][i-2]
        for i in range(1,len(s)+1):
            for j in range(1,len(p)+1):
                if p[j-1]=='.':
                    dp[i][j]=dp[i-1][j-1]
                elif p[j-1]=='*':
                    dp[i][j]=dp[i][j-1] or dp[i][j-2] or (dp[i-1][j] and (s[i-1]==p[j-2] or p[j-2]=='.'))
                else:
                    dp[i][j]=dp[i-1][j-1] and s[i-1]==p[j-1]
        return dp[len(s)][len(p)]





if __name__ == '__main__':
    S = Solution()
    ss =S.isMatch('aaaaaaaa','a*')
    print(ss)


