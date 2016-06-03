"""
Given an absolute path for a file (Unix-style), simplify it.

For example,
path = "/home/", => "/home"
path = "/a/./b/../../c/", => "/c"

Corner Cases:
    Did you consider the case where path = "/../"?
    In this case, you should return "/".
    Another corner case is the path might contain multiple slashes '/' together, such as "/home//foo/".
    In this case, you should ignore redundant slashes and return "/home/foo".

"""


"""
S: 
    1. 简化path. 主要是对../ 的处理
    2. 按照/ 先将path 切分为list.  使用栈, 遇到路径append.  遇到.. pop; .表示当前path 直接pass即可
    3. 在返回path前add '/'
"""
class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        rs = path.split('/')  
        my_stack = []

        for s in rs:
            if s == '' or s =='.':
                pass
            elif s == '..': #pop
                if my_stack:  # not none pop
                    my_stack.pop()
            else: #append
                my_stack.append(s)

        return '/'+'/'.join(my_stack)  # stack ['a','b','c'...]  /join

        


if __name__ == '__main__':
    S =Solution()
    ss = S.simplifyPath("/home/...")
    print(ss)