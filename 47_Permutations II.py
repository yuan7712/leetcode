"""
Given a collection of numbers that might contain duplicates, return all possible unique permutations.

For example,
[1,1,2] have the following unique permutations:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]

"""

"""
S1:
    迭代  --未完成
    --对46-S3修改
    46中[1,2,3]每次确定一个数字的位置, 上层[[1,2],[2,1]] 此层3分别插入不同位置.
    [1,1,1,2,2,3,3] 
    1. 在此将相同数字划分为一组.[(1,1,1),(2,2),(3,3)]
        []
        [1,1,1]   -- add 1 到[]中, 只有一
种        [...] 10种可能,  add[2,2] 到[1,1,1];  即如何将[2,2]放到4个空格处
                        a + b + c + d = 2  => 共有10种
        [...] --add [3,3]

Q: 
    1. 在将[2,2] add 到[1,1,1]的4个位置时, 未找到合适方法.

"""
class Solution1(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        return None
 


"""
S2: 
    递归  AC
    类似46-S2
    46-S2 中是无重复数字[1,2,3] 每次swap 即可.
    47 中包含重复数字,我们只要把重复情况去除即可.
        S[1,1,1,2,2,3,3] 
            46中我们每次确定一个元素,确定S[0]后以1  开始的序列会全部求出.
         然后分别swap(S[0],S[i]) ,但是此处有重复，所以直接pass 1,1,1 直接swap(1,2)即可
         如果swap(1,1),剩余的顺序改变但是仍然与 不swap 有相同子序列  
T: 
    [0,0,0,1,9]                其实只要保证swap的两个数字不同就能保证不重复  //add 2017/3/1
    此处swap 时只要保证,在该子序列中  nums[start]和同一个数字只swap 一次.
    不能简单记录last swap值+ while 跳过.  swap 后子序列不一定増序
    [0,0,0,1,9]  swap(0,9) -> [9,0,0,1,0]  此时子序列[0,0,1,0] 只记last 可能error   

R:
    http://www.cnblogs.com/TenosDoIt/p/3662644.html
    http://www.jiuzhang.com/solutions/permutations-ii/           // add  2017.3.1   即自己需要创建一个path路径，这样就不会带来由于swap而造成重复
         第二种 每次不再swap,而是使用切片将nums 分为两部分  已经确定的+剩余序列 
         [0,0,0,1,9] -> [0,9] +[0,0,1]   [0,9] 是已经确定的 [0,0,1] 剩余序列 

        def _permute(result, temp, nums):
            if nums == []:
                result += [temp]
            else:
                for i in range(len(nums)):
                    if i > 0 and nums[i] == nums[i-1]:    #此处序列肯定有序, 
                        continue
                    _permute(result, temp + [nums[i]], nums[:i] + nums[i+1:])

"""

# 此方法陷入  等待的序列必须是有序的 例如 [0,0,0,1,9] 交换 0 9 后 无序但并不影响；
class Solution2(object):
    def permuteUnique(self, nums):
        ans = []
        start = 0
        nums.sort()
        self.pers(nums,start,ans)
        return ans


    def pers(self,nums,start,ans):
        """
        nums: 原数组
        start:  求子序列 起始位置
        ans: 全局结果
        """
        if start == len(nums):
            ans.append(nums[:])
            return
        mdict = []  #nums[start]  swap 的数字放到list中, 保证不swap 重复值
        for i in range(start,len(nums)):
            if nums[i] in mdict:  #防重复      利用map解决swap时出现的重复问题
                continue
            nums[start],nums[i] = nums[i], nums[start]    # add 2017.3.1 其实只要交换的二者不相同即可？？即S3
            self.pers(nums,start+1,ans)  #确定nums[start],继续判断下一位 start+1
            nums[start] , nums[i] = nums[i], nums[start]  # 还原
            mdict.append(nums[i])
        return 




"""
S3
    --leetcode   **** best
    该方法传递nums时,i等价于之前的start, 只要swap 一次即可,因为值传递修改也无效.
    [0,0,0,1,9] 
    i=1时： 0分别与 0 1 9 swap
        [0,0,0,1,9]   [0,1,0,0,9]  [0,9,0,0,1]  它能保证i=2之后的子序列有序, 传递值继续递归.   # error  解释错误； 本质是只要不太就能交换

R: 
    https://discuss.leetcode.com/topic/8831/a-simple-c-solution-in-only-20-lines

class Solution {
        public:
    void recursion(vector<int> num, int i, int j, vector<vector<int> > &res) {
        if (i == j-1) {
            res.push_back(num);
            return;
        }
        for (int k = i; k < j; k++) {
            if (i != k && num[i] == num[k]) continue;     # 不是传递值的问题 而是只要  num[i] ！= num[k]  那么交换就有意义，交换的含义是确定当前位置 然后递归其余位置，，如果相同则无意义
            swap(num[i], num[k]);
            recursion(num, i+1, j, res);
        }
    }
    vector<vector<int> > permuteUnique(vector<int> &num) {
        sort(num.begin(), num.end());
        vector<vector<int> >res;
        recursion(num, 0, num.size(), res);
        return res;
    }
};

"""


"""
S4 
    非递归
    改进 31  next-permutation
    [0,0,0,1,9] 
    循环执行 next-permutation.  依次找到next [0,0,0,9,1] 直到[9,1,0,0,0]

R:
    https://discuss.leetcode.com/topic/3194/a-non-recursive-c-implementation-with-o-1-space-cost
"""
class Solution(object):
    def permuteUnique(self, nums):


        nums.sort()
        ans = []
        nums_len = len(nums)
        if not nums_len :
            return []
        ans.append(nums[:])  # min  value

        while True:   #每次循环调用next-permutation  
            i = nums_len -1
            while i >= 1 and nums[i] <=nums[i-1]:
                i -=1
            if i == 0 :  # 此时已经递减  max value. 
                return  ans
            j = 0
            for k in range(len(nums)-1,i-1,-1):  #从nums[i:]找比nums[i]大的最小值
                if nums[k] > nums[i-1]:
                    j = k
                    break

            nums[i-1],nums[j] = nums[j],nums[i-1]
            # 将nums[i:]  排序 reverse 即可
            b , e = i , len(nums)-1
            while b<e:
                nums[b],nums[e] = nums[e],nums[b]
                b+=1
                e-=1
            ans.append(nums[:])   #append
        return  ans     



"""

思路
1. 使用swap  每次交换两个Node, 但是只要二者值相同就不再交换没意义。

2. 记录path, 依然是dfs每次确定一个位置，保证原有的 nums 是有序的， 而且中途不再修改此顺序。
             path 每次dfs时添加一个Node, aaab       确定第一个位置时值能 ab 两种
3. S4
"""

        


if __name__ == '__main__':
    S = Solution()
    ss = S.permuteUnique([1,2,2])
    print(ss)
    