class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        if not str :
            return 0
        i ,flag,ans = 0,1,0
        Max = 2**31-1
        while i<len(str) and str[i]==' ':  #去空格
            i +=1
        if i >=len(str):
            return 0
        if str[i] == '-':  #负数
        	flag = -1
        	i +=1
        elif str[i] == '+':
        	i +=1
        while i<len(str) and str[i]>='0' and str[i]<='9':
            now = ord(str[i]) - ord('0')
#            if ans>Max//10 and flag ==1:
#                return Max
#            elif ans>Max//10 and flag ==-1:
#            	return (Max+1)*-1
#            elif ans == Max//10 and flag ==1 and now>Max%10:  #正数2147483647
#                return Max
#            elif ans == Max//10 and flag ==-1 and now>Max%10+1:  #负数2147483648
#                return (Max+1)*-1
            ans = ans*10 + now
            i +=1
        return max(min(ans * flag, 2147483647), -2147483648)  #利用python处理大数不溢出











if __name__ == "__main__":
    s = Solution()
    ss = s.myAtoi("      11919730356x")
    print(ss)                   



"""
Q: 1. 首先清除前缀空格。
   2. 判断+ - 号。
   3. 越界, -2147483648 -> +2147483647
T:  越界可以使用多重if 判断。 python支持大数操作，也可以直接与2147483648 比较。   
"""    