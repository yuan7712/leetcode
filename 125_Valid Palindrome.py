"""
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

For example,
"A man, a plan, a canal: Panama" is a palindrome.
"race a car" is not a palindrome.

Note:
Have you consider that the string might be empty? This is a good question to ask during an interview.

For the purpose of this problem, we define empty string as valid palindrome.

"""




"""
S1 :
    1. 注意str不可改变。 
    2. list 的逆置 使用切片[::-1]
"""
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s_new = []
#        for ch in reversed(s) :
#            if ch.isalnum() :  #字母or数字
#                s_new.append(ch.lower())
        s_new = [c.lower() for c in reversed(s) if c.isalnum()]   #使用列表生成式
        return s_new[::-1]== s_new



"""
S2 : 
    使用filter 过滤
"""
class Solution2:
    # @param {string} s
    # @return {boolean}
    def isPalindrome(self, s):
        # chars = filter(lambda c: c.isalnum(), s).lower() 
        chars = list(filter(lambda c: c.isalnum(), s.lower()))     #filter 返回的是一个生成器， 使用list 全部显示
        return chars[::-1] == chars




"""
S3 : 
    原地设置left right 判断。

"""

class Solution3(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s_len = len(s)
        left , right = 0 , s_len-1
        while left <right :   #当== 时true
            while left< right and not s[left].isalnum():
                left +=1
            while left<right and not s[right].isalnum():
                right -=1
            if s[left].lower()!=s[right].lower() :   #left right 不会越界。 不必判断
                return False
            left +=1
            right -=1
        return True

        
if __name__ == '__main__':
    S =Solution3()
    ss = S.isPalindrome("A man, a plan, a canal: Panama")
    print(ss)









"""
Q :  给定一个str  判断是否是回文。

    1. 去掉杂项，只保留数字和字符
         str python 为不可改变的。 使用isalnum() 方法判断是字母/数字
    2. 全部变为大写或者小写。
        lower()  小写(这些都是str 的函数)
    3. 判断回文
    
"""