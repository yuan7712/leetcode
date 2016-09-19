"""
Write a program to solve a Sudoku puzzle by filling the empty cells.

Empty cells are indicated by the character '.'.

You may assume that there will be only one unique solution.
数独 使1-9每个数字在每一行、每一列和每一宫中都只出现一次，所以又称“九宫格”。
"""

"""
S1:
    dfs 递归尝试每一种case
    找到`.` 后尝试1-9, 递归判断. 对每种尝试 要保证合法。 即行列小格 不出现重复, 否则pass

T:
    Q1：
    leetcode 输入中list[i]为str 不能原地修改： 此处使用切片实现修改
             board[i] = board[i][:j] + '.' + board[i][j + 1:]
             在leetcode 中使用如上切片需修改为： board[row] = board[row][:column] + ['.'] + board[row][column + 1:]
    leetcode 中直接提交 board[i]='.' 也可以Pass。。。
    Q2：
    由[i][j]定位所在小单元格： 注意 i: (3*(i//3),3*(i//3)+3) ...

R：
    关于str 处理
    https://discuss.leetcode.com/topic/5299/python-runs-on-my-computer-but-get-typeerror-on-oj-also-i-ll-include-my-java-accepted-recursive-code/3
    https://discuss.leetcode.com/topic/7475/accepted-python-solution 
"""
class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        
        self.dfs(board,0)
        print(board)

    def dfs(self,board,s_i):
        """
        dfs 依次尝试每个小格. 上-下  左-右
        s_i  起始行数 初值0 , 不必判断. 
            此处也可设为dfs(board,s_i,s_j) :  此时循环s_j在下一行要从0开始, 较多判断,所以此处直接设置每行均从0
        """
        for i in range(s_i,9):
            for j in range(9):
                if board[i][j]=='.':   # 尝试1-9
                    for k in ["1","2","3","4","5","6","7","8","9"]:
                        board[i] = board[i][:j] + k + board[i][j + 1:]
                        if self.isValid(board,i,j) and self.dfs(board,i):
                            return True
                        board[i] = board[i][:j] + '.' + board[i][j + 1:]  #还原
                    return False     #尝试1-9 失败  False
        return True

    def isValid(self,board,i,j):            
        """
        判断board[i][j]添加后是否合法. i行j列所在单元格无重复元素. 
        """
        for k in range(9):  #row colum
            if board[i][k] == board[i][j] and k!=j:
                return False
            if board[k][j] == board[i][j] and i!=k:
                return False
        #ii , jj = i//3 , j//3  #i j 所在单元格
        for p in range(3*(i//3),3*(i//3)+3):
            for q in range(3*(j//3),3*(j//3)+3):
                if board[p][q] == board[i][j] and p!=i and q!=j:
                    return False
        return True
                        

if __name__ == '__main__':
    S = Solution()
    ss = S.solveSudoku(["..9748...","7........",".2.1.9...","..7...24.",".64.1.59.",".98...3..","...8.3.2.","........6","...2759.."])
    print(ss)




"""
36. Valid Sudoku   判断是否符合数独

#      ss = S.solveSudoku([[.,.,9,7,4,8,.,.,.],[7,.,.,.,.,.,.,.,.],[.,2,.,1,.,9,.,.,.],[.,.,7,.,.,.,2,4,.],[.,6,4,.,1,.,5,9,.],[.,9,8,.,.,.,3,.,.],[.,.,.,8,.,3,.,2,.],[.,.,.,.,.,.,.,.,6],[.,.,.,2,7,5,9,.,.]])

"""