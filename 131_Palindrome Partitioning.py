 #coding=utf-8
"""
Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

For example, given s = "aab",
Return

[
  ["aa","b"],
  ["a","a","b"]
]
回文
"""



"""
S1:
    
    [aabba]
    dfs递归.  
            [a] + dfs[abba]
            [aa] + dfs[bba]
            [aab] + dfs[ba]   Pass
            [aabb] + dfs[a]
            ...
    dfs + 在进入递归之前判断 是否回文

T: 
    回文 125 valid-palindrome
    最长回文 5 Longest Palindromic Substring     # dp 求出每个字串是否回文

R:
    关于回文判断,此处是最朴素方法 left right 靠拢, 此外还可以像 5 最长回文串中类似
    创建dp[][] 数组, 先把dp 数组计算出来. 然后dfs.  5-S2
    http://blog.csdn.net/yutianzuijin/article/details/16850031
    http://blog.csdn.net/linhuanmars/article/details/22777711
"""

class Solution1(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        ans = []
        self.dfs(s,[],ans,0)
        return ans
    def dfs(self,s,path,ans,start):
        """
        path : 记录path
        start： 子序列起始位置
        """
        if start == len(s):    #末层
            ans.append(path[:])
            return
        for i in  range(start,len(s)):
            if self.isPalindrome(s,start,i) :
                path.append(s[start:i+1])
                self.dfs(s,path,ans,i+1)
                path.pop()    #pop [aab]  包含[a]递归完后pop，继续[aa]
        return

    def isPalindrome(self,s,left,right):
        """
        判断是否回文
        left <= right   # Sure  
        """
        while left <= right:
            if s[left] != s[right]:
                break
            left += 1
            right -= 1
        else:
            return True   #case Yes
        return False


"""
S2: 
    leetcode 方法. O(n2) 
    -- 与S1 相比较复杂. 需要自行记录多步result.
    [a,a,b]
        [a] ：  result =  [['a']]   #初始结果
        [a,a] : result = [['a','a'],['aa']]    # 当添加a后,我们依据上层结果修改本层.
        [a,a,b]: result = [['a','a','b'],['aa','b']] # 添加b后,判断aab、ab、b 是否回文. 回文则能和之前的result合并,形成新的结果.
        # 综述 [1,2,3,4,5] 例如我们已知长度为5串的result. 现在我们添加X 元素后计算新的result. 如何计算？
            首先判断 1-X (12345X) 是否回文. 回文则 add 到本层result
            继续:    2-X  如果回文, 我们可以将 [1] 的result 和 2-X 合并 形成result
                     3-X  如果回文, [1,2]构成的result 可以和3-X组合
                     4-X 如果不是回文,直接Pass即可.
            由上可知我们需要dp[i][j] 存放i-j 是否回文,此外不仅仅记录上层result, 必须记录所有层result 
T：
    [a,a,b]   dp数组. 具体看5 最长回文
             1  2  3
           1 T  ？ ？
           2    T  ？
           3       T
        for i  in range(len(s)):   #外层 每次add 一个元素
            for j in range(i+1):   # 判断dp[j][i] 如果回文 与之前ans 组合
                if dp[j][i]:
                    tmp = s[j:i+1]
                    ansj = result[0-j]   #0-j的result
                    add tmp 到 ansj 每个元素中.  如[['a']] -> ['a','a']
                    ansj 是本层的一种结果 记录下来.
        以下方法 将求dp数组和 上述 组合.


R:
    https://discuss.leetcode.com/topic/2884/my-java-dp-only-solution-without-recursion-o-n-2
"""
import copy 
class Solution(object):
    def partition(self, s):

        s_l = len(s)
        dp = [[0]*s_l for i in range(s_l)]   #dp[i][j] = 1 ->i-j 回文
        ans = [[[]]]   #ans数组存放每层result, ans[0] = [[]] 空结果集
        
        for i in range(s_l):
            ans.append([]) #存放本层result
            for j in range(i+1): #add s[i]后,判断dp[0][i] dp[1][i]...并与之前result(ans[i])组合
                if s[i] == s[j] and (i-j <=1 or dp[j+1][i-1]):   # j-i 回文. 将[0-j]的result 和 s[j-i]合并,
                    dp[j][i] = 1
                    tmp = s[j:i+1]
                    ans_j = copy.deepcopy(ans[j])  #深度copy
                    [t.append(tmp) for t in ans_j]
                    ans[i+1].extend(ans_j)   #
        return ans[-1]







if __name__ == '__main__':
    S = Solution()
    ss = S.partition("aba")
    print(ss)