"""
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words. You may assume the dictionary does not contain duplicate words.

For example, given
s = "leetcode",
dict = ["leet", "code"].

Return true because "leetcode" can be segmented as "leet code".

UPDATE (2017/1/4):
The wordDict parameter had been changed to a list of strings (instead of a set of strings). Please reload the code definition to get the latest changes.

## 140 相关 求解具体path

"""







"""
s1:  DP

   * 此题和回文 132题类似;

   * 问题： 
            f(0,n)表示该串是否能 正确划分;
            可以通过确定一个k位置将此问题划分为 两个子问题, 子问题不相关;
            f(0,n) = f(0,k) && f(k+1,n)  任意的K;
            
            以上公式和132中判断回文一样. = 可以创建二维数组存放f(i,j)状态;
            
            和132中类似，我们可以将f(0,k) 自行判断, 没必要使用缓存, 即判断(0,k)中元素在不在字典中即可;  (类似于132中判断(0,k)回文)

    * 代码：
            一维数组 存放f(k,n) 

            for i in n-1 ...0: #cal f(i,n)
                for j in i... n-1:  # f(i,n) = f(i,j) && f(j+1,n)
                    (i,j) is in dict && f(j+1,n)

            判断(i,j)是否在dict中,可以使用dict o(1)执行; 或者使用 dp 二维数组cache; 同样是o(1)

    * 复杂度：
             时间： o(n^2)  空间： o(n)  (使用dp判断是否在dict则o(n^2))


T: 
    list 转换 dict 
    >>>list1 = ['key1','key2','key3']
    >>>list2 = ['1','2','3']
    >>>dict(zip(list1,list2))



"""
class Solution1(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """


        tmp = [True]*len(wordDict)
        myDict = dict(zip(wordDict,tmp))
        n = len(s)
        stat = [False] * (n+1)   # 锚点
        stat[-1] = True

        for i in range(n-1,-1,-1):  #cal f(i,n)
            for j in range(i,n): # f(i,n) = f(i,j) && f(j+1,n)
                if stat[j+1] and myDict.get(s[i:j+1],False) : 
                    stat[i] = True
                    break

        return stat[0]



"""
S2: 
    递归： dfs
    f(i,j) = f(i,k) && f(k+1,j)  任意k

    不使用cache:  TLE 超时;  

    S1: 55ms
    S2: 516ms

    还可以对S2稍微优化子问题；类似S1划分更好些；

"""

class Solution(object):
    def wordBreak(self, s, wordDict):

        tmp = [True]*len(wordDict)
        myDict = dict(zip(wordDict,tmp))
        n = len(s)
        cache = [ [-1]* n  for i in range(n)]   # -1 notvalid 1 Treu 0 False


        return self.recur(s,myDict,cache,0,len(s)-1)



    def recur(self,s,wordDict,cache,i,j):   #[i,j]

        if j < i :
            return True
        if cache[i][j] != -1:
            return cache[i][j] == 1
        if wordDict.get(s[i:j+1],False) :  # exict
            cache[i][j] = 1
            return True

        for k in range(i,j):
            if self.recur(s,wordDict,cache,i,k) and self.recur(s,wordDict,cache,k+1,j):
                cache[i][j] = 1
                return True
        cache[i][j] = 0
        return False



"""
Task: 
基于BFS 未看： https://discuss.leetcode.com/topic/2545/a-solution-using-bfs
"""




if __name__ == '__main__':
    S = Solution()
    ans = S.wordBreak("leetcode", ["leetcode"])
    print(ans)