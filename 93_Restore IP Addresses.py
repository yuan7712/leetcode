"""
Given a string containing only digits, restore it by returning all possible valid IP address combinations.

For example:
Given "25525511135",

return ["255.255.11.135", "255.255.111.35"]. (Order does not matter)

"""




"""
S1:
    dfs 
    ip < 255 最多三位数 
T:
    1. Error: "010010" ["0.1.0.010","0.1.00.10","0.1.001.0","0.10.0.10","0.10.01.0","0.100.1.0","01.0.0.10","01.0.01.0","01.00.1.0","010.0.1.0"]
            处理特例0 
    2. '.'.join(path)  将字符串list -> str   使用. 分割 
    3. 此处传递path, 也可以值传递则必须pop
        https://discuss.leetcode.com/topic/4742/very-simple-dfs-solution/2

"""
class Solution1(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        ans = []
        self.dfs(s,ans,[],0)
        return ans
    def dfs (self,s,ans,path,start):
        if (4-len(path))*3 < (len(s)-start) :  #减枝, 当剩余串明显多余pass [25525511135] path['2']时直接pass
            return 
        if len(path) == 4 : #此时必然start>=len(s) 
            ans.append('.'.join(path))
            return
        # case len(path)<4 and start<= len(s)  
        i = start
        # val = int(s[start:start+1])  此处start == len(s) error
        while i < len(s) and i < start+3:
            if int(s[start:i+1]) >255 or (i-start >=1 and  s[start]== '0') :
                continue
            else:
                path.append(s[start:i+1])
                self.dfs(s,ans,path,i+1)
                path.pop()
            i +=1
        return

"""
S2: 
    "25525511135"
    ip 只有4段,所以可以 三层for循环. 确定前三个每个的位数即可.

R: 
    https://discuss.leetcode.com/topic/3919/my-code-in-java
    
"""
class Solution(object):
    def restoreIpAddresses(self, s):

        def isValid(ss):
            if int(ss)> 255 or (len(ss)>1 and ss[0]=='0'):
                return False
            return True

        ans = []
        for i  in range(1,4):
            for j in range(1,4):
                for k in range(1,4):
                    if 0< len(s)-i-j-k <=3: 
                        s1,s2,s3,s4 = s[0:i],s[i:i+j],s[i+j:i+j+k],s[i+j+k:]
                        if isValid(s1) and isValid(s2) and isValid(s3) and isValid(s4):
                            ans.append('.'.join([s1,s2,s3,s4]))
        return ans 




"""
dfs  与131 Palindrome Partitioning 类似.
"""
if __name__ == '__main__':
    S =Solution()
    ss = S.restoreIpAddresses("010010")
    print(ss)


