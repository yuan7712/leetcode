"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.

"""



class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        my_stack = []
        my_dict  = {']':'[','}':'{',')':'('}

        for ch in s :
            if ch in ['[','{','('] : #入栈
                my_stack.append(ch)
            elif ch in [']','}',')'] : #出栈判断
                if len(my_stack) == 0:
                    return False
                elif my_stack.pop() != my_dict[ch] :
                    return False
                else : 
                    pass

        if len(my_stack) == 0 : 
            return  True
        else : 
            return False



if __name__ == '__main__':
    S =Solution()
    ss = S.isValid("{{")
    print(ss)










"""
Q : 
     括号匹配， 使用栈
     
     python  栈 使用list 模拟， append 和 pop 入栈出栈。
"""