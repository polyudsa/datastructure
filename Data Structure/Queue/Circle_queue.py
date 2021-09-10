class MyCircleQueue(object):
    def __init__(self, k:int):
        """initialize the queue, k is the size of the queue"""
        self.queue = [0]*k
        self.head_index = 0
        self.capacity = k
        self.count = 0 
    
    def enqueue(self, item) -> bool:
        if self.count == self.capacity:
            return False
        self.queue[(self.head_index + self.count)%self.capacity] = item
        self.count += 1
    
    def dequeue(self) -> bool:
        if self.count == 0:
            return False
        self.head_index = (self.head_index + 1) % self.capacity
        self.count -= 1

    def get_size(self) -> int:
        return self.count
    
    def is_empty(self) -> bool:
        return self.count == 0
    
    def front(self):
        if self.count == 0:
            return False
        return self.queue[self.head_index]
    
    def rear(self):
        if self.count == 0:
            return False
        return self.queue[(self.head_index + self.count - 1)%self.capacity]

if __name__ == "__main__":
    circle = MyCircleQueue(10)
    for i in range(6):
        circle.enqueue(i)
    # 出队
    circle.dequeue()
    # 获取队列大小
    print(circle.get_size())
    # 获取front元素
    print(circle.front())
    # 获取rear元素
    print(circle.rear())