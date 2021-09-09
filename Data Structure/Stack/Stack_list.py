class Stack(object):
    def __init__(self):
        """初始化"""
        self.items = [] 

    def is_Empty(self):
        """判断是否为空"""
        return len(self.items) == 0
    
    def peek(self):
        """查看栈最上层的元素"""
        print(self.items[-1])
    
    def push(self, item):
        """元素入栈"""
        self.items.append(item)
    
    def pop(self):
        """元素出栈"""
        return self.items.pop()
    
    def search(self, item):
        """查找元素，返回index"""
        temps = []
        for i in range(len(self.items)):
            pop_item = self.items.pop()
            temps.append(pop_item)
            if pop_item == item:
                print(i)
                break
            else:
                i += 1
        for i in temps:
            self.push(i)
    
    def insert(self, item,index):
        i = 0
        temps = []
        while i < (index - 1):
            temps.append(self.items.pop())
            i += 1
        self.items.append(item)
        self.items += temps

if __name__ == "__main__":
    s = Stack()
    print(s.is_Empty())
    for i in range(1, 10):
        s.push(i)
    print(s.peek())
    s.pop()
    print(s.peek())

    s.search(5)
    s.insert(11, 5)
    print(s.items)