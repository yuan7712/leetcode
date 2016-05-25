#coding=utf-8
"""
Implement strStr().

Returns the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

"""


"""
S1: 
    暴力  O(nm)   
"""
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        n_len , h_len = len(needle),len(haystack)
        if n_len > h_len :
            return -1
        for i in range(h_len-n_len+1) :
            j = 0
            while j < n_len and needle[j]==haystack[i+j]:
                j+=1
            if j >=n_len :
                return i
        return -1


"""
S1 -JAVA

public int strStr(String haystack, String needle) {
  for (int i = 0; ; i++) {
    for (int j = 0; ; j++) {
      if (j == needle.length()) return i;
      if (i + j == haystack.length()) return -1;
      if (needle.charAt(j) != haystack.charAt(i + j)) break;
    }
  }
}

"""



"""
S2 : 
    KMP  O(m+n)
    1. 使用next数组，由getNext函数计算。next 数组表示当在此位置失配时，needle 数组的指针该指向哪个位置。
    2. strstr()   依次向后匹配， 指向原串指针i needle指针j;  当失配时i不会回溯 而是指向needle 中的某个元素开始， 而此元素即 next数组中的值
    3. KMP  是从前到后移动needle 串， needle 串也是从前到后匹配。 利用已经匹配的信息，确定最大应该向右移动几个单位。
    4. KMP 的关键即  如何计算next数组，确定该位置失配时移动位数。  此处的计算使用递归思想。
"""
class Solution1(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle :
            return 0
        if not haystack :   #haystack 空 need非空
            return -1
        needle_next = self.getNext(needle)

        i = 0
        j = 0
        while i < len(haystack) and j <len(needle):
            if j ==-1 or haystack[i] == needle[j]:
                i +=1
                j +=1
            else :   #调整i  和 j   ;j使用next i不回退 (当j为-1  i++)
                j = needle_next[j] 

        if j ==len(needle):
            return i -j
        else :
            return -1



    """
    next: 
        获取needle 的next 数组
        1. 从前向后依次计算每个位置的 next 值。 0位置-1 直接向后 移动一个单位。(即第一个不匹配)
        2.  计算i的next时，使用i-1 信息，k = next[i-1] 即在i失配，字串移向k,(它之前k个和i-1之前k个一致)， 
             当 needle[k]==needle[i-1]:  next[i] = k+1 
             否则一致递归找到合适的k
    """
    def getNext(self,needle):

        needle_len = len(needle)
        my_next = [None]*needle_len  # 存放next
        my_next[0] = -1
        for i in range(1,needle_len):
            k = my_next[i-1]
            while k!=-1 and needle[k]!=needle[i-1]:
                k = my_next[k]
            k +=1   #当0 时设置1
            my_next[i] = k

        return my_next
    






"""
BM :
    此算法要比KMP优 几倍。
    1. 核心思想和KMP 类似，即当字串和s 不匹配时候， 尽可能的向后移动。
    2. BM 依然是只移动字串，但是 字串内部的比较是 从后向前的。
    3. 使用了两个预计算值，确定i位置失配时向右移动几个单位、

        3.1 坏字符：   S: ssssssssybadddd P : abyaaba   
            如 当在5处的b失配， 我们应该向右移动3个单位，将P 中的y和之前失配位置S中的y 匹配。
                所以我们应该记录P中每个字符的最后出现的位置。
                此处可能会出现 y在5处b 之后，即 负偏移，此时肯定不能向左移动P，所以我们考虑好后缀
        3.2 好后缀： P : abcabbabcd
            当在5处的b失配，此时后缀abcd 已经匹配， 所以可以考虑前面是否有abcd 或者子后缀 出现 向后移。
                1. 在字串中最右出现abcd 可以移到此处，与s 中abcd 匹配
                2. 如果 不存在abcd 这样全部匹配，可以判断bcd cd d 能和开头匹配。(因为没有全部匹配abcd 字串，所以尽可能向右)
                3. 以上均没有 即将整个串向右移动 串长
    4. 坏字符数组 好计算，给定256字符，依次遍历needle即可。
    5. 核心如何计算 好后缀数组：？
        此处使用suff 数组， suff[i] 表示 以i结尾和 P 串末尾 最多能匹配 位数。(此处两种方法 suffix 和suffixPro（快）)

"""
class Solution2(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        m = len(needle)
        n = len(haystack)
        if not m :
            return 0
        if not n :
            return -1
        # 预计算两个数组
        bmBc = self.bmBad(needle)  
        bmGc = self.bmGood(needle)

        j = 0 
        while j <=n-m :
            i = m-1 
            while i >=0 and needle[i] == haystack[i+j] :   #字串中从后向前匹配
                i -=1
            if i <0: #find ans
                return j
            else:  # 向右偏移
                j += max(bmGc[i],i-bmBc[ord(haystack[i+j])])  # 出现失配时 向右偏移， 选择坏字符和好后缀的最大偏移。(注意坏字符偏移计算时使用haystack中字符)

        return -1

#坏字符数组： 使用256 字符长度数组。记录最后出现位置i.  不必考虑P最后一个元素
    def bmBad(self,needle):
        m = len(needle)
        bmBc = [m]*256
        for i in range(m-1):
            bmBc[ord(needle[i])] = i

        return bmBc


# 辅助数组，为了计算好后缀数组。  s[i]  表示以i结尾的字符串和 needle末尾能匹配的最大长度; 此方法慢，即 一个个比较计算。
    def suffix(self,needle):
        m = len(needle)
        suff =[0]*m
        suff [m-1] = m #最后一个表 即全部匹配
        for i in range(m-2,-1,-1):
            j = i 
            while j>=0 and needle[j] == needle[m-1-i+j]:
                j -=1
            suff[i] = i-j
        return suff


# 改进的计算方法， 计算i位置时， 尽量使用上次的suff匹配，

    def suffixPro(self,needle):
        m = len(needle)
        suff  = [0]*m
        suff[m-1] = m
        g = m-1  #g 表示上次失配的位置， f 表示上次suff 匹配的起始位置。
        for i in range(m-2,-1,-1):
            if i>g and suff[m-1+i-f] < i-g :  #上次匹配在g失配， i在g之后，而且 之前有个对应位置m-1+i-f的suff 值恰好在g 之前，所以可以利用此值。
                suff[i] = suff[i+m-1-f]
            else:   # 此时不能继续使用上次suff, 应该重新计算匹配，当i<g ,g 退到i 处一个个开始匹配，当i>=g  此时必然是m-1+i-f 处的suff 值较大，所以不必调整可以继续比较

                if i<g:
                    g = i
                f= i
                while g >=0 and needle[g] == needle[g+m-1-f]:   
                    g -=1
                suff[i] = f-g

        return suff



# 计算好后缀数组 ,bmGc 在位置失配应该滑动个数
    def bmGood(self,needle):
        m = len(needle)
        suff = self.suffixPro(needle)
        bmGc = [0]*m
        #case 1 , 也可以放在此处。
        #bmGc = [m]*m   #置初值为m, 找不到好后缀即偏移m

        # case 2  ： i处失配， 之后的字串 要和开头处匹配， 除了末尾只有一处suff[i] == i+1, m-i 之前的失配 均可使用此
        bmGc[m-1] = 1 
        for i in range(m-2,-1,-1):
            if suff[i] == i+1 :   
                for j in range(0,m-i):
                    bmGc[j] = m-1-i
                break
        # case 3  ： i 处失配， 后缀要全部匹配串中任意位置
        for i in range(0,m-1):
            bmGc[m-1-suff[i]] = m-1-i
        # case 1  任意位置没有匹配到， 只能全部向后移动m
        for i in range(m-1):
            if bmGc[i] == 0:
                bmGc[i]=m

        return bmGc



if __name__ == '__main__':
    S = Solution()
    ss = S.strStr('asfasfsadfdfgxvfghtwrwerretggggggeetevxcv','ggggg')
    print(ss)

"""
Q : 
    strStr(a,b) 判断b 是否是a 的字串。 返回下标 不在-1
    1. python str 中的find 方法。
    2. 使用暴力，依次遍历匹配
    3. KMP ... BM ... Rabin-Karp ... ???

R: 
    BM:  
        1. http://www.cnblogs.com/lanxuezaipiao/p/3452579.html#undefined
        2. http://www-igm.univ-mlv.fr/~lecroq/string/node14.html#SECTION00140
        3. http://www.inf.fh-flensburg.de/lang/algorithmen/pattern/bmen.htm     [ 此未实现，计算好后缀和上述不一样]
"""