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
    AAABBB 全排列共： A66 /(3! * 3！) = 20种
    dfs, 在dfs过程中加以判断,如果此时栈中 非法,则不继续dfs.
    由于只有一种符号`()`所以无须保留栈, 只需记录栈中(个数即可.
"""
class Solution(object):
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
http://blog.csdn.net/linhuanmars/article/details/19873463
"""

if __name__ == '__main__':
    S =Solution()
    ss = S.generateParenthesis(3)
    print(ss)























"""
AAABBB 全排列共： A66 /(3! * 3！) = 20种
20 -Valid Parentheses  
32 -Longest Valid Parentheses  
"""