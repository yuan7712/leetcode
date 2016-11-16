"""
Given an index k, return the kth row of the Pascal's triangle.

For example, given k = 3,
Return [1,3,3,1].

Note:
Could you optimize your algorithm to use only O(k) extra space?

杨辉三角 只要一行

"""



"""
S1:
    [1,2,1]  从后向前,  add 1; 然后每个元素依次和之前sum

"""
class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        ans = [1]*(rowIndex+1)
        for i in range(rowIndex+1):   #row
            for j in range(i-1,0,-1):
                ans[j] = ans[j]+ans[j-1]
        return ans

if __name__ == '__main__':
    S =Solution()
    ss = S.getRow(4)
    print(ss)

