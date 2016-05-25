"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

For example, 
Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.
"""


class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        ans = 0
        left = 0  #左边游标
        right = 0 #确定右侧高度
        now_max = 0 #当left指向最高时有用
        now_sum = 0 # 标记当前循环 trap 水量
        height_len  = len(height)
        #pass 0 高度
        while left <height_len and height[left] == 0 :
            left +=1
        # 当已经末尾 即全部0 return 0
        while left < height_len-1:
            now_sum= 0
            right = left+1
            now_max = right
            # pass比他低的
            while right<height_len and height[right]< height[left] :
                if height[right]>=height[now_max]:
                    now_max = right  #指向右侧max
                now_sum +=height[right]
                right+=1

            if right >= height_len :
                total = 0
                for k in range(left+1,now_max):
                    total+=height[k]
                ans = ans + (now_max-left-1)*height[now_max] - total
                left = now_max

            else : 
                ans = ans + (right-left-1)*height[left] - now_sum
                left = right

        return ans



if __name__ == '__main__':
    S = Solution()
    ss = S.trap( [1,1,1,1,2,3,4,1,2])
    print(ss)





"""
A:   计算总的蓄水量  
   1. 首先排除左边为0 的无效节点。
   2. 一次遍历移动left,  在没一个left处 移动right 确定二者，使之能够蓄水。 包含两种情况： 
        A： 在left 右侧找到 >=  left 处的 点， 这两点之间可以蓄水。(在移动right时顺便记录不能放水sum,now_sum)
        B： left 已经是他之后的max 高度， 所以只需找到 他之后的 sub 高度点即可。 使用now_max 在循环中标记。
   3. ans += 水量后， 移动left 到当前游标即可。


T：  L 25 中 left 只要限制  while left < height_len-1:  最后一个无意义。



A2:   对每个柱子单独判断，判断每个能蓄水多少， 即(min(max_left , max_right)*1 - height)
    1. 从左->右  确定每个柱子左边max
    2. 从右->左 确定右边max
    3. 累加ans

"""



