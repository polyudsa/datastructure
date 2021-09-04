class Node(object):
    """单链表结点"""
    def __init__(self, item):
        # item 存储数据
        self.item = item
        # next指向下一结点
        self.next = None
    
class SingleLinkList(object):
    """单链表"""
    def __init__(self):
        """初始化链表"""
        self._head = None

    def is_empty(self):
        """"判断链表是否为空"""
        return self._head is None

    def length(self):
        """返回链表元素个数"""
        cur = self._head
        count = 0
        while cur is not None:
            count += 1
            cur = cur.next
        return count
    
    def items(self):
        """遍历元素"""
        data = []
        cur = self._head
        while cur is not None:
            data.append(cur.item)
            cur = cur.next
        return data
    
    def add(self, item):
        """头部添加元素"""
        node = Node(item)
        # 新结点指向原头部结点
        node.next = self._head
        # 新结点赋值给头部结点
        self._head = node
    
    def append(self, item):
        """尾部添加元素"""
        node = Node(item)
        if self.is_empty():
            self._head = node
        else:
            cur = self._head
            while cur.next is not None:
                cur = cur.next
            cur.next = node
    
    def insert(self, index, item):
        """指定位置插入元素"""
        if index <= 0:
            self.add(item)
        elif index > (self.length() - 1):
            self.append(item)
        else:
            node = Node(item)
            cur = self._head
            for i in range(index - 1):
                cur = cur.next
            node.next = cur.next
            cur.next = node

    def remove(self, item):
        """删除结点"""
        cur = self._head
        pre = None
        while cur.item != item:
            pre = cur
            cur = cur.next         
        pre.next = cur.next
    
    def find(self, item):
        """查找元素位置"""
        data = self.items()
        count = 0
        while count < len(data):
            if data[count] == item:
                print("found item in index %d" % count)
                break
            else:
                count += 1

        if count >= len(data):
            print("Unfounded")

if __name__ == "__main__":
    link_list = SingleLinkList()
    for i in range(10):
        link_list.append(i)
    link_list.add(15)
    link_list.insert(3, 8)
    link_list.remove(8)
    link_list.find(4)
    print(link_list.items())
        
