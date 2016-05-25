"""
Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and set.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
set(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

"""

#  使用双向循环链表
class LruNode(object):
     def __init__(self, k,v,p,n):
        self.key = k
        self.value = v
        self.next = n
        self.pre  = p




class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cap = capacity
        self.now_cap = 0 #记录当前容量
        self.my_dict = {}  #dict  存放key-node索引；
        self.my_head = LruNode(0,0,None,None) #head
        self.my_head.pre = self.my_head   #循环链表
        self.my_head.next = self.my_head


        

    def get(self, key):
        """
        :rtype: int
        """
        l = self.my_dict.get(key,None)   #(key-node地址)
        if not l : #不存在
            return -1
        else:  #get后应该前置，所以先del 后add
            self.delItem(l)
            self.add(l)
            return l.value 
        

    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: nothing
        """
        tmp = self.my_dict.get(key,None) 
        if tmp :   #已经存在  更新val
            tmp.value = value
            self.get(tmp.key)  #kaoqian
            return 
        if self.cap == self.now_cap :
            k = self.delItem(self.my_head.next)  #删除head 处
            self.my_dict.pop(k)

        new_node = LruNode(key,value,None,None)
        self.add(new_node)



    # 添加到队尾 , 并且add 到dict    
    def add(self,Lnode): 
        tmp = self.my_head.pre
        tmp.next = Lnode
        Lnode.pre = tmp
        Lnode.next = self.my_head
        self.my_head.pre = Lnode
        self.now_cap +=1
        self.my_dict[Lnode.key] = Lnode


# del 没有del dict中的key; 返回了key ; 也可以在此处del key-value
    def delItem(self,Lnode):
        key = self.my_head.next.key
        Lnode.pre.next = Lnode.next
        Lnode.next.pre = Lnode.pre
        self.now_cap -=1
        return key


          


if __name__ == '__main__':
    S = LRUCache(2)
    r = S.set(2,1)
    S.set(1,1)
    S.set(2,3)
    S.set(4,1)
    rrr = S.get(1)
    print(rrr)
    rr = S.get(2)
    print(rr)








"""
Q: LRU 最近最少使用. 
    1. 实现get. (使用key ,所以考虑使用hashmap 加速访问), 当找到该点后 要将该点置到链表的前面
    2. set 放到链表前面，当达到容量后del 后面元素。

A ： 
    1. 使用hashmap保存 key和node索引
    2. 使用双向循环链表。(方便del add ) 
          创建头结点方便操作。 靠近队头为不常使用的，(满时del)  队尾常使用的，set时填到队尾
    3. http://flychao88.iteye.com/blog/1977653


E :
    1.  在保存键值对时， 记住在add 函数内 self.my_dict[Lnode.key] = Lnode ;  更新Lnode 的pre和next 后再入dict
    2. set() 当原来的 key  已经存在时  应该更新value
    3. set()  更新操作后 应该将该node靠前， 即可以使用get()  使之靠前

"""