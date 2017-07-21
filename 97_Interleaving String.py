"""
Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.

For example,
Given:
s1 = "aabcc",
s2 = "dbbca",

When s3 = "aadbbcbcac", return true.
When s3 = "aadbbbaccc", return false.

题目： 
    1. 首先len(s1) + len(s2) = len(s3)
    2. s3是由s1 s2 交叉组成;  s1可以分为m段 s2分为n段， 然后二者按照顺序交叉;



类比： 72
     之前的dp题目大部分是 对字符串切割, 如切割为每段都是回文等; 但是本题目需要对S1 S2 两个切割;

115 

"""





"""
S1:       DP  o(n^2)  一维长度数组 o(n)  beats 96%


        1. 划分子问题 找到最优子结构;  2. 重叠子问题; 

    * 子问题：
            len(s3) = n = len(s1) + len(s2)
            f(i) 表示S3[0:i]  是否能由s1和s2组合(都指某个前缀); 那么此题问题就转换为 f(n)

            问题分解： 对于求解f(i) 我们只要确定s3[i]应该由s1还是s2确定即可; s3[0:i-1]已经由f(0) ...f(i-1)确定;
                        1.  如何确定s3[i] 属于s1 还是s2 ? 
                            A: 实际上对于f(i) 其可能由多种不同组合长度的s1 s2 前缀构成,但是二者和必然是i
                               ** 所以可以使用f(i)记录 (a,b) 数组：  表示s1[0:a]和s2[0:b]能够交叉成为f(i)  a+b = i  **
                               f(i) ： 依次遍历f(i-1) 集合尝试将s3[i] 合并到s1 or s2 中;

                               如果f(i) == None ： 表示 s3[0:i] 并不能由s1和s2任何前缀交叉组成;  f(n) 也就没必要再继续算下去;
                               f(i) == [(1,9) (2,8)]   : 表示s3[0:i] 可以由不同组合前缀的s1 s2 构成;

                        2. 复杂度： 
                                按照以上思路, f(i)只会使用到f(i-1);

                                for i in 0...n:  #s3[i]
                                    for item in f(i-1): #item = (a,b)
                                        if s3[i] == s1[a+1]:
                                            f(i).append(a+1,b)
                                        if s3[i] == s2[b+1]:
                                            f(i).append(a,b+1)
                                return f(n) == None

                                **以上f(i)存放的(a,b) 最大长度也就是 2i ;**

                                **时间复杂度都是 o(n^2)**

                        3. 关于找到具体解，path还原：
                                如果需要找到所有的path; 那么就需要保存所有f(i);
                                然后从f(n)递归组合这些可能性;  过程很繁琐;



"""

class Solution1(object):
    def isInterleave(self, s1, s2, s3):

        if len(s3) != len(s1) + len(s2) :
            return False 

        last  = set()  # ((i,j) , (i2,j2))  
        last.add((-1,-1))

        for i in range(len(s3)):   # cal f(i) 
            tmp = set()
            for (m,n) in last :   #(i,j)
                if m+1 <len(s1) and s3[i] == s1[m+1]:
                    tmp.add((m+1,n))
                if n+1 <len(s2) and s3[i] == s2[n+1]:
                    tmp.add((m,n+1))
            last = tmp
            if not last:
                return False

        return True



"""
S2 : 
    DP  从上到下  递归+cache  

    * 问题划分 ：
                还是和S1中类似
                f(i)  核心还是确认s3[i] 属于s1 or s2

    * 伪代码： 
              f (s3_b, s2_b, s1_b):    #s3+b = s1_b + s2_b 
                 boolean b1 = s3[s3_b] == s1[s1_b] && f(s3_b,s2_b,s1_b+1)   # use s1
                 boolean b2 = s3[s3_b] == s2[s2_b] && f(s3_b,s2_b+1,s1_b)   # use s1
                 return b1 || b2

            所以可以使用cache缓冲结果，虽然参数3个,但是s3+b = s1_b + s2_b  所以只要保存一个二维数组即可;


"""
class Solution2(object):
    def isInterleave(self, s1, s2, s3):
        pass




"""
S3：  DP 使用二维数组;

     * 问题划分： 
                和S1中问题划分类似。
                S1中是从  "s3" 角度出发判断 f(i)  到底能分为几种 s1 s2 前缀;

                此方法就是直接使用 二维数组 stat[i][j]  表示 s1[0:i] 和 s2[0:j] 是否能组成s3[0:i+j] 
                     其实和S1解法划分基本一致, 只是角度不同而已;

    * 伪代码： 
                 m = len(s1) n = len(s2)  m+n = len(s3)

                 公式： stat[i][j] = stat[i-1][j] && s1[i]==s3[i+j]    or stat[i][j-1] && s2[j]==s3[i+j] 
                        计算 stat[i][j] 只会使用到 左边和上边;   所以我们依次行遍历基三stat即可；(第一行可能单独处理)

                        for i in 1...m :
                            for j in  0...n:  #cal stat[i][j]
                                #use stat[i-1][j] and stat[i][j-1]
                                stat[i][j] = 公式...

                        return stat[-1][-1]

    * 复杂度：     时间o(n^2) 空间o(n^2)  由于只使用左边上边 稍微优化 o(n) ??



* R : 
    https://discuss.leetcode.com/topic/3532/my-dp-solution-in-c
"""
class Solution3(object):
    def isInterleave(self, s1, s2, s3):
        pass




"""
S4 : 
    BFS ：
    https://discuss.leetcode.com/topic/6562/8ms-c-solution-using-bfs-with-explanation

    见S中分析; 其实和dp 二维数组类似;
    
"""





        
"""
S:  ****

    dp求解，问题有多种方法进行子问题划分， 善于寻找较为便捷的问题划分方法;   不同划分方法 复杂度也有较大差异;

    * S2 S3 S4 总结：

            这三种方法, 分别使用递归dfs ,dp二维数组 , BFS 求解;

        * 重新看问题: 
                给定 s1 s2 看是否能交叉成为s3;  m = len(s1)  n = len(s2)
                看做一个排列组合问题, S1 S2 有序, 给定m+n 个位置,  如何确定S3? 显然有 **   C m+n M 种情况;**

                m+n 个位置从前往后  依次确定每个操作 选择s1 还是 s2;

                将此动作描述为一个矩阵  m*n    s1 = "aabcc"  s2"dbbca":
                    s2: d b b c a 
                  s1:(S)
                  a
                  a
                  a
                  b
                  c             (E)

                  在此矩阵中起始位置 (S)表示s1 s2 中任何字符都没有选择;  向右走一步 表示选择s2的一个字符; 向下同理;
                  ** 那么我们的问题就变成 从(S) 到(E) 是否可达!!!**  (E)状态即使用所有的s1和s2交叉;

                     * 动作确定： 此处目标串s3: 所以每次移动时必然进行判断; 如(i,j)位置向右移动到(i+1,j)则需要判断s3[i+j+1] == s1[i+1] 
        * BFS DFS DP:
                S3 DP二维： 
                        此方法即计算该矩阵中每个Node; 从左上角一直计算到右下角;
                S2 DFS递归：
                        左上角递归执行, 深度搜索, 使用cache 复杂度降低不少; 而且并不会计算全部(i,j)中途如果到达了(E)那么直接返回结果即可;  **故有时和DP二维相比反而高效!**

                S4 BFS:
                        广度搜索;  S->E ; 空间复杂度上应该比 S3低些，使用队列；
        
        * 总结： 
                最好使用 dfs+ cache ！
                dp + 二维有时不好调试


"""

if __name__ == '__main__':
    s = Solution()
    ans = s.isInterleave("aabcc","dbbca","aadbbbaccc")
    print(ans)

"""
s1 = "aabcc",
s2 = "dbbca",

When s3 = "aadbbcbcac", return true.
When s3 = "aadbbbaccc", return false.

""" 