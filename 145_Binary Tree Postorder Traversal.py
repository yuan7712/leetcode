"""
Given a binary tree, return the postorder traversal of its nodes' values.
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None




"""
S1:
    1. push 一直向左, tag=0 标记入栈后转向左子树;
    2. 此时判断是左还是右侧上升.
            case right:  直接pop 父节点即可
            case left：  转向right 并且设置父点tag==1, 表示父点转向右子树
"""
class Solution1(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        m_stack = []
        ans = []
        if not root : 
            return []
        p = root

        while p or m_stack:
            while p :
                m_stack.append([p,0])   #push add info from left(tag==0)
                p = p.left
            # p == null 栈顶为其父点. 可能左或右上升. 如果右侧上升 直接pop即可. (右子树单支 递归)
            while m_stack and m_stack[-1][1] == 1 :
                tmp = m_stack.pop()[0]
                ans.append(tmp.val)  # visit
            # 转向right, 修改父点 tag=1 
            if m_stack:   # turn  right  
                m_stack[-1][1] = 1   # tag = 1
                p  = m_stack[-1][0].right   # p可能null
        return ans



"""
S2: 
    1. p 一直向左
    2. 如果p 右子树非空 push p; 转右即可.
    3. p 为叶子节点,visit ; (此时栈顶是其父点)  此时判断是否可以退栈    然后转向父节点右子树
        退栈 case 1:  m_stack[-1].right == last   last 点是从右子树上升 一直递归
             case 2:  m_stack[-1].right == None   此时父点右子树null, pop即可
"""
class Solution2(object):
    def postorderTraversal(self, root):
        m_stack = []
        ans = []
        last = None   # last visit
        p = root 

        while p or m_stack:
            while p.left:    # left->
                m_stack.append(p)
                p = p.left

            if p.right: # 转右子树
                m_stack.append(p)
                p = p.right
            else: 
                ans.append(p.val)  # visit  叶子点
                last = p
                 # pop  退栈
                while m_stack and (m_stack[-1].right == last or m_stack[-1].right == None):
                    last = m_stack.pop()
                    ans.append(last.val) #visit
                if m_stack :  # 转右
                    p = m_stack[-1].right
                else:
                    p = None # over
        return ans



"""
S3 :
    前 中 后 通用方法,
    1. 此方法和S2 一样. 
    2. 同样都是 记录last 访问node.
"""

class Solution3(object):
    def postorderTraversal(self, root):
        if not root :
            return []
        m_stack = []
        ans = []
        last = None # last pop

        while root or m_stack:
            if root:
                m_stack.append(root)
                # pre order
                #ans.append(root.val)
                root = root.left
            else :
                root = m_stack[-1]
                #in order
                #if root.right == None or root.right!=last:
                    #ans.append(root.val)
                if root.right == None or root.right == last:
                    last = m_stack.pop()  # last  visit
                    # post order 
                    ans.append(last.val)  #visit
                    root = None
                else:
                    root = root.right
        return ans        



"""
S4:   *******
    将前序 根 左 右; 稍作改变, 左右换序; 最后遍历结果为 根 右 左. 
    reverse 即后序.
"""
class Solution4(object):
    def postorderTraversal(self, root):
        if not root :
            return []
        m_stack = []
        ans = []
        m_stack.append(root)

        while m_stack:
            p = m_stack.pop()
            ans.append(p.val)  #visit
            # 改变顺序 先left 后right ;变为根 右 左 遍历
            if p.left : 
                m_stack.append(p.left)
            if p.right:
                m_stack.append(p.right)
        ans.reverse()
        return ans

"""
S5:
    Morris + S4 方法.
    S4 中将后序遍历 转换为    根右左(前序改变)+reverse 
    此方法 Morris 对前序Morris 改变 然后reverse;
    1. 只需将前序Morris 中所有 left right  改变即可
"""
class Solution5(object):
    def postorderTraversal(self, root):
        if not root :
            return []
        ans = []
        p = root
        while p :
            if not p.right:
                ans.append(p.val)
                p = p.left
            else:
                tmp = p.right
                while tmp.left and tmp.left !=p:
                    tmp = tmp.left
                if tmp.left == p:
                    tmp.left = None
                    p = p.left
                else:
                    tmp.left = p
                    ans.append(p.val)
                    p = p.right
        ans.reverse()
        return ans

"""
S6:
    Morris 后序遍历 比前 中 稍微复杂,但是基本一致.

    1. 和前中 一样, 我们在转向左子树时 也是找到该Node p 的前驱q,  将q.right 指向自己;
    2. 但是我们应该在哪遍历？ 
         后序遍历 ： 左 右 根; 
         前 ： 根 左 右  中： 左 根 右  
         当前中序中 第二次到达p的前驱q时, 我们就可以直接转向p的右子树; 但是后序必须得向上返回遍历父节点.
      这些父节点 即 p 左子树到q 的path.  我们只需在转向p 右子树之前 逆序遍历他们即可.
    3. 为此我们增加一个Node , 将整个树 挂到Node 左子树上.


T:
    1. 复杂度： 因为需要  逆序输出p.left 到其前驱的path. 所以和前中相比需要更多空间.
    2. 此方法没有采用转换为 根右左 那样方便. 如S5
R：
    http://www.cnblogs.com/AnnieKim/archive/2013/06/15/MorrisTraversal.html

"""
class Solution(object):
    def postorderTraversal(self, root):
        if not root :
            return []
        ans = []

        p = TreeNode(0)
        p.left = root

        while p :
            if not p.left :  # left null turn right
                p = p.right
            else:
                tmp = p.left
                while tmp.right and tmp.right!= p:  # find p's pre
                    tmp = tmp.right
                if tmp.right == p:  # 第二次 
                    q = p.left
                    nodes = []
                    while q != p:   # visit q->tmp  reverse
                        nodes.append(q.val)
                        q = q.right
                    nodes.reverse()
                    ans.extend(nodes)   #or ans[len(ans):] = nodes

                    tmp.right = None
                    p = p.right

                else : #right == null
                    tmp.right = p
                    p = p.left
        return ans









"""
后序遍历： 
         左 右 根 
         1. 最简单方法  递归实现
         2. 非递归使用栈：
            后序相比前中序复杂,因为当从孩子node返回根时必须区分从左还是右返回; 左则转右 右则pop visit根.

            2.1 :  使用栈记录每个node访问情况, 转左 右时 判断是否已经访问node,防止重复访问  
            2.2 :  S1  入栈时存储tag,  表示该node入栈后 转向左边还是右边.    
            2.3 :  S2  在遍历时记住last访问点,判断 p.right==last 即可知  是否从右边上升. 
            2.4 ： S3  前 中 后序  通用方法, 此与S2 一样;
            T:    后序遍历中  栈中即为该node的 父点path
         3. 逆向考虑： S4 ***
                    后序： 左 右 根
                    前序： 根 左 右
                    如果在前序遍历时,调换左右入栈顺序,则 变为 根 右 左 ; 这样正好是 后序遍历的reverse; reverse即后序;

         4. Morris 非递归不使用栈 o(1) 空间   S6



R:
    http://noalgo.info/832.html    3. S4
    http://www.cnblogs.com/AnnieKim/archive/2013/06/15/MorrisTraversal.html  4. S5
"""
if __name__ == '__main__':
    S =Solution1()
    p1 = TreeNode(1)
    p2 = TreeNode(2)
    p3 = TreeNode(3)
    p1.right = p3
    p1.left  = p2
    ss = S.postorderTraversal(p1)
    print(ss)
   


