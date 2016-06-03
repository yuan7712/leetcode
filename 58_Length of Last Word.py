"""
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.

For example, 
Given s = "Hello World",
return 5.

"""


"""
S: 
    1. 找到最后一个单词长度. 逆向遍历即可
    2. case 'a    '  首先应该将末尾空格去掉;
"""
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if  not s :
            return 0
        i = -1
        num = 0
        while i >= -1*(len(s)) and s[i]==' ':   # remove  " "
            i-=1
        while i >= -1*(len(s)) and s[i]!=' ':   # 逆向遍历 
            num+=1
            i-=1
        return num

if __name__ == '__main__':
    S =Solution()
    ss = S.lengthOfLastWord('ss ass     ')
    print(ss)