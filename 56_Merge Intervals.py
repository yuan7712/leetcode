"""
Given a collection of intervals, merge all overlapping intervals.

For example,
Given [1,3],[2,6],[8,10],[15,18],
return [1,6],[8,10],[15,18].

"""

# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


"""
S1: 
    如果[]有序则比较简单, add时 只要看前一个即可.
    1. 利用python list.sort()   对指定关键字排序 L.sort(key=lambda x:(x[1],x[0]))   tuple先比较第一个在比较第二个
    2. for 只要判断ans 最后一个 判断是否合并即可

"""
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if len(intervals) ==0 :
            return []
        intervals.sort(key = lambda x:(x.start,x.end))   #sort 先按照start 再end
        ans = [intervals[0]]
        for i in range(1,len(intervals)):
            if intervals[i].start > ans[-1].end : 
                ans.append(intervals[i])
            else :
                #ans[-1].start = min(ans[-1].start,intervals[i].start) # 可以去掉无用
                ans[-1].end = max(ans[-1].end,intervals[i].end)
        return ans