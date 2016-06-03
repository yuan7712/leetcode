"""
Given a string S, find the longest palindromic substring in S. 
You may assume that the maximum length of S is 1000, and there exists one unique longest palindromic substring.

"""


"""
S1 : 
    Leetcode Pass
    O(n^2)
    1. 整合了奇数和偶数问题，以某个元素为中心分别计算 奇和偶长度的 回文串。
    2. 在i位置 (i,i+1) 和(i-1,i+1) 分别向两边扩展即可。 
"""
class Solution1(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        ans ,center= 0,0  #center记录回文中点 ans长度
        l_s = len(s)
        for i in  range(l_s):
            l1 = self.findLongest(i-1,i+1,s)
            l2 = self.findLongest(i,i+1,s)
            l =max(l1,l2)
            if l>ans:
                ans = l
                center = i
        if ans%2 : #奇数长度
            return s[center-ans//2:center+ans//2+1]
        else :
            #print(center,ans,center-ans//2+1,center+ans//2)
            return s[center-ans//2+1:center+ans//2+1]

    def findLongest(self,left,right,s):
        """
        从left right 向两边滑动，返回序列长度
        """
        l_s = len(s)
        while left>=0 and right<l_s :
            if s[left] != s[right]:
                break
            left -= 1
            right += 1
        return right- left -1


"""
S2： DP  超时！

    1. 使用dp[i][j]  表示i->j 是否是回文串；
            如果s[i] == s[j] 那么是否是回文决定于 dp[i+1][ j - 1]
            如果s[i] != s[j] 的时候， dp[i][j] 直接就是 false。
    2. 动态规划的进行是按照字符串的长度从1 到 n推进的。

    3. 相当于会对所有可能长度的串进行判断是否回文。(只不过利用了长度k-1的信息)
         超时！！！


"""
class Solution2(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        s_l = len(s)
        if s_l<=1:
            return s
        dp = [[0]*s_l for i in range(s_l)]
        ans = 0
        left, right = 0,0
        # 设置初始矩阵，dp[i][i]为单个长度设置True
        dp[0][0] = True
        for i in range(1,s_l):
            dp[i][i] = True
            dp[i][i-1] = True   #不可忽略，当我们判断长度为2即s[0]==s[1]时，dp[0][1]由dp[1][0]决定，所以必须预先设置True.至于其余不必设置;
        
        # k+1 表示当前回文长度，我们判断每种长度回文。
        for k in range(1,s_l):
            i = 0
            # 对每种长度回文遍历所有可能； 长度2时 ： 0,1  1,2  2,3  3,4 ...
            while k+i <s_l:
                j  = k+i
                if s[i] != s[j]:
                    dp[i][j] = False
                else :
                    dp[i][j] = dp[i+1][j-1]
                    if dp[i][j] and k+1>ans:
                        ans = k
                        left =i
                        right = j
                i +=1

        return s[left:right+1]



"""
S3: Manacherą s Algorithm
    此方法和S1类似,也是要按照从每个元素出发分别向两边扩展计算最长回文。 使用#填充到字母之间处理奇偶数问题。

    1. 和S1 中不同的是,预先计算每个位置扩展的回文长度。
         计算P数组：
          1.1  C R 保存上次最靠右回文的 中心的右边界、
          1.2  当计算P[i] 时，如果i在R左侧，则C左边有个和i对应的i_morrir; 我们能保证i回文长度至少 min(R-i,P[i_mirror])
                P[ i_morrir ] < R – i, 都不必扩展，可以直接使P[i] =  P[ i_morrir ]
                所以我们可以按照该长度继续向后比较，而不是从该点每次从0开始两边扩展。
          1.3  当找到的右边界>R时 可以更新C R  以备下次使用值。
          1.4  如果i>=R  表示我们不能使用上次的回文 加快判断，只能从0开始向两边扩展计算长度。
    2. 最后我们变量P数组找到最长回文，和中心点。 (此时包含#，去除即可)
         max_len  max_center  我们找到的串均是#在两边的。(预处理时将每个字母两边添加#)
         观察知： max_len 即为原回文串长度。
         (max_center  - max_len)//2 即左边界。 max_center - max_len 为找到的ss中的回文左边界#

Q： 
    1. 在对s转变时 应该在每个字符前后都加#, 这样最后能方便确定原回文串
R：
    1. http://blog.csdn.net/hopeztm/article/details/7932245#
    2. http://www.cnblogs.com/TenosDoIt/p/3675788.html
"""
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        s_l = len(s)
        if s_l<=1:
            return s
        ss = '#'.join(s)
        ss = '$#'+ss+'#^'   #前缀加# 统一方便后面确定回文串,字母前后都是#，最后就不必再分类判断，加上$^ 省去判断边界。
        ss_l = len(ss)
        P =[0]*(ss_l)
        C, R = 0,0   #使用C表示上次回文中心，R表示回文右边界。

        for i in range(1,ss_l-1):   #不管^和$
            i_mirror = 2*C -i
            P[i] = min(R-i,P[i_mirror]) if R>i else  0
            while ss[i+1+P[i]] ==ss[i-1-P[i]]:   # 因为有边界^ $所以不必判断越界
                P[i]+=1
            if i+P[i]>R:  #更新R
                C = i
                R = i+P[i]
        print(P[1:ss_l-1])

        max_len = 0
        max_center = 0
        for i in range(ss_l):
            if P[i]>max_len:
                max_len = P[i]
                max_center = i

        l  = (max_center  - max_len)//2
        return  s[l:l+max_len]



if __name__ == "__main__":
    s = Solution()
    ss = s.longestPalindrome("abba") 
    print(ss)

        










if __name__ == "__main__":
    s = Solution()
    ss = s.longestPalindrome("abb") 
    print(ss)





"""
Q： 
    计算字符串最长的回文
    1. 最暴力即： 找出所有的字符串， 挨个判断是否回文。 o(n^3)
    2. S1 : o(n^2)  从每个元素向两边扩展。
    3. S2：DP.  超时？
    4. S3 ：Manacherą s Algorithm   优 O(n)
"""