"""
Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

For example,
S = "ADOBECODEBANC"
T = "ABC"
Minimum window is "BANC".

Note:
If there is no such window in S that covers all characters in T, return the empty string "".

If there are multiple such windows, you are guaranteed that there will always be only one unique minimum window in S.

"""


"""
S1: 
    error
    1. 设置list  存放各个元素位置. 
    2. 从前到后依次扫描, 当以A 开头扫到一个完整的后, 直接切换到3号位B
T: 
    T串为不重复字符时,适用.   默认了每个字符只要一次
    2. 修改isNeed函数可以适合重复
"""
class Solution1(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        loc = []
        t_num = [0]*len(t)   #该字符num
        min_len = 2**31
        ans = []
        start,end = 0,0 #end
        def isNeed(t):  #判断此时是否还需要字符
            for i in t:
                if i <=0:
                    return True
            return False

        while end < len(s):  #尾指针一直向后
            if s[end] in t:
                loc_i = t.index(s[end])  #记录需求
                t_num[loc_i]+=1
                loc.append(end)  #记录包含字符的位置
                while not isNeed(t_num) :  #all num >0   cal min   **while**
                    num = end-loc[start]+1
                    loc_j = t.index(s[loc[start]])
                    t_num[loc_j]-=1
                    if num < min_len:   #mark min
                        min_len = num
                        ans = [loc[start],end]
                    start+=1  #不再del 当前串起始  loc[start]
            end+=1
        if len(ans) == 0:
            return ""
        return s[ans[0]:ans[1]+1]


"""
S2: 
    超时  允许重复字母 
    -- 耗时操作 isNeed
    -- 修改isNeed  Pass
R:
    http://www.cnblogs.com/lichen782/p/leetcode_minimum_window_substring_3.html
"""
class Solution2(object):
    def minWindow(self, s, t):
        loc = []   # 记录下次start位置  
        need = {}  #需求 dict各个字母个数,  也可以 int[256]
        t_num = {}   #计数  start-end 串中各个字母存在个数
        min_len = 2**31   #min
        ans = [] 
        for i in t:
            if need.get(i,-1) == -1:
                t_num[i] = 0
                need[i] = 1
            else:
                need[i]+=1
        start,end ,f_num = 0,0,0    # f_num 已经满足需求字母个数,
#        def isNeed(t,n,s):
#            for i in s:
#                if t[i] < n[i]:  #不足
#                    return True
#            return False

        while end < len(s):  #尾指针
            if s[end] in t:
                loc.append(end)  #记录下次start位置
                t_num[s[end]]+=1  #记录个数
                if t_num[s[end]] == need[s[end]] :  #满足需求,不可<= ;  <= 则和len(t)比较
                    f_num +=1
                #while  not isNeed(t_num,need,t) :
                while  f_num == len(need) :
                    num = end-loc[start]+1
                    t_num[s[loc[start]]]-=1  #num -1
                    if t_num[s[loc[start]]] < need[s[loc[start]]]: #
                        f_num -=1
                    if num < min_len:
                        min_len = num
                        ans = [loc[start],end]
                    start +=1
            end+=1
        if len(ans) == 0:
            return ""
        return s[ans[0]:ans[1]+1]

"""
S3:
    leetcode 方法  12 行
T：
    1. 使用collections模块对各个字母计数不必自己写. need[不存在] = 0
    2. missing 表示还需要几个字符. need 记录各个字母需求, =0 恰好 <0 表示超出
            与S1 S2 不同此处 此处只有一个need数组
            2.1  首先从前向后遍历找到一个 符合t的串
            2.2  当找到串后 此时need数组中 存在许多 <0 项;  约减
            2.2  找到一个串后missing =0 ; 此时各个字母必然不缺. 然后j一直向后add. 只要使用2.1 中约减就可以.
                 FFAABRCBA   ABC
                    1. 找到FFAABC  第一个满足的串  此时 missing=0 ; AF <0 
                        所以删FFA need[i]==0  ; (只针对前缀,当然可以need[b]>0) 尽可能将start向后移
                    2. 以上得到ABRC missing=0 ;
                        add B->   ABRCB  使用1.  删减 无可以删的
                        add A->   ABRCBA 使用1.  删减 ABR  ->CBA
R：
    https://discuss.leetcode.com/topic/20692/12-lines-python
"""
from collections import Counter
class Solution(object):
    def minWindow(self, s, t):
        need, missing = Counter(t), len(t)
        i = I = J = 0
        for j, c in enumerate(s, 1):
            missing -= need[c] > 0
            need[c] -= 1
            if not missing:
                while i < j and need[s[i]] < 0:
                    need[s[i]] += 1
                    i += 1
                if not J or j - i <= J - I:
                    I, J = i, j
        return s[I:J]



if __name__ == '__main__':
    S =Solution()
    ss = S.minWindow('FFABAC','ABC')
    print(ss)



