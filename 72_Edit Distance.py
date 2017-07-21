"""
Given two words word1 and word2, find the minimum number of steps required to convert word1 to word2. (each operation is counted as 1 step.)

You have the following 3 operations permitted on a word:

a) Insert a character
b) Delete a character
c) Replace a character

最少变换步数 from s1 to s2

T: 115 97

和115叫相似,都是将S1变换到S2！

"""



"""
S1:  DP 从下到上  二维数组  时间o(n^2) 空间o(n^2) 可以优化为o(n)

    1. 划分子问题 找到最优子结构;  2. 重叠子问题; 

    * 问题分析：

                给定S1转换为S2的最少步骤;

                f(i,j) : 表示从S1[0:i]转换到 S2[0:j]最少步数;  则 求f(len(S1), len(S2))

                问题分解： f(i,j) 核心是对S1[i]采取什么动作。 每种动作可能转换为不同的子问题;
                        1. Insert  
                        2. Delete
                        3. Replace

                            if S1[i] == S2[j] : 不操作S1[i]最好 ;  f(i-1,j-1)    #使用S1[i] 和S2[j] 匹配
                            else S1[i] != S2[j] :
                                                Delete : f(i-1,j)+1   # 删除S1[i]那么只能看f(i-1,j)结果
                                                Replace: f(i-1,j-1) +1 # S1[0:i-1] 和S2[0:j-1] 还是按照f(i-1,j-1)match; S1[i]替换后和S2[j]match
                                                Insert : f(i,j-1) +1  # 在S1[i]之后insert,使得新插入的字符和S2[j]match, 则需使用f(i,j-1)
                            3 种操作中insert 稍微别扭点;

                        **划分问题**
                                    ： 可以假想计算f(i,j)时刻, 我们需要的f(ii,jj)信息全部已知;
                                       所以关注点： 集中到如何处理s1[i] 和 s2[j] 中!!!

    * 伪代码：
                 f(i,j)  uses: f(i-1,j-1) f(i-1,j) f(i,j-1) : 使用到 左 上 左上  3个方向的Node;

                 故使用二维矩阵; 也可以压缩使用一维;

                        1. 需要对第一行 第一列单独处理 (或者使用一个m+1 * n+1 矩阵处理好外围层)
                        2. 依次行遍历
                            for i in 1...len(s1):
                                for j in 1...len(s2):  #cal f(i,j)
                                    3操作
                        return[-1][-1]


                * 关于外围层 或者 第一行列如何处理：

                    1.1  第一行处理：
                                    S1 = "a"  S2 = "abcde"  f(0,i) 即将S1[0]  转换为S2[0:j] 最少步; 
                                    S1[0] == S2[0] 则 f(0,0) = 0  其余f(0,i) = i
                                    S1[0] != S2[0] 则 f(0,0) = 1  其余f(0,i) = i+1(insert + 第一步replace)
                        第一列处理：
                                    同理S1 = "abcde" -> S2 = "a" 求f(i,0)
                                    1.1.1   S1[0] == S2[0] 则f(0,0) = 0 : 其余f(i,0) = i # del 
                                            S1[0] != S2[0] 则f(0,0) = 1 del; f(1,0) 重复1.1.1 步骤
                                    总结： 第一列就是将前缀!=S2[i] 的设置为 f(i,0) = f(i-1)+1; 如果S1[i] == S2[0] f(i,0) = f(i-1,0) 剩余的还是f(i-1)+1

                    1.2  使用外围行列：

                                    1.1 中处理过于繁琐; 需要判断S1[0]  S2[0]; 如果增加一个外围层较方便;  由于增加一行一列 所以f(i,j)偏移

                         第一行：  S1 =  ""  S2 = "abcde" 
                                    f(0,0) : 即 "" 转换为"" 次数显然是0;  
                                    f(0,1) : 即"" 转换为"a" 次数显然1; ...
                         第一列：  S1 = "abcde"  S2 = ""
                                   f(1,0) = "a" 转换为"" 次数显然是1
                                   ...
                        利用空串处理第一行列很方便;
"""

class Solution1(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """

        m , n = len(word1) , len(word2)
        stat = [[0]*(n+1) for i in range(m+1)]

        # 第一行 f(0,i)
        for i in range(n+1):
            stat[0][i] = i
        # 第一列
        for j in range(m+1):
            stat[j][0] = j

        for i in range(1,m+1):
            for j in range(1,n+1):   #cal f(i,j)  S1[i-1] S2[j-1]
                if word1[i-1] == word2[j-1]:
                    stat[i][j] = stat[i-1][j-1]
                else :
                    stat[i][j] = min(stat[i-1][j-1],stat[i-1][j],stat[i][j-1])+1 
        
        return stat[-1][-1]                      




"""
S2: 
    dfs+cache

    * 问题划分：
                使用递归反而好写;
                S1中递推式 f(i,j) 判断S1[i] S2[j] 进而转向子问题即可;
                唯一需要关注的就是：  递推终止;
                防止i,j 越界;  

                为了统一迭代式： f(i,j) 还是表示 S1[0:i] 转换为S2[0:j] 最少步数; 即求解f(len(s1),len(s2))

    * 伪代码：
              S1 -> S2
              recur(i,j)  #s1 i | s2 j

                # 终止判断

                if j == 0 : #s2 end
                    return i
                if i == 0 :
                    return j

                if s1[i] == s2[j]:
                    return  recur(i-1,j-1)
                else : 
                    return min(3 case ) +1
"""

class Solution2(object):
    def minDistance(self, word1, word2):
        """

        """

        #cache = [ [-1]*len(word2) for i in range(len(s1)) ]
        cache = dict() # 使用dict 空间少点
        ans = self.recur(word1,word2,len(word1)-1,len(word2)-1,cache)
        return ans



    def recur(self,s1,s2,s1_e,s2_e,cache):
        """
        return s1[0:s1_e] -》 s2[0:s2_e]  最少转换步

        """
        if cache.get((s1_e,s2_e),-1)!=-1:
            return cache[(s1_e,s2_e)]

        if s1_e < 0:   #注意此处<  表示s1已经空串
            cache[(s1_e,s2_e)] = s2_e+1
            return s2_e+1
        if s2_e < 0:
            cache[(s1_e,s2_e)] = s1_e+1
            return s1_e+1

        if s1[s1_e] == s2[s2_e]:
            cache[(s1_e-1,s2_e-1)]  = self.recur(s1,s2,s1_e-1,s2_e-1,cache)
            return cache[(s1_e-1,s2_e-1)]
        else : 
            tmp1 = self.recur(s1,s2,s1_e-1,s2_e-1,cache)
            tmp2 = self.recur(s1,s2,s1_e-1,s2_e,cache)
            tmp3 = self.recur(s1,s2,s1_e,s2_e-1,cache)
            cache[(s1_e-1,s2_e-1)] = tmp1
            cache[(s1_e-1,s2_e)] = tmp2
            cache[(s1_e,s2_e-1)] = tmp3
            cache[(s1_e,s2_e)] = min(tmp1,tmp2,tmp3)+1
            return cache[(s1_e,s2_e)]

        








if __name__ == '__main__':
    S2 = Solution2()
    ans = S2.minDistance("asfsfssdfsds","asdasdasdas")
    print(ans)

    S1 = Solution1()
    ans1 = S1.minDistance("asfsfssdfsds","asdasdasdas")
    print(ans1)