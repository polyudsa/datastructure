class Doubly_Node:
    ''' Implementation of Doubly Node
    
    Args:
    - init_data: initiate data of a node
        
    Attributes:
    - data: the data of the node
    - next: the pointer that points to the next node
    - prev: the pointer that points to the previous node
    '''
    def __init__(self, init_data):
        self.data = init_data
        self.next = None
        self.prev = None
        

class Doubly_List:
    ''' Implementation of doubly linked list
    
    Attributes:
    - head: Doubly_Node, the head of Doubly_list
    - tail: Doubly_Node, the tail of Doubly_list
    - len: int, the number of nodes
    '''
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.len = 0    
            
    
    def insert_first(self, item):
        # O(1)
        ''' Insert a new node at the head
        
        Args:
        - item: the data of new node
        '''   
        
        # Initiate the doubly linked list
        if self.len == 0:            
            new_node = Doubly_Node(item)          # 1. create a node   
            self.head = new_node                  # 2. point the head to the node
            self.tail = new_node                  # 3. point the tail to the node
            self.len += 1                         # 4. length plus 1
           
        # Insert node before the first node
        else:                
            new_node = Doubly_Node(item)          # 1. create a new node                       
            new_node.next = self.head             # 2. connect the new node to the original first node    
            self.head.prev = new_node             # 3. connect the original first node to the new node                
            self.head = new_node                  # 4. point the old head to the new node
            self.len += 1                         # 5. length plus 1
                        
                
    def insert_last(self, item):
        # O(1)
        ''' Insert a new node at the tail
        
        Args:
        - item: the data of new node   
        '''
        
        # Initiate the doubly linked list
        if self.len == 0:            
            new_node = Doubly_Node(item)          # 1. create a node   
            self.head = new_node                  # 2. point the head to the node
            self.tail = new_node                  # 3. point the tail to the node
            self.len += 1                         # 4. length plus 1
           
        # Insert node after the last node
        else:                
            new_node = Doubly_Node(item)          # 1. create a new node                       
            new_node.prev = self.tail             # 2. connect the new node to the original last node    
            self.tail.next = new_node             # 3. connect the original last node to the new node                
            self.tail = new_node                  # 4. point the old tail to the new node
            self.len += 1                         # 5. length plus 1
        
        
    def insert(self, item, target_index):
        # O(n)
        ''' Insert a new node to the target index
        
        Args:
        - item: the data of new node
        - target_index: int, the target index of new node        
        '''
        
        if (target_index > self.len) and (self.len != 0):
            raise Exception("Error! The index is out of range")
        elif target_index < 0:
            if -target_index > self.len +1 :
                raise Exception("Error! The index is out of range")
            target_index = target_index + self.len + 1
            
        # Insert a new node at the head
        if target_index == 0:
            self.insert_first(item)               # O(1)
            
        # Insert a new node at the tail
        elif target_index == self.len:
            self.insert_last(item)                # O(1)
            
        # Insert in bewteen
        else:
            new_node = Doubly_Node(item)          # 1. create a new node
            predecessor = self.head              
            for i in range(target_index-1):       # 2. locate the predecessor
                predecessor = predecessor.next    # O(n)
            successor = predecessor.next          # 3. locate the sucessor
            
            new_node.next = successor             # 4. connect the new node to the successor
            successor.prev = new_node             # 5. connect the successor to the new node
            new_node.prev = predecessor           # 6. connect the new node to the predecessor
            predecessor.next = new_node           # 7. connect the predecessor to the new node
            self.len += 1                         # 8. length plus 1
        
    def delete_first(self):
        # O(1)
        ''' Delete the node at the head'''
        
        if self.len == 1:
            self.head = None
            self.tail = None
            self.len -= 1
        else:
            self.head.next.prev = None            # 1. connect the second node to None
            self.head = self.head.next            # 2. move head to the second node
            self.len -= 1                         # 3. length minus 1
        
    def delete_last(self):
        # O(1)
        ''' Delete the node at the tail'''
        
        if self.len == 1:
            self.head = None
            self.tail = None
            self.len -= 1
        else:
            self.tail.prev.next = None            # 1. connect the second node from tail to None
            self.tail = self.tail.prev            # 2. move tail to previous node 
            self.len -= 1                         # 3. length minus 1

    def delete(self, target_index):
        # O(n)
        ''' Delete the node at target index
        
        Args:
        - target_index: int, the target index of deleting node 
        '''
        
        if target_index+1 > self.len:
            raise Exception("Error! The index is out of range")
        elif target_index < 0:
            if -target_index > self.len:
                raise Exception("Error! The index is out of range")
            target_index += self.len
            
        # Delete the node at the head
        if target_index == 0:
            self.delete_first()                    # O(1)
            
        # Delete the node at the tail
        elif target_index+1 == self.len:
            self.delete_last()                     # O(1)
            
        # Delete the node in between
        else:
            predecessor = self.head
            for i in range(target_index-1):         # O(n)
                predecessor = predecessor.next      # 1. locate the predecessor
            successor = predecessor.next.next       # 2. locate the successor
            predecessor.next = successor            # 3. connect the predecessor to the successor
            successor.prev = predecessor            # 4. connect the successor to the predecessor
            self.len -= 1                           # 5. length minus 1