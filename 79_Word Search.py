"""
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

For example,
Given board =

[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
word = "ABCCED", -> returns true,
word = "SEE", -> returns true,
word = "ABCB", -> returns false.

"""



"""
S1:
    dfs
    "ABCB" 判断此串,首先在board 中找到A的位置 总共两个. 分别dfs 判断
    dfs依次匹配每个字母,该字母匹配后,分别从上下左右 四个方向 dfs


T:
    1. 注意越界处理
    2. 外层调用dfs时, 遍历首先找到第一个字母匹配的位置, 
    3. case : ["b","a","b"] ,"bbabab"
    4. 处理防止重复: 可以不记录path  将字母变为非法字符如 '*';  dfs 后再继续变回.
        https://discuss.leetcode.com/topic/22788/python-dfs-solution-with-comments/6
"""
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
         
        def dfs(path,s_w,s_i,s_j):
            """
            path : 记录当前路径中字母位置[(0,0) ,(0,1)...] 防止重复元素
            s_w : word 开始匹配的字母位置. s_w >= len(word) 则全部匹配完毕
            s_i,s_j : 起始匹配board 字母位置. s_i 行 s_j列
            匹配到 return True
            """
            if s_w >= len(word):
                return True 
            if s_i<0 or s_j<0 or s_j >= len(board[0])  or s_i>=len(board): # 处理越界 return False
                return False
            if board[s_i][s_j]!=word[s_w]  or (s_i,s_j) in path:  #处理重复元素
                return False
            # path add
            path.append((s_i,s_j)) # 上下左右 只要一个方向匹配 return  True
            if dfs(path,s_w+1,s_i,s_j+1) or dfs(path,s_w+1,s_i,s_j-1) or dfs(path,s_w+1,s_i-1,s_j) or dfs(path,s_w+1,s_i+1,s_j):
                return True
            path.pop()
            return False
        
        # 开始时找到首字母匹配位置 dfs . 未判断word 空串
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0] and dfs([],0,i,j) : 
                    return True
        return False
 



if __name__ == '__main__':
    S =Solution()
    ss = S.exist(["b","a","c"],"cab")
    print(ss)

"""
使用相邻字母组成单词.相邻： 上下左右.  即一笔将这些连起来. 如ABSF false ABFS true
 一个字母只能使用一次  ABBA false
             self.dfs(board,path,word,s_w+1,s_i,s_j+1)  #right
            self.dfs(board,path,word,s_w+1,s_i,s_j-1)  #left
            self.dfs(board,path,word,s_w+1,s_i-1,s_j) #up
            self.dfs(board,path,word,s_w+1,s_i+1,s_j) #down
"""