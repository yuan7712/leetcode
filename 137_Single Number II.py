"""
Given an array of integers, every element appears three times except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

给定一个包含n个整数的数组，除了一个数出现一次外所有的整数均出现三次，找出这个只出现一次的整数。

"""



"""
S1 : 
    位运算处理， 目标记录bit上1 的个数.(我们将一个个数字，看成是一个个bit处理) 当该bit上1个数为3时循环变为1。用二进制模拟三进制计算
     1.  因为1 的个数有3中状态 0(3) 1 2 ; 所以需要2位才能标记。(如果题目变为5个重复数字则需要3位) 00 10 01 分别表示 0  1 2 个1.(00...选择随意)
     2. 基于以上画一个 真值表
         first  second A[i]   |  ff     ss      (ff ss  表示循环后first second 对应新值)
         0      0       1       1       0
         1      0       1       0       1   
         0      1       1       0       0
         0      0       0       0       0
         1      0       0       1       0
         0      1       0       0       1

    3. 基于以上使用卡诺图生成逻辑表达式： 
        ff = (first^i) & ~second
        ss = (second^i) & ~ff
        注意： 在求ss表达式子时，使用中间3列 和ss即可，因为first 已经改变为ff

T : 
    当题目改变为找出不是5个重复数字的数字时，我们可以自己画真值表生成表达式
    https://leetcode.com/discuss/6632/challenge-me-thx

"""
class Solution1(object):
    def singleNumber(self, nums):
        """
        :

         nums: List[int]
        :rtype: int
        """

        first , second = 0,0 #分别代表第1,2位数

        for i in nums:
            first = (first^i) & ~second
            second = (second^i) & ~first

        return first




"""
S2: 

    同样是位运算，申请一个32 长度的list, 对每个数字将每一位取出，累加到total. (当该位个数==3时置为0) ，然后将此数字表达。

Q： 1. 如上 当所有数字为正数时， java 和python 都没有error; 但是 当出现负数ans 时  python 就会error

        如： [1,1,1,-4] 
        当遍历后 total (%3后)中显示为  [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1](反序)
        此为-4 的补码，在java 中我们依次累加即可， 到最后会溢出，但是最高位仍然当作符号位， 所以最终是-4
        而 python 中，当把这些累加时，python 不会溢出， 超过范围自动变为了大数。 最终返回的是一个正数。 error

T :   所以我们需要 自己判断正负号，当负数时候，自行将-4 补码 变为-4
         补码-> 源码   取反+1  即可。  [1 0 0 0 0 0 0 0 ... 0 0 0 1 0 0 ]
          不管最高位， 记录0 的值， 最终+1  * -1 返回即可

http://liangjiabin.com/blog/2015/03/leetcode-single-number-ii-in-python.html
http://chaoren.is-programmer.com/posts/43222.html


"""
class Solution2(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total  = [0]*32

        for i in nums:
            for j in range(32):
                total[j]+=(i>>j)&1;
        ans = 0
        print(total)
        if total[31]%3 :   #当为负数时候,由于python 不会溢出，所以自行处理， total存放的为补码，将补码->原值。取反+1
            for k in range(31):
                if total[k]%3 == 0 :    #相当于取反
                    ans += 1<<k
            return -(ans+1)   #(取反+1 返回原值)
        else:  #正数
            for k in range(32):
                ans +=(total[k]%3)<<k
            return ans









# 已下为S2 对应的java代码

"""
//https://leetcode.com/problems/single-number-ii/
public class SingleNumber2 {
    
    
    public int singleNumber(int[] nums) {
        
        int [] total = new int[32];   //记录每位上1 的个数
        
        // 对每个数字依次取出每位值，累加到 total
        for (int i =0 ;i < nums.length ; i++)
        {
            for (int j = 0 ; j< 32; j++)
            {
                total[j]+=(nums[i]>>j)&1;
                /*
                 *   或者将1 左移。注意当1<<31 时变为了负数-2147483648，此时& 结果就不会是0 或者1 ，所以此处用！=0 判断。而<< 小于31 时 不是 0 就是1
                 *  if((A[i] & (1 << j)) != 0)  
                    a[j] = (a[j] + 1) % 3;  
                    
                 */
            }
        }
        int ans = 0;
        for (int k = 0 ;k<32 ;k++)
        {   
            System.out.print(total[k]);
            ans += (total[k]%3)<<k;
        }
        
     return ans;
    } 
 
    public static void main(String[] args)  {
        
        SingleNumber2 S = new SingleNumber2();
        int[] is = new int[]{1,1,1,2};
        int ans = S.singleNumber(is);
        System.out.println(ans);    
        
    }
    
}
"""





if __name__ == '__main__':
    S = Solution2()
    ss =S.singleNumber([1,1,1,-4])
    print(ss)        













"""
A : 
   此题要找出个数不是3的数字，而且list是无序的。
   1. 可以考虑创建一个dict, 依次遍历记录数字个数。再次扫描找到个数不是3的。 [o(n)空间,]
   2. 从位运算考虑，将一个个数字看成一位位， 申请32长度数组，依次遍历 记录每位中1 的个数。最后将数组中数字%3，即是要求的。 (但是python 中由于处理大数时不溢出,需自己判断补码转化)
         如 1 1 1 3 3 3 2 
         1(001) 3(011)  对这一组数字，只要将不同位的1 个数sum 即可，1 3 即使不同，但是最终%3 后就会只剩下2 的(010)
         Q : python 中数字处理？？？
    3. 同样是和2 一样的思路，只是更简洁， 标记每位1的个数时候，使用两个数字即可。 00  10 01 表示 0 1 2 个1 ，当有3个1 时候就会自动循环到00.
         此种方法即,数电中使用真值表 用卡诺图写出 逻辑表达式.  S1 即此种方法。
"""    