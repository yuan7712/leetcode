"""
给定n, 能组成1,2,3,..n 唯一数字 组成全排列。 返回第k个

"""
class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        nums = list(range(1,n+1))
        ans = ''

        def f(m):
            c = 1
            for i in range(1,m+1):
                c  *= i
            return c
        k-=1   # 当k正好为(n-1)! 整倍数时 此时 now 就会错误指向下一个，所以k前退1
        tmp = f(n-1)
        while n >0:
            #tmp = f(n-1)
            now  = k // tmp   # n-1!
            ans += str(nums[now])
            k = k -now*tmp
            if n ==1 :
                tmp =1
            else :
                tmp = tmp//(n-1)
            n = n-1 
            nums.remove(nums[now])
            #nums.sort()  del 后依然有序 不必排序

        
        return ans







if __name__ == '__main__':
    S = Solution()
    ss =S.getPermutation(3,1)
    print(ss)




"""
A : 给定12345 找第k个。 

    1.应该从前向后一个个数字进行判断。先确定第一个数字，使用4！比较
    2. 然后将k变小，判断3！ 确定第二个数字...类推


Q： 1. k-=1.   将k前移 为了统一如 12345  确定第一个数字时候 k正好为4！，此时now 应该为0，所以k-1 
    2. k 为0  则按照顺序 一次填入 12345
    3. (n-1)! 计算
    fac = reduce(lambda x, y: x * y, xrange(1, n))  # fac(n-1)



T :    上面每次要判断n==1  此时为最后一个数字，所以可以将while 条件变为n>1
    最后一个数字单独添加。

    ```
    while n > 1:
        pass

    return ans+nums[0]
    ```

"""