"""
Q :   两个有序数组 a1 a2  找到medain.   复杂度：O (log (m+n)).

"""


# Error
"""
Error : 奇偶数问题，思路与A2 类似，只是奇偶数判断error

"""
class Solution1(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        n1_left , n2_left = 0,0
        n1_right,n2_right = len(nums1)-1 , len(nums2)-1
        n1_mid ,n2_mid = 0,0

        while n1_left < n1_right :
            n1_mid  = (n1_left+n1_right)//2
            n2_mid  = (n2_left+n2_right)//2
            if nums1[n1_mid] == nums2[n2_mid] :
                return nums1[n1_mid]
            elif nums1[n1_mid] < nums2[n2_mid] :
                n1_left = n1_mid+1
                n2_right = n2_mid-1
            else :
                n1_right = n1_mid-1
                n2_left = n2_mid+1

        return (nums1[n1_left]+nums2[n2_left])/2






"""
S2核心思想：

1. 对AB 数组找到合适的ij 将AB 分为左右两半。(左边全部小于右边)
2. 关于奇偶数：不单独考虑，只考虑总和，总和为奇：左边部分max; 总和为偶： 左边max 和右边min 均值。
3. 我们只需移动i 即可。对i 使用二分 移动i。依次缩小i范围。
4. i 应该在较短的一个数组移动，防止j 越界。
5. 移动i时候应该判断 防止越界。
6. 只要改变i+j 和 即可 变为top k 问题


"""



class Solution2 (object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        l_num1 ,l_num2 = len(nums1) , len(nums2)
        # nums1始终指向较短序列，防止划分时 导致另一个 越界
        if l_num1 > l_num2 :
            l_num1,l_num2,nums1,nums2 = l_num2,l_num1,nums2,nums1
        # 在较短的序列上，滑动切分位置。min max  二分选择切分位置。
        s1_min , s1_max = 0,l_num1    # 标记S1_seg 范围，
        s1_seg , s2_seg = 0,0

        while s1_min<=s1_max:
            s1_seg = (s1_min+s1_max)//2  #找S1分割位置。
            s2_seg = (l_num1+l_num2+1)//2 - s1_seg  # 两个分割位置左边数目总共为总数一半(和为偶数)，或者多一个(奇)

            # 首先判断防止越界。 当> 时 表示 s1_seg 应该向左，左右移动max
            if s1_seg>0 and s2_seg<l_num2 and nums1[s1_seg-1] > nums2[s2_seg] :
                s1_max = s1_seg-1
            # s1_seg  应该向左
            elif s2_seg>0 and s1_seg<l_num1 and  nums2[s2_seg-1] > nums1[s1_seg]:
                s1_min = s1_seg+1
            else:
                # 首先找到左边的最大值
                if s1_seg == 0:
                     max_left  = nums2[s2_seg-1]
                elif s2_seg ==0:    #此处必须判断 防止[1][2]  
                    max_left = nums1[s1_seg-1]
                else :
                    max_left = max(nums1[s1_seg-1],nums2[s2_seg-1])
                # 当左侧已经判断完毕， 如果odd 没必要判断右边
                if (l_num1+l_num2)%2 : #odd
                    return max_left
                if s1_seg == l_num1:
                    min_right  = nums2[s2_seg]
                elif s2_seg == l_num2:
                    min_right = nums1[s1_seg]
                else :
                    min_right = min(nums1[s1_seg],nums2[s2_seg])
                return (max_left+min_right)/2.0








"""
S3:
    1.首先获取两个长度 len1  len2
    2. 设置两个游标 p1 p2 
    3. 奇偶数，总数为奇数，找到一个ans 返回， 总数偶数继续找下一个ans2  返回平均

T： 
    1. 判断一个为空串，此时直接返回另一个medain
    2. while  时 防止越界，当一个越界后跳出 while, 继续寻找ans

"""
class Solution3(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums1_len ,nums2_len = len(nums1) , len(nums2)
        #  当其中一个为空串时 ，直接返回medain(判断总数奇偶)
        if nums1_len == 0: 
            if (nums2_len)%2 == 0 :
                return (nums2[nums2_len//2-1]+nums2[nums2_len//2])/2.0
            else :
                return nums2[nums2_len//2]
        if nums2_len == 0: 
            if (nums1_len)%2 == 0 :
                return (nums1[nums1_len//2-1]+nums1[nums1_len//2])/2.0
            else :
                return nums1[nums1_len//2]

        # target 最终找第target 个数字， 如果和为偶数个  则还需找下一个
        target = (nums1_len+nums2_len+1)//2
        i  = 0
        p_1 ,p_2 = 0,0 #num1 num2 的两个游标
        # ans 记录第target 个数字， ans2 记录第target+1 个数字
        ans = 0
        ans2 = 0

        while i < target :
            if nums1[p_1]<=nums2[p_2]:
                ans = nums1[p_1]
                p_1+=1
                i+=1
            else:
                nums1[p_1]>nums2[p_2]
                ans = nums2[p_2]
                p_2+=1
                i+=1
            if p_1 >=nums1_len or p_2>=nums2_len :
                break
        
        # 跳出while 时，已经找到ans, 
        if p_1< nums1_len and p_2 < nums2_len :  # 均未越界
            ans2 = min (nums1[p_1],nums2[p_2])
        # nums1  游标越界，
        elif p_1 >=nums1_len :
            while i < target:
                ans = nums2[p_2]
                p_2+=1 
                i+=1
            ans2 = nums2[p_2]
        else :
            while i < target:
                ans = nums1[p_1]
                p_1+=1 
                i+=1
            ans2 = nums1[p_1]

        if (nums1_len+nums2_len)%2 == 0 :
            return (ans+ans2)/2.0
        else :
            return ans




      



"""
S4 :  也可以将此问题转化为求top k 问题。 对于total为奇数和偶数 分别处理即可。

    top k 的求法可以使用二分 递归求。 为知笔记

Q ： python 如何同C 一样 list 传递部分片段，不使用切片？
"""





if __name__ == '__main__':
    S =Solution2()
    ss =S.findMedianSortedArrays([],[1,2])
    print(ss)
    S3 = Solution3()
    SS3 = S3.findMedianSortedArrays([],[1,2])
    print(SS3)
