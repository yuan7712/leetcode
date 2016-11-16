"""
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.

Example 1:
Given intervals [1,3],[6,9], insert and merge [2,5] in as [1,5],[6,9].

Example 2:
Given [1,2],[3,5],[6,7],[8,10],[12,16], insert and merge [4,9] in as [1,2],[3,10],[12,16].

This is because the new interval [4,9] overlaps with [3,5],[6,7],[8,10].

"""

#Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


"""
S1:
    [[1,3],[6,9]]    [2,4]
    1. 首先loc确定要插入data始末位置.  loc函数确定. 在intervals内部则为奇数, 如2;在间隔外偶数 如 0 4 ..
    2. loc_s loc_e  分别是始末insert位置.
       按照是否奇偶数分为4种case 分别插入

T： 
    过于繁琐
"""
class Solution1(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        loc_s = self.loc(intervals,newInterval.start)
        loc_e = self.loc(intervals,newInterval.end)
#        if loc_s%2 == 0: 
#            # new = [newInterval[0],9]
#            if loc_e %2 ==0:
#                #new[1] = newInterval[1]
#                return intervals[0:loc_s//2]+[newInterval]+intervals[loc_e//2:]
#            else : 
#                #new[1] = intervals[loc_e//2][1]
#                newInterval.end = intervals[loc_e//2].end
#                return intervals[0:loc_s//2]+[newInterval]+intervals[loc_e//2+1:]
#
#        if loc_s%2 !=0 :
#            #intervals[loc_s//2]
#            newInterval.start = intervals[loc_s//2].start
#            if loc_e %2 ==0:
#                #intervals[loc_s//2][1] = newInterval[1] 
#                return intervals[0:loc_s//2]+[newInterval]+intervals[loc_e//2:]
#            else : 
#                #intervals[loc_s//2][1] = intervals[loc_e//2][1]
#                newInterval.end = intervals[loc_e//2].end
#                return intervals[0:loc_s//2]+[newInterval]+intervals[loc_e//2+1:]

        if loc_s%2!=0:
            newInterval.start = intervals[loc_s//2].start
        if loc_e %2 == 0:
            return intervals[0:loc_s//2]+[newInterval]+intervals[loc_e//2:]
        else :
            newInterval.end = intervals[loc_e//2].end
            return intervals[0:loc_s//2]+[newInterval]+intervals[loc_e//2+1:]

    def loc(self,intervals,key):
        """
        intervals: [1,2],[6,7]
        key: 3 确定3位置. 如果在intervals内部奇数,其余位置偶数.  此处3insert位置为3
        """
        ans = 0
        for i in intervals:
            if key < i.start:  #over
                break
            if key >= i.start:
                ans +=1
            if key > i.end:
                ans +=1
        return ans


"""
S2:
    1. 从左到右遍历 首先把能确定[]加入到result
    2. 继续 从此位置向右添加添加右边界能确定的[]
    3. left right  记录左右分别add 个数
         left +right < 总个数时 ： 中间则存在若干[] 取min  max 左右边界
         = 总个数   中间无[]  直接add 

    
T: 
    1. 注意result中保持有序
"""
class Solution(object):
    def insert(self, intervals, newInterval):
        result = []
        l_i = len(intervals)  
        left, right = 0,0   # left  rihgt  add num
        for i in range(l_i):  #left开始[]
            if intervals[i].end < newInterval.start: 
                result.append(intervals[i])
                left +=1
        for i in range(left,l_i):
            if intervals[i].start > newInterval.end: 
                result.append(intervals[i])
                right +=1

        if right +left <l_i:
            newInterval.start = min(newInterval.start,intervals[left].start)
            newInterval.end = max(newInterval.end,intervals[l_i-1right].end)
        return result[0:left]+[newInterval]+result[left+1:]

"""
S3:
    leetcode py  ==S2
    https://discuss.leetcode.com/topic/16988/7-lines-3-easy-solutions

"""
def insert(self, intervals, newInterval):
    s, e = newInterval.start, newInterval.end
    left = [i for i in intervals if i.end < s]
    right = [i for i in intervals if i.start > e]
    if left + right != intervals:
        s = min(s, intervals[len(left)].start)
        e = max(e, intervals[~len(right)].end)   # ~5 =-6
    return left + [Interval(s, e)] + right


if __name__ == '__main__':
    S = Solution()

    ss = S.insert([[1,3],[6,9]],[2,7])
    print(ss)
