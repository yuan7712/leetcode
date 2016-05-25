class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows ==1:  #防止L12，%是为0. 
            return s
        #l = [[]]*numRows  # 创建2维数组  Error
        l = [[] for i in range(numRows)]  #创建二维数组，此种上面error
        un = numRows *2 -2
        for i in range(len(s)) :
            now = i %un 
            if  now <numRows:
                l[now].append(s[i])
            else :  #>n-1
                l[2*(numRows-1)-now].append(s[i])
        str = ''
        for i in range(len(l)):    #将list-> str
            str += ''.join(l[i])
        return str






class Solution2:
    # @param {string} s
    # @param {integer} numRows
    # @return {string}
    def convert(self, s, numRows):
        if numRows <= 0:
            return None
        if numRows == 1:
            return s
        N = numRows * 2 - 2
        rows = ["" for _ in xrange(numRows)]  #使用一维List更好
        for idx, char in enumerate(s):
            if idx % N < numRows:
                rows[idx % N] += char
            else:
                rows[N - idx % N] += char  #ok
        return "".join(rows)







if __name__ == "__main__":
    s = Solution()
    ss = s.convert("A", 1)
    print(ss)           




"""
Q:
 1. 创建二维数组，使用 L= [[]]*numRows 创建 修改L[0] 后L[1]...也会改变。[[]]*3表示3个指向这个空列表元素的引用,修改任何一个元素都会改变整个列表
 2. list -> str 使用join函数
 3. 防止 %0 error 所以单独判断 1 

T ：1. now<numRows的都可以合并。。。
    2. L 使用一维更好。不必二维。。 


"""    