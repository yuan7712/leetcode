class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        1. 使用滑动 start 和end(此处使用i)
        2. 依次遍历， 当dict 中不存在，存入dict(存放location方便start更改)
        3. 当i位置与start之后的重复后，直接更新 start,并重置该字符location
        4. 最后max(ans,i-start+1)， 防止‘abcd’ 
        """
        str = {}
        ans = 0
        start  = 0
        i = 0
        l = len(s)
        if not l:  #空串返0
            return 0 
        for i in range(len(s)):
            lca = str.get(s[i],-1) #获取位置。
            if lca < 0  or lca<start:  #-1 不存在，因为start之前还可能包含该字符
                str[s[i]]=i #存位置
            else :
                ans = max(ans,i-start)
                start = lca+1
                str[s[i]] = i
        return max(ans,i-start+1)




class Solution2:
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        """
        1. 此与上一个基本一致，单独使用end++，所以不必防‘abc’
        2. start 使用逐步改变 whlie 将重复元素一个个置为0.上一个直接改变start
        """
        ans, start, end = 0, 0, 0
        countDict = {}
        for c in s:
            end += 1
            countDict[c] = countDict.get(c, 0) + 1
            while countDict[c] > 1:
                countDict[s[start]] -= 1
                start += 1
            ans = max(ans, end - start)
        return ans        






re = Solution2()
s = re.lengthOfLongestSubstring('abc')
print(s)