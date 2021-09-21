class Queue:
    '''Implementation of circular queue
    
    Args:
    - LEN: int, the physical size of queue, start from 1
    - FILL_VALUE: the default value of queue, default None
    
    Attributes:
    - data: list, the elements of queue
    - head: int, the position (index+1) of the head item, range from 1 to LEN
    - tail: int, the position (index+1) of the tail (not the tail item), range
    from 1 to LEN
    - LEN: int, the physical size of queue, start from 1
    - FILL_VALUE: the default value of queue, default None
    
    '''
    
    def __init__(self, LEN=100, FILL_VALUE=None):
        assert LEN >= 1
        self.data = list()
        self.FILL_VALUE = FILL_VALUE
        for count in range(LEN):
            self.data.append(FILL_VALUE)
        
        self.head = 1    # the position (index+1) of the head item
        self.tail = 1    # the position (index+1) of the tail (not the tail item)
        self.LEN = LEN   # the physical size of queue
        self.FILL_VALUE = FILL_VALUE
        
        
    def Enqueue(self, item):
        '''Insert new item to the tail
        
        Args:
        - item: the item to insert
        
        '''
        if self.is_full():
            raise Exception("Error! The queue is full")
        
        self.data[self.tail-1] = item
        
        if self.tail == self.LEN:  
            self.tail = 1    # the tail reach the end, re-pointing to the start
        else:
            self.tail += 1
            
    def Dequeue(self): 
        '''Extract the item from the head
        '''
        if self.is_empty():
            raise Exception("Error! The queue is empty")
        
        item = self.data[self.head-1]
        self.data[self.head-1] = self.FILL_VALUE
        if self.head == self.LEN:
            self.head = 1    # the head reach the end, re-pointing to the start
        else:
            self.head += 1
        return item
        
                
    def is_empty(self):
        '''Determine if the queue is empty
        '''
        if self.head == self.tail:
            return True
        else:
            return False
        
            
    def is_full(self):
        '''Determine if the queue is full
        
        PS: To make the sign for empty(tail==head), we need to leave one space
        empty, for example, the queue [ 6 | 2 | 7 | 8 | (tail) | 9(head) | 5 ]
        is full.
        
        '''
        if (self.tail+1 == self.head) or \
        ((self.head==1) and (self.tail == self.LEN)):
            return True
        else:
            return False