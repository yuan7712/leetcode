"""
Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules.

The Sudoku board could be partially filled, where empty cells are filled with the character '.'.

Note:
A valid Sudoku board (partially filled) is not necessarily solvable. Only the filled cells need to be validated.

"""


class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        flag = [0]*9
        #判断行
        for i in range(9):
            flag = [0]*9
            for j in range(9):
                if board[i][j]!='.':
                    flag[int(board[i][j])-1] += 1 
                    if flag[int(board[i][j])-1]>1:
                        return False
        
        #lie 
        for i in range(9):
            flag = [0]*9
            for j in range(9):
                if board[j][i]!='.':
                    flag[int(board[j][i])-1] +=1 
                    if flag[int(board[j][i])-1]>1:
                        return False

        for i in range(3):
            for j in range(3):
                flag = [0]*9
                for m in range(3):
                    for n in range(3):
                        ii = 3*i+m 
                        jj = 3*j +n
                        if board[ii][jj]!='.':
                            flag[int(board[ii][jj])-1] +=1
                            if flag[int(board[ii][jj])-1]>1:
                                return False


        return True












if __name__ == '__main__':
    
    S =Solution()
    ss =S.isValidSudoku([".87654321","2........","3........","4........","5........","6........","7........","8........","9........"])
    print(ss)




"""
Q: 该题目是判断给定的矩阵是否是 合法的.(这个数独不一定是可解的，只要当前填入的合法即可)
    即判断每行 每列 每个9宫格  中是否包含相同的元素

    对每个九宫格的判断，首先定位到了9个格，然后依次遍历

T： 运行时间长
"""
