class Array(object):
    ''' Implementation of array
    
    Args:
    - values: list, the values of array
    - capacity: int, the capacity of array
    - fillValue: the default value of array
        
    Attributes:
    - data: list, the data of array
    - logicalSize: int, the logical size of array, start from 1
    - capacity: int, the physical size of array, start from 1
    '''

    def __init__(self, values=None, capacity=10, fillValue=None):
        # O(n)
        self.data = list()
        for count in range(capacity):
            self.data.append(fillValue)
        if values is not None:
            for i, value in enumerate(values):             # O(n)
                self.data[i] = value
            self.logicalSize = i+1          # the logical size of array
        else:
            self.logicalSize = 0            # the logical size of array
            
        self.capacity = capacity            # the physical size of array
        
    def print_array(self):
        # O(n)
        for i in range(self.logicalSize):
            print(self.data[i])
            
    def append(self):
        # O(n)
        # when the array is full, double the capacity
        temp = Array(None, self.capacity*2)
        for i in range(self.logicalSize):                   # O(n)
            temp.data[i] = self.data[i]
        self.data = temp.data
        self.capacity = temp.capacity
        
    def subtract(self):
        # O(n)
        # when logical size <= capacity // 4, reducing the capacity to one-half
        temp = Array(None, self.capacity//2)
        for i in range(self.logicalSize):                   # O(n)
            temp.data[i] = self.data[i]
        self.data = temp.data
        self.capacity = temp.capacity
        
    def insert(self, newItem, targetIndex):
        # O(n)
        '''Insert new item to target index
        
        Args: 
        - newItem: the item to insert
        - targetIndex: int, the target index of new item, start from 0
        
        '''
        # when the array is full, double the capacity
        if self.capacity - self.logicalSize == 0:
            self.append()                                   # O(n)
        for i in range(self.logicalSize, targetIndex, -1):  # O(n)
            self.data[i] = self.data[i-1]
        self.data[targetIndex] = newItem
        self.logicalSize += 1
        
    def delete(self, targetIndex):
        # O(n)
        '''Delete the item of target index
        
        Args:
        - targetIndex: int, the target index of deleting item, start from 0
        
        '''
        if self.logicalSize - targetIndex < 1:
            raise Exception("Error! The index is out of range")

        for i in range(targetIndex, self.logicalSize, 1):   # O(n)
            self.data[i] = self.data[i+1]
        self.data[self.logicalSize] = None
        self.logicalSize -= 1
        
        # when logical size <= capacity // 4, reducing the capacity to one-half
        if  self.logicalSize <= self.capacity// 4:  
            self.subtract()                                 # O(n)
            
    def array_max(self):
        # O(n)
        currentMax = self.data[0]
        for i in range(1, self.logicalSize):                # O(n)
            if self.data[i] > currentMax:
                currentMax = self.data[i]
        return currentMax