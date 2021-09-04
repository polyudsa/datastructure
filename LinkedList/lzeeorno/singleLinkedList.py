'''
单链表实现
1. 从头部插入
2.从尾部插入
3. 空链表
4. 从指定位置插入
5.删除功能
6. 查找下一个
'''
#创建节点
class Node(obj):
    def __init__(self,item) -> None:
        self.element = item
        self.next = None
        