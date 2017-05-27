"""
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, add spaces in s to construct a sentence where each word is a valid dictionary word. You may assume the dictionary does not contain duplicate words.

Return all such possible sentences.

For example, given
s = "catsanddog",
dict = ["cat", "cats", "and", "sand", "dog"].

A solution is ["cats and dog", "cat sand dog"].


139 相关题目;

"""



"""

S1:  dfs   error 超时
    
    * 代码：
     
             dfs(start,stack, ans )  # stack即path
                start == end : 
                    ans.append()   # 全局ans
        
                for i in start...n:
                    stack push [start:i]
                    dfs(i)
                    stack.pop  #  [start:i]

    * 超时TLE 
            CASE ; "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                    ,["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]



"""

class Solution1(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """

        # list -> dict 
        tmp = [True]*len(wordDict)
        myDict = dict(zip(wordDict,tmp))

        ans = []
        path = []

        self.dfs(s,myDict,path,ans,0)
        return ans




    def dfs(self,s,wordDict,path,ans,start):
        """
        """
        if start == len(s): # add
            ans.append(" ".join(path))
            return 

        for i in range(start,len(s)):  # [start,i] && dfs(i+1)
            if wordDict.get(s[start:i+1],False) :
                path.append(s[start:i+1])
                self.dfs(s,wordDict,path,ans,i+1)
                path.pop()

        return 



"""
S2: 
    dfs + cache 92 ms  【使用此种dfs比S1优】

   *  S1中超时是因为有许多重复计算,S2中计划使用cache 解决;

        "leetcode"
        dfs(0) -> dfs(1) dfs(2) ... dfs(n)
        dfs(2) -> dfs(3) ...

        所以使用dict  直接存储dfs(i)的结果
    

    * 关于两种dfs: 
        递推公式都一样dfs(i) = (i,k)  && dfs(k+1)
            S1: 计算dfs(i) 不返回结果, 使用栈记录其path;
                 dfs(i)有多个k的分割位置, 只要将(i,k)入栈然后 dfs(k+1)即可;
                 当i==len(s) 末尾时, path中已经记录了一个case; 将此path添加到全局 ans即可

                 需传递： 全局ans,path栈

            S2： 计算dfs(i) 返回结果, 不使用栈记录path,不必全局结果集;
                 dfs(i)有多个k的分割位置, 只要调用ans = dfs(k+1) 将dfs(k+1)结果和(i,k) 组合即可获得dfs(i)的一种结果;

                 此方法使用较方便, 方便我们使用cache; 

    * S2 代码：
            dfs(start,cache):
                if start in cache:
                    return 
                if start == end :
                    return []   # empty ans
                ans = []
                for k in start...end:
                    tmp = dfs(k+1)
                    (start,k) 和 tmp 合并;  添加到ans

                cache[start] = ans 
                return ans

"""
from collections import defaultdict

class Solution(object):
    def wordBreak(self, s, wordDict):

        # list -> dict   
        tmp = [True]*len(wordDict)
        myDict = dict(zip(wordDict,tmp))

        #ans = []
        #path = []
        cacheDict = defaultdict(list)   #cacheDict[i] -> wordBreak(s[i:], wordDict)
        ans = self.dfs(s,myDict,cacheDict,0)
        return ans




    def dfs(self,s,wordDict,cacheDict,start):
        """
        dfs(i)   return 从i开始能构成的ans ["abc cde ", "aaa ddd"]
        dfs(i)  = (i,k) + dfs(k)
        """

        if cacheDict.get(start,False)!=False:  #exist
            return cacheDict.get(start)   #["case 1"]

        if start == len(s): # add
            return [""]   # empty ans

        ans  = []
        if wordDict.get(s[start:len(s)],False):     # 对于此种单独处理  "abc" ["abc"]  防止出现 "abc "
            ans.append(s[start:len(s)])

        for i in range(start,len(s)-1):  #  [start,i] + dfs(i+1)
            if wordDict.get(s[start:i+1],False) :  # exist
                tmp = self.dfs(s,wordDict,cacheDict,i+1)   #["case 1", " case 2"]
                for item in tmp :
                    ans.append(s[start:i+1]+" "+item)
        cacheDict[start] = ans
        return ans 






"""
S： 

     之前从下到上的DP,对于求解最优解法可行, 也能中途记录不同位置如何划分子问题, 最后进而还原该最优解;

    但是此题目 求解所有解,  从下到上  不可行;  所以使用dfs记录全部结果

"""


        




if __name__ == '__main__':
    s =Solution()
    #ans =  s.wordBreak("abc",["abc"])
    ans =  s.wordBreak("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                    ,["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"])  #"catsanddog",["cat", "cats", "and", "sand", "dog"]
    #ans =  s.wordBreak("catsanddog",["cat", "cats", "and", "sand", "dog"])
    print(ans)
