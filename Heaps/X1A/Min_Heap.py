import sys
sys.path.append('../../LinkedList/X1A/')
from Array import Array
from math import floor, ceil, log

class Min_Heap:
    '''Implementation of min heap with array
    
    Args:
    - FILL_VALUE: default None, the default value of heap
    
    Attributes:
    - data: list, the data of heap in BFS order (PS: the first element was 
    left to be empty)    
    - len: int, the logical size of heap
    - CAPACITY: int, the physical size of heap, start from 1
    - FILL_VALUE: default None, the default value of heap
    
    '''
    
    def __init__(self, CAPACITY = 10, FILL_VALUE=None):
        self.data =  Array(CAPACITY=CAPACITY, FILL_VALUE=FILL_VALUE).data
        self.len = 0
        self.CAPACITY = CAPACITY
        self.FILL_VALUE = FILL_VALUE

        
    def upheap(self):
        '''Upheap last item to follow the heap-order property
        '''
        child_idx = self.len
        parent_idx = floor(self.len/2)
        while self.data[child_idx] < self.data[parent_idx]:
            self.data[child_idx], self.data[parent_idx] = \
            self.data[parent_idx],  self.data[child_idx]
            
            if parent_idx == 1:
                break
            child_idx = parent_idx
            parent_idx = floor(child_idx/2)
    
    
    def insert(self, item):
        '''Insert new node into the min heap
        
        Args:
        - item: int, the data to insert
        
        Return:
        - None
        
        '''
        self.len += 1
        self.data[self.len] = item
        if self.len> 1 :
            self.upheap()     
            
            
    def downheap(self):
        '''Downheap first item to follow the heap-order property
        '''
        parent_idx = 1
        # Choose the child node with smaller data
        if self.len == 2:
            child_idx = 2
        else:
            child_idx = 2 if self.data[2]<self.data[3] else 3

        while self.data[parent_idx] > self.data[child_idx]:
            self.data[child_idx], self.data[parent_idx] = \
            self.data[parent_idx],  self.data[child_idx]
                                    
            if child_idx  > self.len/2:
                break
            parent_idx = child_idx
            if 2*parent_idx == self.len:
                child_idx = 2*parent_idx
            else:
                child_idx = 2*parent_idx if self.data[2*parent_idx]\
                <self.data[2*parent_idx+1] else 2*parent_idx+1
        
        
    def remove_min(self):
        '''Remove the min node from the heap
        '''
        if self.len == 0:
            raise Expertion("Error! The heap is already empty")
        self.data[1] = self.data[self.len]
        self.data[self.len] = self.FILL_VALUE
        self.len -= 1
        if self.len > 2:
            self.downheap()
            
            
    def _min(self):
        '''Return the min value of the heap
        
        Return:
        - int, the minimum vaule node of the heap
        '''
        return self.data[1]
    
    
    def _max(self):
        '''Return the max vaule of the heap
        
        Return:
        - int, the maximum vaule node of the heap
        '''
        if self.len == 0:
            raise Expertion("Error! The heap is empty")
        m = self.data[self.len]
        for i in range(2**(ceil(log(self.len+1, 2)-1)), self.len):
            if self.data[i]> m:
                m = self.data[i]
        return m            