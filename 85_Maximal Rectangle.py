"""
Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

For example, given the following matrix:

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0
Return 6.

最大矩形

"""



"""
S1： DP -- 未完

1. 划分子问题 找到最优子结构;  2. 重叠子问题; 

   求解最大的矩形面积;  两个点定矩形;   对于每个点(i,j) 找其匹配的左上角点 (ii,jj);   创建二维矩阵存储各个点对应的左上角左边; 最大面积最后可以遍历矩阵o(n) 求得；

   问题： 如何求解该cache矩阵；

   f(i,j) :  与f(i-1,j) f(i,j-1) 有关;  f(i-1,j)判断i此行是否满足;  f(i,j-1)判断j列;     //子问题划分！

   迭代顺序：

   从左上角开始 

   1 1 1 1 1 1 1
   1 2 2 2 2 2 2
   1 2 3 3 3 3 3
   1 2 3 4 4 4 4
   1 2 3 4 5 5 5
   1 2 3 4 5 6 6

   首先确定 1(第一批) 然后第二批... 迭代过程中可以顺便记录最大面积


A: 
    细节： 
    1. 由于[i,j]为右下角确定的矩形可能不止一个, 所以状态矩阵在存储时必须存储多个Node;
    2. (i,j)位置判断左或上方Node 形成更大矩形时,每次都需要计算向上或左最多行几步；
       所以可以创建单独的二维矩阵记录 该位置向左或上最多走的步数；

    复杂度： 
    for i in range n : 
        for j in range (m): 向下
            //计算该点最优面积
            [i-1][j]  和 [i][j-1] 
            其中都可以存了多个左上角顶点, 对于每个矩形还必须  使用cache数组 o(1)判断是否能组成新的数组;

        for k in range (n) : 向右
            同上



太复杂。。。 未完




"""
class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """

        if not matrix:
            return -1
        m = len(matrix)  
        n = len(matrix[0])
        
        stat = [[(-1,-1)]*n for i in range(m)]
        
        for i in range(m):
            if matrix[i][0] == 1 :
                stat[i][0] = (i,0)
        for i in range(n):
            if matrix[0][i] == 1:
                stat[0][i] = (0,i)

        for i in range(1,m):   # i,i
            for j in range(i,m):   # 列
                if matrix[i][j] == 1 :
                    pass



    def isValid(self,matrix,stat,x,y):

        """
        判断矩阵(x,y)  位置和(x-1,y)  (x,y-1) 是否可以合并成更大矩形；

        保证不会越界

        """

        (x1,y1) = stat[x][y-1]  #left
        s1 = 0

        # 判断j列 是否有 j-jj 个1
        if x1 != -1:
            for i in range(x - x1 +1):
                if matrix[x-i][y] != 1:
                    break  #area
            s1 = (x-x1+1)*(y-y1+1)


        
        

        else :   # 判断i行 上
            (x2,y2) = stat[x-1][y]  #up
            s2 = 0
            for  i in range(y-x2+1):
                if matrix[x][y-i]!= 1:
                    break
            s2 = (x-x2+1)*(y-y2+1)



"""
S2:         时间 o(n^2)  空间o(n) 
    

重新分析问题：   矩形面积除了使用两个顶点确定外，还可以使用两条边来确定; S1中基于顶点确定矩形会出现(i,j)对应于多个顶点问题，较复杂；

暴力思路：    给定n长数组 那么n(n+1)/2 种底边.  给定m*n 矩阵，我们依次分析以每行中若干 矩阵元素作为底边的case; 
              例如矩阵第一行 [1,1,1,0,0,1,1]  我们可以记录(i,j) 作为底边能构成的最大面积(或者记录高度)
              计算下一行时：  该行(i,j)  会使用到上一行(i,j) 记录最大面积的信息;

              * 利用底边确定矩形，和顶点确定相比，不会出现重复case; 即一个底边只要记录最大高度即可;
              * 复杂度： 
                        首先需要二维数组，记录(i,j) 作为底边的最大高度。
                        for i in rows: 
                            for j in n^2 种底边(i,j):
                                更新(i,j) 记录的最大高度

                        起码o(n^3)


转换思路84：    
                给定一个数组[1,2,3,0,2,3]计算 最大的矩形 即84中问题， 使用o(n)可以解决；

                所以给定二维数组，我们对于每行只要记录该位置能达到的最大高度，然后将此问题转换为 84 解决；

                如第一行  1 1 1 0 0 1 
                第二行：  1 1 0 1 1 0  -> 2 2 0 1 1 0   (只要本行元素为0 那么之前高度清零)

                * 复杂度： 
                        for  i  in rows: 
                            for i in n :  // 更新高度

                            o(n)  计算该层作为底边最大面积

                        时间复杂度 o(n^2)  空间o(n) 使用栈



关于84中问题给定柱状图计算最大矩形面积：

                o(n)计算即使栈;




R: http://blog.csdn.net/u013291394/article/details/50865281


"""
class Solution2(object):
    def maximalRectangle(self, matrix):

        if not matrix : 
            return 0

        
        m  = len(matrix)  #row
        n = len(matrix[0]) #colum   m*n
        height = [0]* (n+1)
        ans = 0


        for i in range(m):   # rows

            # update height
            for j in range(n):
                height[j] =  height[j]+1 if matrix[i][j] == '1' else 0

            # cal area base this row 
            #  栈中记录该高度 柱子的最右侧索引;
            my_stack = [-1]  #stack  使用锚点防止栈空, 栈中存放索引,height[-1] = 0 

            for i in range(n+1):  # 0...n-1

                while   my_stack  and  height[i] < height[my_stack[-1]] :   # pop  cal area
                    h = height[my_stack.pop()]  #高度
                    ans = max( (i - my_stack[-1] -1)*h ,ans)

                my_stack.append(i)
        print(ans)
        return ans


    def maximalRectangle2(self, matrix):
        """
        计算柱状图最大矩形面积 稍修改;

        栈中存放(height,num) : (3,4) 表示高度为3的柱子有4个;  栈中高度都是递增的; 注意最后要使用一个高度为0柱子 清空栈;

        栈： (1,1) (3,1) (5,1) 
             此时 判断高度为2 柱子;  2<5 所以(5,1) (3,1)出栈, 出栈同时计算该柱子能达到的最大面积.
             pop(5,1) : area = 5*1
             pop(3,1) : area = 3*(1+1)    高度为5的num+高度3num

             push(2,3) : 相当于把3 5 都视为高度为2的柱子入栈;  即削掉高的部分;

        """
        if not matrix : 
            return 0
        
        m  = len(matrix)  #row
        n = len(matrix[0]) #colum   m*n
        height = [0]* (n+1)
        ans = 0


        for i in range(m):   # rows
            # update height
            for j in range(n):
                height[j] =  height[j]+1 if matrix[i][j] == '1' else 0

            # cal area base this row 
            #  栈中记录该高度 柱子的最右侧索引;
            my_stack = []  #stack  (height,num)

            for i in range(n+1):  # 0...n-1
                if not my_stack or height[i] >= my_stack[-1][0]: 
                    my_stack.append((height[i],1))
                    continue

                # pop
                num = 0
                while my_stack and height[i] < my_stack[-1][0]: #pop
                    tmp = my_stack.pop()
                    num += tmp[1]
                    ans = max(ans,num*tmp[0])
                my_stack.append((height[i],num+1))
        print(ans)
        return ans 



"""
S3 : leetcode DP    时间o(n^2)  空间o(n)

    还是DP, 问题划分的很好！！！ 不易理解;

    问题分解：  
            1. 如何确定一个矩形面积？
                S1中使用对角顶点，造成case过多;
                S2中使用确定 底边*height; (转换为求解柱状图最大面积问题)
                S3和S2类似,  对于点(i,j) 通过左边界left, 右边界right 确定底边长度; 再使用height确定该位置的最大高度; 进而求得area;

            2. s(i,j) = [ right(i,j) - left(i,j) ]  * hright(i,j)

            3. left right height 如何计算 ？
                这三者分别表示(i,j)位置能达到的最左(右，上)边界; 
                1 2 3 4 5
                0 6 7 0 0    (非0用方便表示位置)
                    6号位： left :自己  right:7 高度：2 
                    必须保证这三个元素确定的矩形，是合法矩形，即内部都是  1

                假设第一行 (i,j) 都已经计算出 left right height 
                计算第二行： (i+1,j)  上一行的(i,j)已经确定了 (i,j)的矩形;  那么计算2(i+1,j)完全可以利用1(i,j)信息;
                            我们只要判断1(i,j)中确定的矩形是否再向下扩展一行即可;
                            2(i+1,j) 中确定的矩形 **只会比1(i,j)中确定的(左右)边界更小, 确保3点确定的矩形合法**

                0 0 1 1 1 0 0
                0 0 1 2 1 0 0
                1 1 1 3 1 1 1

                        如图2号： 确定left right height (2,4,2)  (索引，索引 ，高度)
                        计算3号位：虽然其左边界为0 右边界为6; 但是(0,6,3) 并不能保证该矩形合法; 反之利用2号位信息就可以确保 (2,4,3)是该位置能到达最大高度锁获取的矩形;
            4. 公式： 
                        left(i,j) = max(left(i-1,j), cur_left), cur_left can be determined from the current row
                        right(i,j) = min(right(i-1,j), cur_right), cur_right can be determined from the current row
                        height(i,j) = height(i-1,j) + 1, if matrix[i][j]=='1';  height(i,j) = 0, if matrix[i][j]=='0'

            5. 一定能找到最优解？
                        Q1： 3中的矩形，当计算3号位时，确定的该矩形不一定是包含3的最优矩形
                            A1： 的确, 假设3号位此行无线长都为1, 那么即使包含3高度为1 也肯定比 (2,4,3)确定的优;
                        Q2： 如何保证最优？
                            A2： (i,j)位置 确定的矩形不一定是包含该位置的最优矩形, 但是肯定是**该高度下的最优矩形**
                                 即类似于(i,j)计算其最大高度h,然后尽最大可能左右扩展得到矩形;
                                 但是对于任意全局最优解, 该矩形中**必然有个元素 符合使用left right height 确定** (反证法)

                                 所以即便(i,j)确定的不是包含该位置最优也无妨,最终必然有某个(i,j)符合;

    代码:     
            1. 只要创建3个一维矩阵,分别存储left right height;  依次计算每行的值, (i,j)只使用(i-1,j)所以一维矩阵即可;
            2. 3个过程 并不冲突， 独立计算
            3. 中途计算最大面积即可;

    复杂度： o(n^2)  空间o(n)


* R: 
    https://discuss.leetcode.com/topic/6650/share-my-dp-solution

class Solution {public:
int maximalRectangle(vector<vector<char> > &matrix) {
    if(matrix.empty()) return 0;
    const int m = matrix.size();
    const int n = matrix[0].size();
    int left[n], right[n], height[n];
    fill_n(left,n,0); fill_n(right,n,n); fill_n(height,n,0);
    int maxA = 0;
    for(int i=0; i<m; i++) {
        int cur_left=0, cur_right=n; 
        for(int j=0; j<n; j++) { // compute height (can do this from either side)
            if(matrix[i][j]=='1') height[j]++; 
            else height[j]=0;
        }
        for(int j=0; j<n; j++) { // compute left (from left to right)
            if(matrix[i][j]=='1') left[j]=max(left[j],cur_left);
            else {left[j]=0; cur_left=j+1;}
        }
        // compute right (from right to left)
        for(int j=n-1; j>=0; j--) {
            if(matrix[i][j]=='1') right[j]=min(right[j],cur_right);
            else {right[j]=n; cur_right=j;}    
        }
        // compute the area of rectangle (can do this from either side)
        for(int j=0; j<n; j++)
            maxA = max(maxA,(right[j]-left[j])*height[j]);
    }
    return maxA;
}
};
"""











"""

S: 

 推荐使用S2中方法2.  比较好控制;

 S3 较复杂..


"""




if __name__ == '__main__':
    s = Solution2()
    s.maximalRectangle2(["10100"])