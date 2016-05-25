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

class Solution(object):
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
            elif p_l == 1 or p[1] !='*': # next
                if not s_l or (p[0]!='.' and p[0]!=s[0]) :  #len(s) == 0 or  不匹配
                    return False
                else:
                    return match(s[1:],p[1:])
            else: # len(p) >=2








"""
先来看递归的解法：

如果P[j+1]!='*'，S[i] == P[j]=>匹配下一位(i+1, j+1)，S[i]!=P[j]=>匹配失败；

如果P[j+1]=='*'，S[i]==P[j]=>匹配下一位(i+1, j+2)或者(i, j+2)，S[i]!=P[j]=>匹配下一位(i,j+2)。

匹配成功的条件为S[i]=='\0' && P[j]=='\0'。

"""