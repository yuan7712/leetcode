class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        ans = 0 
        left ,right = 0,len(height)-1
        while left <right :
            hi = min(height[left],height[right]) #height
            ans  = max(ans,hi*(right-left))
            if height[left]<height[right] : #left向右找到比之前高的
                now = left
                while left< right and height[left]<=height[now] :
                    left += 1
            else :
                now = right
                while left <right and height[right]<=height[now] :
                    right -= 1
        return ans



class Solution2:
    # @param {integer[]} height
    # @return {integer}
    def maxArea(self, height):
        left = 0
        right = len(height) - 1
        max_area = 0
        while left < right:
            max_area = max(max_area, min(height[left], height[right]) * (right - left))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area


if __name__ == "__main__":
    s = Solution()
    ss = s.maxArea([1,3,9,6,7,8,7,5,2])
    print(ss)        




"""
Q :  计算最大蓄水量,主要是由于两边低板决定的。 所以从两边向内缩。
当left 高度低于right时 left 应该向右找到比之前更高的板(包括相等，相等的板area肯定比之前小)， 同理右侧向内




"""