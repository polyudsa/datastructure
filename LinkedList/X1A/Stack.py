class Stack:
    ''' Implementation of Stack
    
    Args:
    - LEN: int, the physical size of stack, start from 1
    - FILL_VALUE: the default value of stack, default None
    
    Attributes:
    - data: list, the elements of stack
    - top: int, the number of elements, equal zero where empty
    - LEN: int, the physical size of stack, start from 1, default 100
    - FILL_VALUE: the default value of stack, default None
    '''
    
    def __init__(self, LEN=100, FILL_VALUE=None):
        assert LEN >= 1
        self.data = list()
        self.FILL_VALUE = FILL_VALUE
        for count in range(LEN):
            self.data.append(FILL_VALUE)
        
        self.top = 0               # the logical size of stack         
        self.LEN = LEN             # the physical size of stack
        
    
    def Push(self, item):
        '''Insert new item to the top of the stack
        
        Args:
        - item: the item to insert
        
        '''
        if self.top == self.LEN:
            raise Exception("Error! The stack is full")
        else:            
            self.data[self.top] = item  
            self.top += 1
            
            
    def Top(self):
        '''Return the topmost element in the stack without removing it
        '''
        if self.is_empty():
            raise Exception("Error! The stack is empty")
        else:
            return self.data[self.top-1]

        
    def Pop(self):
        '''Extract the top item from the stack
        '''
        if self.is_empty():
            raise Exception("Error! The stack is empty")
        else:
            self.top -= 1
            self.data[self.top] = self.FILL_VALUE
            
    def is_empty(self):
        if self.top == 0:
            return True
        else:
            return False