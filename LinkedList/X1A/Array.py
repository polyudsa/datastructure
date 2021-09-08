class Array(object):
    ''' Implementation of array
    
    Args:
    - values: list, the values of array
    - capacity: int, the capacity of array
    - fill_value: the default value of array
        
    Attributes:
    - data: list, the data of array
    - logical_size: int, the logical size of array, start from 1
    - capacity: int, the physical size of array, start from 1
    '''

    def __init__(self, values=None, capacity=10, fill_value=None):
        # O(n)
        self.data = list()
        for count in range(capacity):
            self.data.append(fill_value)
        if values is not None:
            for i, value in enumerate(values):             # O(n)
                self.data[i] = value
            self.logical_size = i+1          # the logical size of array
        else:
            self.logical_size = 0            # the logical size of array
            
        self.capacity = capacity            # the physical size of array
        
    def print_array(self):
        # O(n)
        for i in range(self.logical_size):
            print(self.data[i])
            
    def append(self):
        # O(n)
        # when the array is full, double the capacity
        temp = Array(None, self.capacity*2)
        for i in range(self.logical_size):                   # O(n)
            temp.data[i] = self.data[i]
        self.data = temp.data
        self.capacity = temp.capacity
        
    def subtract(self):
        # O(n)
        # when logical size <= capacity // 4, reducing the capacity to one-half
        temp = Array(None, self.capacity//2)
        for i in range(self.logical_size):                   # O(n)
            temp.data[i] = self.data[i]
        self.data = temp.data
        self.capacity = temp.capacity
        
    def insert(self, new_item, target_index):
        # O(n)
        '''Insert new item to target index
        
        Args: 
        - new_item: the item to insert
        - target_index: int, the target index of new item, start from 0
        '''
        # when the array is full, double the capacity
        if self.capacity = self.logical_size:
            self.append()                                   # O(n)
        for i in range(self.logical_size, target_index, -1):  # O(n)
            self.data[i] = self.data[i-1]
        self.data[target_index] = new_item
        self.logical_size += 1
        
    def delete(self, target_index):
        # O(n)
        '''Delete the item of target index
        
        Args:
        - target_index: int, the target index of deleting item, start from 0
        '''
        if self.logical_size - target_index < 1:
            raise Exception("Error! The index is out of range")

        for i in range(target_index, self.logical_size, 1):   # O(n)
            self.data[i] = self.data[i+1]
        self.data[self.logical_size] = None
        self.logical_size -= 1
        
        # when logical size <= capacity // 4, reducing the capacity to one-half
        if  self.logical_size <= self.capacity// 4:  
            self.subtract()                                 # O(n)
            
    def array_max(self):
        # O(n)
        current_max = self.data[0]
        for i in range(1, self.logical_size):                # O(n)
            if self.data[i] > current_max:
                current_max = self.data[i]
        return current_max