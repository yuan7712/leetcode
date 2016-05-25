"""
Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, /. Each operand may be an integer or another expression.

Some examples:
  ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
  ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6


R:
    中缀表达式： A - B * C + D     画成一个二叉树...
    前缀表达式： + - A * B C D    波兰表达式
    后缀表达式： A B C * - D +    逆波兰表达式

后缀表达式计算：  预算对象直接压栈，遇到 运算符 pop 两个数 计算。
"""


class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """

        my_stack = [] 

        for ch in tokens:
            if ch.lstrip('-').isdigit() :    #由于'-3'.isdigit()  False; 使用lstrip() 方法用于截掉字符串左边的空格或指定字符
                my_stack.append(int(ch))
            else:
                tmp1 = my_stack.pop()
                tmp2 = my_stack.pop()
                if ch == '+':
                    my_stack.append(tmp2+tmp1)
                elif ch == '-':
                    my_stack.append(tmp2-tmp1)
                elif ch == '*':
                    my_stack.append(tmp2*tmp1)
                else :
                    if tmp2//tmp1 >=0 or tmp2%tmp1 ==0:
                        my_stack.append(tmp2//tmp1)
                    else:
                        my_stack.append(tmp2//tmp1+1)   #处理-5//2  此种情况

        return my_stack[0]



        





if __name__ == '__main__':
    S =Solution()
    ss =S.evalRPN(["4","-2","/","2","-3","-","-"])
    print(ss)






"""
Q :
     1. 处理负数. '-3'.isdigit()  False
     2. 处理负数的除法问题： 
         -5//2 -> -3 应该纠正为-2 ;   而java之类的 -5/2 = -2
         -4//2 应该为-2
      ["4","-2","/","2","-3","-","-"]
      ["10","6","9","3","+","-11","*","/","*","17","+","5","+"] 
"""