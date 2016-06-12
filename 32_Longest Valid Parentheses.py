"""
Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

For "(()", the longest valid parentheses substring is "()", which has length = 2.

Another example is ")()())", where the longest valid parentheses substring is "()()", which has length = 4.

"""


"""
S1: 
    此题要求串S中最长的合法的括号匹配。  o(n)

    1. 首先，S 中不同长度的匹配可以会受到( 和) 间隔开。
        case1 : ) :   ()) (()))   如此) 分割成两个不同长度的匹配
        case2 :( :    ( (()) (( (()())   ( 分割成若干个子匹配。
        case3: (和)： () ) (()) ) (( (())    他们将S分开。但是)分割肯定在(分割之前， 因为)必然能和(匹配，即)不缺失配，除非该串全部为)分割，如1中
    2. 所以我们可以先将(入栈，并且遇到)时候出栈， 记录匹配的个数。当)不能匹配时记录ans取max
        当我们遍历完后如果栈空，说明此时为case2,即肯定没有出现( 分割，所以直接返回max即可。
    3. 当栈非空时:
        因为此时我们的now标记的只是最后一次最长的匹配()个数，但是由于此不是合法匹配，所以必须拆解。
        如 case2 :  now = 5  我们记录了5个括号，但是由于(分割，我们必须判断每个字串长度，
                    我们可以使用栈中(的下标很简单的确定每个长度。所以我们将栈中保存成(的下标。
            case2:  栈中： 0 5 6  -> 每个长度 4 0 6 取Max即可。
    4. 但是case2 有一种特殊情况 ((()))  (() ((())
        此时我们使用栈中(下标只能找到后两组长度，但是第一组呢，我们可以使用遍历时候记录的最后一次匹配的长度now 计算出 第一个长度。



"""
class Solution1(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        my_stack = []
        s_l = len(s)
        ans = 0  #ans记录max()个数
        now = 0
        # 将( 下标入栈，)出栈匹配 now记录当前匹配的()个数
        for i in range(len(s)):
            if s[i] == '(':
                my_stack.append(i)
            else:
                if len(my_stack) ==0:
                    ans = max(ans,now)
                    now = 0
                else:
                    now +=1
                    my_stack.pop()
        # 栈空，此时必然不会出现)分割情况， 所以直接返max即可。
        if not my_stack :
            ans = max(ans,now)
            return ans *2
        # 被(分割，遍历完之前谁也不知道now记录的()是不是在一个合法匹配内，此时说明出现error; 所以我们使用栈中(下标计算每个小段长度
        else :
            my_stack_l = len(my_stack)
            print(my_stack)
            #last 主要是防止 ((()))  (() ((()) 最前面这样的串不能记录长度，所以使用now计算。
            last = 2*now - (s_l -my_stack[0]-my_stack_l)

            my_max = [ans*2,last]
            for i in range(len(my_stack)-1):
                my_max.append(my_stack[i+1]-my_stack[i]-1)

            my_max.append(s_l-1-my_stack[-1])
            print(my_max)
            ans = max(my_max)
            return ans 







"""
S2: 
    leetcode 方法，一次遍历，和S1方法基本一致，不过简化很多。

    1. 为了分别(间隔的序列，同样栈中存放(的下标
    2. 同样不同的串会被(或) 分割。
    case1 ) :  我们只要记录上次失配)的位置，并且如果当前)成功匹配后，
        如果栈空，表示此时匹配到 合法的()
    case2 (: 
        当匹配后栈非空时，表示栈中依然(未得到匹配，我们只需用栈顶的( 下标即可确定当前已经匹配长度。

    3. 和S1相比，求序列长度时依次递增
        ) ()() ) ()()()  : 如此当每个括号匹配时，我们就记录当前已知匹配的最大长度，使用栈顶的(下标也能分割属于不同块的长度
        ())()()  :  同样此种也是每次匹配后更新已经匹配的长度

"""

class Solution2(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s :
            return 0
        my_stack = []
        s_l = len(s)
        ans = 0
        last = -1  #标记最后一个失配)的位置

        for i in range(s_l):
            if s[i] == '(':
                my_stack.append(i)
            else : # )
                if len(my_stack) == 0 :  #)失配
                    last = i
                else: #存在(能匹配； 只要匹配就计算当前已知的合法序列长度
                    my_stack.pop()
                    if len(my_stack) == 0:  #找到一个合法的。记录长度。
                        ans = max(ans ,i-last)
                    else: # 还存在(在栈中失配
                        ans = max(ans,i-my_stack[-1])
        return ans




"""
S3: 
    leetcode 方法，此方法更为巧妙 ， 容易理解。
    # 两次遍历 时间复杂度o(n)  空间复杂度o(1)
    @author  曹鹏 (http://weibo.com/cpcs)

    1. 此种方法很巧妙， 之前S1 中分析知  对于) 分割的串我们将)和栈中(匹配，失配时重新计数即可。
        但是对于( 分割的串 由于遍历时我们也不知此序列是否合法，只能达到末尾才知道。
            所以S1 S2 中都是想要存储(的下标，来判断(造成的分段。   (  ((()))   ((   ((()))
        但是此方法将( 分割 转换为)分割， 我们只要 逆序再次遍历再遍历一次即可。
    2. 所以此处栈都没有必要，只要一个变量即可。
 
"""

class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s :
            return 0
        deep = 0
        last = -1
        ans = 0
        for i in range(len(s)) : 
            if s[i] == '(':  #相当于入栈 
                deep+=1
            else : 
                deep -=1
                if deep < 0:   #相当于S2 中)失配，记录)最后一次失配位置
                    last = i
                    deep = 0 
                elif deep ==0 : #相当于S2中pop后 栈空，此时记录序列长度
                    ans = max(ans,i-last)
                else :  #对应S2 中栈中存在(未匹配， 此处不管
                    pass

        # 逆序遍历， 
        deep = 0 
        last = len(s)
        for i in range(len(s)-1,-1,-1):  
            if s[i] == ')':
                deep+=1
            else :
                deep -=1
                if deep <0 :
                    last = i
                    deep = 0
                elif deep == 0:
                    ans = max(ans ,last-i)
                else :
                    pass

        return ans      




        










if __name__ == '__main__':
    S = Solution()
    ss =S.longestValidParentheses('((()()()(()()()()')
    print(ss)







"""
Q ： 
    此题要知道，序列长度可能会由于(或者) 分割开。所以主要处理如何记录分开时长度。
    ) 造成的分割很容易记录，失配时即重新记录长度即可。 但是(分割的不太好记录，因为遍历过程中我们也不知是否 非法序列。

    S1 ： 对(情况， 记录他们的下标，最后使用下标判断最后一次记录序列的各个段长度。 求Max.   很复杂 麻烦。
    S2 :  和S1一样 选择记录下标。 但是巧妙的是 当匹配()后， 我们求当前已知的最大合法序列长度，不像S1 始终想找Max
             这样的话对) 分割，我们记录最后失配) 位置即可
             对于(  我们使用栈顶(下标 即可知当前合法序列长度。
    S3： 巧妙的将(分割不好判断 通过逆向再次遍历 转换为) 匹配，   优！！！


"""