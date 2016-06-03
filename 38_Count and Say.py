"""
The count-and-say sequence is the sequence of integers beginning as follows:
1, 11, 21, 1211, 111221, ...

1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
Given an integer n, generate the nth sequence.

Note: The sequence of integers will be represented as a string.

"""


"""
S: 
    模拟执行即可. 对于之前的序列,依次count每个元素出现次数：111 22 1 ->  3个1 2个2 1个1 即 next=> 312211.

T：
    将int 型list ->str;
    ''.join(s) s中元素必须是str; 所以可以使用生成式 先将s 每个元素变为str
"""

class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        def getNext(s):
            """
            :type s : []
            :rtype []
            输入s 返回s的next; 
            """
            i ,num= 0,0
            ans = []
            while i < len(s) :
                now = s[i]
                num = 0
                while i< len(s) and s[i]==now :
                    i+=1
                    num +=1
                ans.append(num)
                ans.append(now)
            return ans


        if not n :   # n ==0
            return ""
        s = [1]
        n -=1       
        while n :
            s= getNext(s)
            n-=1
        ans = "".join(str(i) for i in s)
        return ans



if __name__ == '__main__':
    S = Solution()
    SS = S.countAndSay(6)
    print(SS)

                    

