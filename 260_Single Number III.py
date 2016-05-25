"""
Given an array of numbers nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once.

For example:

Given nums = [1, 2, 1, 3, 2, 5], return [3, 5].

Note:
1. The order of the result is not important. So in the above example, [5, 3] is also correct.
2. Your algorithm should run in linear runtime complexity. Could you implement it using only constant space complexity?

"""

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        tmp = 0
        for i in nums:
            tmp ^= i
        print(tmp)
        k = 0   #第一个非0的位数 ,通过while
        while tmp!=0 and tmp%2==0:    #!=0  而不是>0 负数
            tmp = tmp/2
            k+=1
        
        nums_0 = []
        nums_1 = []
        # 将list 按照每个数字第k位为0 1 分为两组
        for j in nums:
            if (j>>k)&1  ==1 :
                nums_1.append(j)
            else :
                nums_0.append(j)
        # 转化为136 中问题，        
        ans_1 = 0
        ans_2 = 0
        for i in nums_1:
            ans_1 ^= i
        for j in nums_0:
            ans_2 ^= j

        ans = [ans_1,ans_2]
        return ans


if __name__ == '__main__':
    S =Solution()
    ss =S.singleNumber([43772400,1674008457,1779561093,744132272,1674008457,448610617,1779561093,124075538,-1034600064,49040018,612881857,390719949,-359290212,-812493625,124732,-1361696369,49040018,-145417756,-812493625,2078552599,1568689850,865876872,865876872,-1471385435,1816352571,1793963758,2078552599,-1034600064,1475115274,-119634980,124732,661111294,-1813882010,1568689850,448610617,1347212898,-1293494866,612881857,661111294,-1361696369,1816352571,-1813882010,-359290212,1475115274,1793963758,1347212898,43772400,-1471385435,124075538,-1293494866,-119634980,390719949])
    print(ss)





"""
A :  此题是136 的变形， 有两个 一次出现的数字，而136 只有一个。

    136 中只有一个单个数字时候， 通过异或就能 简单获取该数字。 但是此时有两个数字，异或后得到的是两个ans 异或值。

 可以从异或的结果考虑， 疑惑后某一位 必定一个为0 一个为1 。
    1. 确定为0  1 的位数。
    2. 将list 按照该位为0 或1 分为两组。[两个ans必定分开，相同的数字必定在一组]
    3. 这样就转化为了 136 中问题


T ： 
    题目进行分组时， 可以使用左右left right 游标 类似快排，将list 原地分为左右。而不用申请list     


"""