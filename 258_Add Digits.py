"""
Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

For example:

Given num = 38, the process is like: 3 + 8 = 11, 1 + 1 = 2. Since 2 has only one digit, return it.

Follow up:
Could you do it without any loop/recursion in O(1) runtime?

Hint:

A naive implementation of the above process is trivial. Could you come up with other methods? 

"""



"""
S1:
    普通思路, 依次计算
"""
class Solution1(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        while num >9:
            num = self.calDigit(num)
        return num


    def calDigit(self,num):
        """
        num >9 : 
        return 各个位数之和

        """
        ans = 0
        while num : 
            ans += num%10
            num //=10
        return ans


"""
S2: 
    技巧 digit root problem  求12345 数字之和  一直递归直到<10

    12,345 = 1 × (9,999 + 1) + 2 × (999 + 1) + 3 × (99 + 1) + 4 × (9 + 1) + 5.
    12,345 = (1 × 9,999 + 2 × 999 + 3 × 99 + 4 × 9) + (1 + 2 + 3 + 4 + 5).
    ->  12345 % 9 = (1 + 2 + 3 + 4 +5 ) % 9 = 15%9 = (1+5)%9
    特例： num为9的倍数时,  num%9 =0  实际应该是9
    所以按此一直递归即可    所以num%9就是此题答案
T:
    对于上述特例
        if num == 0 : return 0
            else:return (num - 1) % 9 + 1    # %范围0-8 可以先-1 +1

R： 
    https://discuss.leetcode.com/topic/23279/two-lines-c-code-with-explanation
    https://www.zhihu.com/question/30972581/answer/50203344?from=timeline&isappinstalled=0
"""
class Solution2(object):
    def addDigits(self, num):
        ans = num%9
        return ans if ans or num ==0 else 9   #特例num==0   num%9==0


"""
关于树根Digital root：
    1.  给一个正整数. 将各个位数字求和.依次递归直到变为个位数.   1237->13->4
    2. 求解：  12345 % 9 = (1 + 2 + 3 + 4 +5 ) % 9 = 15%9 = (1+5)%9 
                0    n==0
                9    n!=0&n%9==0
                n%9  oth
    3. 性质
            3.1 S(n) = S^x(n)   #S(n)表示n的树根
            3.2 乘法口诀表  对应的树根也有规律  ->维基百科
            ...
"""

if __name__ == '__main__':
    S = Solution2()
    ss = S.addDigits(43434)
    print(ss)
    S1 = Solution1()
    s1 = S1.addDigits(43434**5)
    print(s1)

