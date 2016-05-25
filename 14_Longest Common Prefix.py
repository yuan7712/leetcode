class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs :
            return ''
        str_max = 2**31 -1
        for i in range(len(strs)):
            str_max = min (str_max,len(strs[i]))
        ans = 0
        now = ''
        for j in range(str_max):
            now = strs[0][j]
            k = 0
            while k<len(strs): 
                if strs[k][j] != now :
                    return strs[0][:j]
                else :
                    k +=1
        return strs[0][:str_max]


if __name__ == '__main__':
    S = Solution()
    SS = S.longestCommonPrefix([['ss']])
    print(SS)                    





"""
Q : 最长前缀匹配，只需防止越界问题即。 此处先判断最短的串长度。最后返回ans 使用切片。
     也可以每次判断 strs[i] 长度防止越界。

"""
