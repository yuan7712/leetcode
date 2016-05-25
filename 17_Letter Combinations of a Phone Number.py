class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        my_dict = { '1':['*'],'2':['a','b','c'],'3':['d','e','f'],'4':['g','h','i'],'5':['j','k','l']
                    ,'6':['m','n','o'],'7':['p','q','r','s'],'8':['t','u','v'],'9':['w','x','y','z']} 
        ans  = []
        if not digits :
            return []
        if len(digits)==1:
            return my_dict[digits]
        else :
            now = my_dict[digits[0]]  #第一个list
            next = self.letterCombinations(digits[1:])
            for i in range(len(now)):
                for j in range(len(next)):
                    ans.append(now[i]+next[j])

        return ans






class Solution2(object):
    def letterCombinations(self, digits):
        if not digits:
            return []

        map_ = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }
        queue = [""]  #初始长度为1，将第一个数字对应的字母和"" 组合

        for digit in digits:
            size = len(queue)
            for _ in range(size):
                cur = queue.pop(0)
                for letter in map_[digit]:  #对之前ans，每个pop 再次组合
                    queue.append(cur + letter)
        return queue



if __name__ == '__main__':
    s = Solution()
    ss = s.letterCombinations('23')
    print(ss)



"""
S1:  使用递归，'123'->'1' 和'23' 匹配。使用list 存放组合。
S2 :  使用非递归，'123'依次向后遍历，维护ans队列，每次pop然后组合生成新的队列
"""
