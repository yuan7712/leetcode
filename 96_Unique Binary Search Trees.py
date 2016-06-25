"""
Given n, how many structurally unique BST's (binary search trees) that store values 1...n?

For example,
Given n = 3, there are a total of 5 unique BST's.

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
   
"""




"""
S1:
    递归, 时间长...

    n = 1 :  f(1) = 1
    n = 2 :  f(2) = 2
    n = 3 :  f(3) = 5   f(0)*f(2) + f(1)*f(1) + f(2)*f(0)  依次选取每个为root
    n = 4 :  f(4) = f(0)*f(3) + f(1)*f(2) +f(2)*f(1) + f(3)*f(0)
    ...
"""

class Solution1(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        m_dict = {0:1,1:1}
        def f(m):
            if m <=1:
                return 1
            ans = 0
            i = 0
            while i < m//2:
                ans += 2*f(m-i-1)*f(i)
                i +=1
            if m%2:  #odd
                ans +=f(m-i-1)**2
            return ans

        return f(n)



"""
S2:
    使用dict 缓存f(n) 值

"""
class Solution(object):
    def numTrees(self, n):
        m_dict = {0:1,1:1}
        def f(m):
            if m_dict.get(m,-1) >0 :
                return m_dict[m]
            ans = 0
            i = 0
            while i < m//2:
                ans += 2*f(m-i-1)*f(i)
                i +=1
            if m%2:  #odd
                ans +=f(m-i-1)**2
            m_dict[m] = ans
            return ans

        return f(n)


"""
DP:
    
int numTrees(int n) {
    int dp[n+1];
    dp[0] = dp[1] = 1;
    for (int i=2; i<=n; i++) {
        dp[i] = 0;
        for (int j=1; j<=i; j++) {
            dp[i] += dp[j-1] * dp[i-j];
        }
    }
    return dp[n];
"""