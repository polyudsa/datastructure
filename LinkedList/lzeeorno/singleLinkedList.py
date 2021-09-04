'''
单链表实现
1. 从头部插入
2.从尾部插入
3. 空链表
4. 从指定位置插入
5.删除功能
6. 查找下一个
7. 遍历
'''
#创建节点
class Node(object):
    def __init__(self,item) -> None:
        self.element = item
        self.next = None
#create single linkedlist class
class SingleLinkedList(object):
    def __init__(self) -> None:
        self.header = None
        self.length = 0
    #1
    def add_head(self,node):
        if self.is_empty():
            self.header = node
        else:
            self.next = self.header
            self.header = node
        self.length += 1

    #2
    def append(self,node):
        curr_Node = self.header
        if self.is_empty():
            self.add_head(node)
        else:
            while(curr_Node != None):
                curr_Node = curr_Node.next
            curr_Node.next = node
            self.length += 1  
    #3
    def is_empty(self):
        if self.header == None:
            return True
        else:
            return False

    #7
    def travel(self):
        curr_Node = self.header
        if self.length == 0:
            print('空链表')
        else:
            for i in range(self.length):
                print("%s"% curr_Node.element, end = " ")
                curr_Node = curr_Node.next
            print("\n")
def main():
    node1 = Node(1)
    single_link_list = SingleLinkedList()
    while True:
        num = eval(input("输入操作："))
        if(num == 1):
            print("list:")
            single_link_list.travel()
            node1=Node(eval(input("输入你想要插入在头部的数：")))
            single_link_list.add_head(node1)
            print("list:")
            single_link_list.travel()
        
        if(num == 2):
            print("list:")
            single_link_list.travel()
            node2 = Node(eval(input("输入你想要插入在尾部的数：")))
            single_link_list.append(node2)
            print("list:")
            single_link_list.travel()

        if(num == 3):
            print("searching...")
            single_link_list.travel()
            print("\n")
        
        if (num == 0):
            break

if __name__ == '__main__':
    main()