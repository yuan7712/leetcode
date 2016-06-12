"""
Given a binary tree, return the inorder traversal of its nodes' values.
中序遍历
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

"""
S1: 
    中序遍历：  左 根 右 ;  使用栈： 时间o(n)  空间o(n)
    p ： 一直向左 直到 null; 
    visit  pop 
    转右子树
"""
class Solution1(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        m_stack = []
        ans = []
        p = root

        while p or m_stack:
            while p :
                m_stack.append(p)
                p = p.left
            p = m_stack.pop()
            ans.append(p.val) #visit
            p = p.right
        """
        while  root or m_stack:
            if p:
                m_stack.append(p)
                p = p.left
            else:
                p = m_stack.pop()
                ans.append(p.val)
                p = p.right
        """
        return ans



"""
S2 :
    此方法 栈模拟递归中栈 策略;前中后序 均能在S2 不同位置visit 实现遍历.
    visit node 时： 栈中 根到此node path.

"""
class Solution2(object):
    def inorderTraversal(self, root):
        if not root :
            return []
        m_stack = []
        ans = []
        last = None # last pop 
        while root or m_stack:
            if root:   # 一直向左
                m_stack.append(root)
                # pre
                #ans.append(root.val)
                root = root.left
            else :
                root = m_stack[-1]
                #inorder
                """
                中序： 由于转向右子树后 其父节点还在栈中，如果不if 当从右子树回溯时 可能其父节点再次visit
                """
                if root.right == None or root.right!=last:
                    ans.append(root.val)

                # 只有当右子树全部visit后， 才会将其父节点pop, last 记录上一次pop 的node.
                if root.right == None or root.right == last:
                    last = m_stack.pop()
                    # post order  
                    #ans.append(last.val)
                    root = None
                # 转右子树，
                else:
                    root = root.right
        return ans




"""
S3: Morris  遍历 时间o(n) 空间o(1)  不使用栈

    如果不使用栈,使用o(1)空间,最大的问题就是在遍历子节点后 如何返回其父节点.Morris 使用了线索二叉树的思路.
我们利用叶子节点的空指针域 记录它的pre succ 即可.
    1. 如果p.left 为空, visit p. 然后转right 即可.(注意: 此处即使p为叶子节点, 在访问p之前已经将p的后继设置好了)
    2. 如果p.left 非空, 找到其前驱
            case1 :  前驱.right 指向自己, 说明p的左子树已经访问过了, 所以visit p, 然后转右即可
            case2 :  前驱.right==null , 说明p的左子树还没有访问,所以将其前驱.right 指向p. 然后转向左侧即可;
    T:  
        1.此方法核心就是当我们要 向左转时, 我们将其前驱.right指向自己. 这样就保证左子树访问完后还能回到父节点.
        2. 当返回父节点后,我们如何防止再次转向左侧？ 
             我们再次找其前驱,如果前驱.right 已经指向自己了,说明左子树已经访问完. 转右即可.
             由上可知,对于node p 我们会两次找其前驱. 第一次设置前驱.right 指向自己.  第二次确定左侧访问完毕.
        3. n个node的n-1 条边, 每条最多走两次.
        4. 这三种Morris 代码基本一致. 都是基于线索, 找p的中序前驱
    R:  
        http://www.cnblogs.com/AnnieKim/archive/2013/06/15/MorrisTraversal.html



"""
class Solution(object):
    def inorderTraversal(self, root):
        if not root:
            return []
        ans = []
        p = root
        while p:
            if not p.left :  #left == null  visit
                ans.append(p.val)
                p = p.right   
            else: # left!=null
                tmp = p.left
                while tmp.right and tmp.right!=p:   # 找到其前驱
                    tmp = tmp.right
                if tmp.right == p:  # 第二次访问前驱, 表明左子树已经visit
                    ans.append(p.val)
                    tmp.right = None # 重置线索,还原原样
                    p = p.right
                else:   # 第一次访问前驱, 建立线索
                    tmp.right = p
                    p = p.left
        return ans



                





"""
S:
    中序遍历: 左 根 右 
    1. 最简单  递归
        前 中 后 递归很方便;只要修改visit的位置即可. 
        他们代码一致 是由于 递归栈的pop push 策略一致; 当visit该元素时  栈中为根->此node path
    2. 非递归  使用栈; 
        2.1 : S1
        2.2 : S2 
        T:  非递归实现中,可以有多种写法,主要就是由于我们对栈中元素保存策略不同;
            S1: S1中当访问root后 转向右子树时  栈中不会再存放 root;  采取直接pop转右;
            S2：我们对S1 改变visit位置,即可变为前序,但是后序则不可以. S2 则采取模拟递归 中栈的策略, 
                 所以我们在S2 中只要在不同位置visit 即可前 中 后 遍历. 

    3. 非递归  不使用栈; 时间o(n)空间o(1)  S3  Morris

"""


if __name__ == '__main__':
    S =Solution()
    p1 = TreeNode(1)
    p2 = TreeNode(2)
    p3 = TreeNode(3)
    p1.right = p2
    p2.left  = p3
    ss = S.inorderTraversal(p1)
    print(ss)