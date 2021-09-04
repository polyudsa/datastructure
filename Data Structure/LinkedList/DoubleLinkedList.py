class Node(object):
    def __init__(self, item=None):
        """与单链表不同在于添加了前向指针"""
        self.item = item
        self.pre = None
        self.next = None

class DoubleLinkedList(object):
    def __init__(self):
        """初始化双链表"""
        self._head = None
    
    def is_empty(self):
        return self._head == None
    
    def length(self):
        cur = self._head
        count = 0
        while cur is not None:
            cur = cur.next
            count += 1
        return count
    
    def items(self):
        cur = self._head
        while cur is not None:
            yield cur.item
            cur = cur.next
    
    def add(self, item):
        """表头插入元素"""
        node = Node(item)
        if self._head == None:
            self._head = node
        else:
            self._head.pre = node
            node.next = self._head
            node = self._head
    
    def append(self, item):
        """表尾插入元素"""
        if self.is_empty():
            self.add(item)
        else:
            cur = self._head
            node = Node(item)
            while cur.next != None:   
                cur = cur.next
            cur.next = node
            node.pre = cur

    def insert(self, index, item):
        cur = self._head
        node = Node(item)
        if index <= 0:
            self.add(item)
        elif index >= (self.length()-1):
            self.append(item)
        else:
            for i in range(index -1):
                cur = cur.next
            node.next = cur.next
            cur.next.pre = node
            node.pre = cur
            cur.next = node

    def remove(self,item):
        cur = self._head
        while cur.item != item:
            cur = cur.next
        cur.pre.next = cur.next
        cur.next.pre = cur.pre
    
    def find(self, item):
        count = 0
        for i in self.items():
            if i == item:
                print("found item in index %d" % count)
                break
            else:
                count += 1
        if count >= self.length():
            print("Unfounded")


if __name__ == "__main__":
    link_list = DoubleLinkedList()
    for i in range(10):
        link_list.append(i)
    link_list.add(15)
    print(link_list.length())

    link_list.insert(3, 8)
    link_list.remove(8)
    link_list.find(4)

    # 迭代生成器
    data = link_list.items()
    while True:
        try:
            print(data.__next__()," ")
        except StopIteration:
            exit