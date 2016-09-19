"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]

"""


"""
S1:
    dfs ****
    AAABBB 全排列共： A66 /(3! * 3！) = 20种
    dfs, 在dfs过程中加以判断,如果此时栈中 非法,则不继续dfs.
    由于只有一种符号`()`所以无须保留栈, 只需记录栈中(个数即可.
"""
class Solution1(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str] 
        """
        ans = []
        self.dfs(ans,"",0,2*n)
        return ans

    def dfs(self,ans,path,l_num,n):
        """
        path： 记录轨迹
        l_num: 栈中 (个数, add(时l_num++; add) 时l_nm--
        n： 还需要括号个数, 初始2*n
        """
        if n == 0 and l_num == 0:
            ans.append(path[:])
        if n < 0:
            return
        # ( and )
        self.dfs(ans,path+"(",l_num+1,n-1)
        if l_num >0 :  #非空栈 add ）
            self.dfs(ans,path+")",l_num-1,n-1)
        return 


"""
S2:
    递归 
    对S1中dfs改变为递归. 使用栈保存中间状态.
    AAABBB
    栈：  A
          AA  AB
          AAA AAB ABA (ABB  error不进栈)
    以上基本就是dfs中栈状态改变. 我们需要记录栈中每个记录失配A(左括号)的个数,当ABB此种时,则error不进栈
    case:  长度满足时 ans.add()
    case:  栈空  return

R: 
    https://discuss.leetcode.com/topic/1921/does-anyone-come-up-with-a-non-recursion-solution/4
"""

class Solution2(object):
    def generateParenthesis(self, n):
        ans = []
        my_stack = [('(',1)]   #STACK 1表示该记录失配(个数. [或者记录 每项(个数...]

        while len(my_stack):
            tmp = my_stack.pop()
            if len(tmp[0]) > 2*n:
                continue
            if len(tmp[0]) == 2*n and tmp[1]==0 :    #len(s)==2*n  and tmp[1]==0  
                ans.append(tmp[0])
            if tmp[1]<n : # add (
                my_stack.append((tmp[0]+'(',tmp[1]+1))
            if tmp[1]>0:  # add )
                my_stack.append((tmp[0]+')',tmp[1]-1))

        return  ans




"""
S3:
    递归. 
T:
    卡塔兰数:
        卡塔兰数，是组合数学中一个常出现在各种计数问题中出现的数列。
        输入一个整数n，计算h(n)。其递归式如下：h(n)= h(0)*h(n-1)+h(1)*h(n-2) + ... + h(n-1)h(0) (其中n>=2，h(0) = h(1) = 1)    
        该递推关系的解为：h(n)=C(2n,n)/(n+1) (n=1,2,3,...)
        常用场景: n个括号对合法序列个数、n个节点构成多少二叉树、123...n出栈种类....  [详见笔记]
        此题如果仅仅求总个数,直接使用公式即可.
A:  f(n) : n个括号对, 能构成的合法序列.  第一个字符必然是`(`, 它必然会与之后的某个`)`匹配, 二者之间必然是成对的括号对.
           使用第一个() 将2n个字符分为两部分.  
                    (i个括号对) n-i-1个括号对.
                    我们对i从0一直遍历到n-1. 即可.  分别使用f(i)和f(n-i-1)组合 ->f(n)
    f(n) = f(0)*f(n-1) + f(1)*f(n-2)+.....f(n-1)*f(0)    #这即卡塔兰数.
    会不会存在重复? 
        2n个字符,对于每一种合法序列,第一个`(`只能与2n中某一个位置匹配.

T： 
    此方法递归,会重复计算f(i),可以添加cache加速,或者直接修改为S4 dp.
R:
    1. https://discuss.leetcode.com/topic/5866/my-accepted-java-solution    
    2. http://www.cnblogs.com/grandyang/p/4444160.html 
    3. http://blog.csdn.net/wuzhekai1985/article/details/6764858     #卡塔兰数
"""
class Solution3(object):
    def generateParenthesis(self, n):
        return self.f(n)
    def f(self,n):
        """
        f(n) :表示还有n个括号对的 所有组合. f(0)  ['']  f(1)=['()']
        return ： 所有组合 ['()']
        """
        if n == 0 : 
            return ['']
        ans = []
        for i in range(n):  #0...n-1
            tmp1 = self.f(i)
            tmp2 = self.f(n-i-1)
            for p in tmp1:
                for q in tmp2:
                    ans.append('('+p+')'+q)
        return  ans


"""
S4:
    dp ****
    还是基于S3的卡塔兰,此处改为dp
    f(n) = f(0)*f(n-1) + f(1)*f(n-2)+.....f(n-1)*f(0)  #f(n)记录n个括号对产生的所有合法序列.
R:
    https://discuss.leetcode.com/topic/3474/an-iterative-method
"""
class Solution(object):
    def generateParenthesis(self, n):
        dp = [['']]+[ [] for i in range(n)]   #n+1 dp[i]==f(i)  return dp[-1]
        for i in range(1,n+1):  #cal f(i)
            for j in range(i):
                tmp1 = dp[j]
                tmp2 = dp[i-j-1]
                for p in tmp1:
                    for q in tmp2:
                        dp[i].append('('+p+')'+q)
        return dp[-1]



"""
A: 
    此题S1 S2 基于dfs求解. S3 S4 使用卡塔兰数.
    求n个括号对的合法个数,这背后即 卡塔兰数.  还有许多类似问题如S3中所述.

R:
    http://blog.csdn.net/linhuanmars/article/details/19873463     卡塔兰
关于卡塔兰： 
    http://blog.csdn.net/wuzhekai1985/article/details/6764858
    http://www.cnblogs.com/wuyuegb2312/p/3016878.html#bop
    http://blog.csdn.net/hackbuteer1/article/details/7450250
    见笔记.
"""

if __name__ == '__main__':
    S =Solution()
    ss = S.generateParenthesis(4)
    print(ss)
    print(len(ss))























"""
AAABBB 全排列共：C63种  A66 /(3! * 3！) = 20种
20 -Valid Parentheses  
32 -Longest Valid Parentheses  
"""