"""
Given an array of strings, group anagrams together.

For example, given: ["eat", "tea", "tan", "ate", "nat", "bat"], 
Return:

[
  ["ate", "eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:
1. For the return value, each inner list's elements must follow the lexicographic order.
2. All inputs will be in lower-case.
"""


"""
S: 
    对strs进行分组.
    1. 使用dict. 将不同顺序的str 转变为递增的str key . 存入dict
    2. 遍历dict时，将每个[]中的str sort
"""
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        my_dict = {}

        for s in strs:
            s_key = ''.join(sorted(s))  
            # 改进 1. dic[sortedItem] = dic.get(sortedItem, []) + [item]
            # 2.  d = collections.defaultdict(list)
            if my_dict.get(s_key ,-1) == -1:
                my_dict[s_key] = [s]
            else :
                my_dict[s_key].append(s)
        ans = []
        
        for (k,v) in my_dict.items():  
            v.sort()
            ans.append(v)
        return ans

from collections import defaultdict
class Solution2(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        d = defaultdict(list)
        for s in strs:
            d[''.join(sorted(s))].append(s)
        ans = []
        for (k,v) in d.items():  #
            v.sort()
            ans.append(v)
        return ans 


"""
S3: 
    遍历前 先sort也好..
"""
class Solution3(object):
    def groupAnagrams(self, strs):
        dic = {}
        for item in sorted(strs):
            sortedItem = ''.join(sorted(item))
            dic[sortedItem] = dic.get(sortedItem, []) + [item]
        return dic.values()


if __name__ == '__main__':
    S =Solution4()
    ss = S.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    print(list(ss))