"""
Given a string s, partition s such that every substring of the partition is a palindrome.

Return the minimum cuts needed for a palindrome partitioning of s.

For example, given s = "aab",
Return 1 since the palindrome partitioning ["aa","b"] could be produced using 1 cut.


## 131   Palindrome Partitioning   

最少切分几刀， 使得字串都是回文；


"""




"""
S1:  DP -- 超时！！o (n^3)

1. 划分子问题 找到最优子结构;  2. 重叠子问题; 

"AAB"

1. 划分问题：  对于n长串，能找到n-1个位置切分为两个最优子问题(或者不切分), 且 f(n) =  f(left) + f(right) ;
2. 重叠子问题： n长字串,  在k位置切分;   [start,k] + [k+1,end];  由于左右是两个不同问题.  所以应该使用矩阵记录 f(i,j) 表示i-j之间的最少刀数；
       公式： f(i,j) = 任意k f(i,k) + f(k+1,j) + 1  [对于非回文串可以将此项设置为无穷大]
              f(i,i) = 0
              最终求解的即 f(1,n) 
              使用矩阵M存储, 只会使用到矩阵右上角, 迭代计算时沿着东北方向遍历即可;  因为求解f(i,j) 必须知道比j-i 长的字串解；

3. 此问题和算法导论中一样

"""

class Solution1(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """

        if not s : 
            return 0

        n = len(s)
        stat = [[0]*n for i in range(n)]  # n*n 

        for i in  range(n):
            for j in range(n-i):  # [j, j+i]
                if j == j+i:  # single char
                    stat[j][j+i] = 0
                else: 
                    if self.isPalindrome(s,j,j+i) :  #  not cut 
                        stat[j][j+i] = 0
                    else:
                        tmp  = 2**30
                        for k in range(j,j+i):
                            tmp = min((stat[j][k]+stat[k+1][j+i]+1), tmp)
                        stat[j][j+i] = tmp

        print(stat[0][-1])
    

    def isPalindrome(self,s,left,right):
        """
        判断是否回文
        left <= right   
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

R :  https://discuss.leetcode.com/topic/2048/my-dp-solution-explanation-and-code 

    S1中DP分析正确, 但是子问题划分不合理导致复杂度o(n^3) (中途判断字串是否为回文也会造成复杂度提升);

    重新划分子问题;

    f(1,n) : 从1-n最少切分数; S1中采用 f(1,n) = f(1,k) + f(k+1,n) +1   划分为两个子问题;  需要使用二维矩阵存储f(i,j);

    *** 此处 f(1,n) 也是从前向后 在n-1 个位置切分； 分为两段： (1,k)  (k+1,n); 
        但是f(1,n) 求解不再依赖f(1,k) 转而判断(1,k)是否为回文  只依赖(k+1,n);  

         f(1,n) = f(1,k) + f(k+1,n) 任意K;     **只是对于f(k+1,n) 依然使用缓冲, 但是f(1,k)自行判断获取最小值**

        (1,k) 为回文串：  f(1,n)  = min  任意k  (f(k+1,n) + 1)    // 左侧回文不必切分  f(1,k) = 0
        (1,k)  非回文：   f(1,k) 最优解是什么呢？ 假设(1,k) 最优解 第一刀在j 位置切分; 
                          即 f(1,k) = f(1,j) + f(j+1,k)
                          f(1,n) = f(1,j) + f(j+1,k) + 1(j切分)  + f(k+1,n) + 1(k切分) ;  
                          然而  f(j+1,k) + 1  + f(k+1,n)   可以视为f(j+1,n)  最优解, 此最优解在求f(1,n)  已经知道了;

                          所以对于(1,k) 为非回文不必再考虑此处最优解, 之前f(1,j)已经考虑到了;


    * 遍历：  由于f(1,n) 只依赖f(k,n) 所以我们只要一维数组cache即可;  f(k,n) 含义：从k位置到末尾的最少切分刀数，最优解：
              计算f(1,n) 需要遍历每个空格，如果(1,k) 为回文则可以更新值; 

    * 和S1相比： f(1,n) = f(1,k) + f(k+1,n)
                 总的问题划分一致，但是S2更加精细划分，将f(1,k) 转换为f(j,n) 子问题，使得我们不必存储二维矩阵，使用一维即可;
    
    * 复杂度： 
            stat[n] //cache
            for i in n-1 ... 0: // 依次计算f(i,n)
                for k in i... n-1 : // 
                    if(1,k) 回文：  // 暴力o(n)
                          更新值;
            以上如果暴力回文复杂度 o(n^3)



    * 判断回文DP：
              S1中暴力判断回文; 
              使用DP改进 回文判断
              isPal(i,j) = s[i] == s[j] && s(i+1,j-1) == True

              计算f(i,n)时 会判断(i,k).  其中会用到(i-1,k)这些字串是否回文; 所以使用二维矩阵存储；
    
    * 复杂度 ： 
              当计算回文使用DP 后变为o(n^2)  空间也是n2

    * 关于记录具体解path: 
             创建一维数组，记录f(i,n)在那处划分为子问题即可；
             在fStat[i] = min(fStat[i], fStat[j+1]+1) 处记录该值；
             最后递归 还原解;
    


"""

class Solution2(object):

    def minCut(self, s):

        if not s : 
            return -1
        n = len(s)
        
        # f(i,n)  default  长度n=1,  当判断[i,n] 是否回文会使用到 f(n+1,n)  
        #  最后一个必须为-1 ; "aa" 假设确定在最末尾切，fStat[j+1]+1 为最小切分， 应该和我0；
        fStat = [i for i in range(n-1,-2,-1)] 

        pStat = [[False]*n for i in range(n)]  # pal stat p[i][j] == isPal(i,j)
#        for i in range(n):
#            pStat[i][i] = True

        for i in range(n-1,-1,-1):  # cal f(i,n)
            for j in range (i,n) :   # isPal[i,j]  f(j,n)
                if( s[i] == s[j] and  (  j < i+2  or pStat[i+1][j-1] == True) ):   # 注意先判断 i < j+2  防止越界， 如[a,b,c] 判断 (2,2)
                    pStat[i][j] = True
                    fStat[i] = min(fStat[i], fStat[j+1]+1)
        return fStat[0]







"""
Task: 

未看：

https://discuss.leetcode.com/topic/2840/my-solution-does-not-need-a-table-for-palindrome-is-it-right-it-uses-only-o-n-space/2
"""






if __name__ == '__main__':
    s = Solution2()
    s.minCut("aa")
    s.minCut("apjesgpsxoeiokmqmfgvjslcjukbqxpsobyhjpbgdfruqdkeiszrlmtwgfxyfostpqczidfljwfbbrflkgdvtytbgqalguewnhvvmcgxboycffopmtmhtfizxkmeftcucxpobxmelmjtuzigsxnncxpaibgpuijwhankxbplpyejxmrrjgeoevqozwdtgospohznkoyzocjlracchjqnggbfeebmuvbicbvmpuleywrpzwsihivnrwtxcukwplgtobhgxukwrdlszfaiqxwjvrgxnsveedxseeyeykarqnjrtlaliyudpacctzizcftjlunlgnfwcqqxcqikocqffsjyurzwysfjmswvhbrmshjuzsgpwyubtfbnwajuvrfhlccvfwhxfqthkcwhatktymgxostjlztwdxritygbrbibdgkezvzajizxasjnrcjwzdfvdnwwqeyumkamhzoqhnqjfzwzbixclcxqrtniznemxeahfozp")

