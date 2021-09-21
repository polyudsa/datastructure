class Array(object):
    ''' Implementation of array
    
    Args:
    - data: list, the elements of array
    - CAPACITY: int, the physical size of array
    - FILL_VALUE: default None, the default value of array
        
    Attributes:
    - data: list, the elements of array
    - len: int, the logical size of array
    - CAPACITY: int, the physical size of array, start from 1
    - FILL_VALUE: default None, the default value of array
    
    '''
    

    def __init__(self, data=None, CAPACITY=10, FILL_VALUE=None):
        # O(n)
        self.data = list()
        self.FILL_VALUE = FILL_VALUE
        for count in range(CAPACITY):
            self.data.append(FILL_VALUE)
        if data is not None:
            for i, element in enumerate(data):             # O(n)
                self.data[i] = element
            self.len = i+1                   # the logical size of array
        else:
            self.len = 0                     # the logical size of array
            
        self.CAPACITY = CAPACITY             # the physical size of array
        
        
    def insert(self, data, target_index):
        # O(n)
        '''Insert new item to target index
        
        Args: 
        - data: the item to insert
        - target_index: int, the target index of new item, start from 0
        
        '''
        if self.CAPACITY == self.len:
            raise Exception("Error! The array is full")
            
        if (target_index > self.len) and (self.len != 0):
            raise Exception("Error! The index is out of range")
        elif target_index < 0:
            if -target_index > self.len +1 :
                raise Exception("Error! The index is out of range")
            target_index = target_index + self.len + 1
            
        for i in range(self.len, target_index, -1):  # O(n)
            self.data[i] = self.data[i-1]
        self.data[target_index] = data
        self.len += 1
        
        
    def delete(self, target_index):
        # O(n)
        '''Delete the item of target index
        
        Args:
        - target_index: int, the target index of deleting item, start from 0
        
        '''
        if target_index+1 > self.len:
            raise Exception("Error! The index is out of range")
        elif target_index < 0:
            if -target_index > self.len:
                raise Exception("Error! The index is out of range")
            target_index += self.len

        for i in range(target_index, self.len-1):   # O(n)
            self.data[i] = self.data[i+1]

        self.data[self.len-1] = self.FILL_VALUE
        self.len -= 1

            
    def array_max(self):
        # O(n) sequential search
        currentMax = self.data[0]
        for i in range(1, self.len):                # O(n)
            if self.data[i] > currentMax:
                currentMax = self.data[i]
        return currentMax