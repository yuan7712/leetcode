
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        mydic = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        ans ,pre, now = 0,0,0
        for i in s :
            now = mydic[i]
            if now <= pre :
                ans += now
            else :
                ans = ans +now -2*pre
            pre  = now
        return ans


if __name__ == '__main__':
    s = Solution()
    ss = s.romanToInt('CXCIX')
    print(ss)       



"""
Q: 关于罗马数字：
    1. 与进制无关.重复数次：一个罗马数字重复几次，就表示这个数的几倍。
    2. 右加左减，大数右边小数 加，左边小数减。
    3. 此处只是3999以内，只是R->int 所以只需从左到右 或者逆序 遍历。

T: 
    1. 左到右，依次add,当遇到遇到大数时表示 前一位该减去
    2. 右到左，依次sub,(左减)，当遇到大数 add

Q ： int->R  要比此复杂

"""


        