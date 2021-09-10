class Queue(object):
    def __init__(self,size=5):
        """初始化"""
        self.items = []
    
    def is_Empty(self):
        return len(self.items) == 0
    
    def get_Size(self):
        return len(self.items)
    
    def enqueue(self, item):
        """入栈,时间复杂度O(1),队尾添加即可"""
        self.items.append(item)
    
    def dequeue(self):
        """出栈,时间复杂度O(n),要移动次位元素到首位"""
        print(self.items.pop(0))
        for i in range(self.get_Size() - 1):
            self.items[i] = self.items[i+1]
        self.items.pop() 

    def clear(self):
        self.items = []

if __name__ == "__main__":
    q = Queue()
    # 初始化
    for i in range(10):
        q.enqueue(i)
    print(q.items)
    # 出队列
    q.dequeue()
    # 打印元素
    print(q.items)
    # 获取长度
    print(q.get_Size())
    # 判断是否为空
    print(q.is_Empty())