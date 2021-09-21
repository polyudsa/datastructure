class Singly_Node:
    ''' Implementation of singly linked list node
    
    Args:
    - init_data: initiate data of a node
        
    Attributes:
    - data: the data of the node
    - next: the pointer that points to the next node
    
    '''
    def __init__(self, init_data):
        self.data = init_data
        self.next = None
        
        
class Singly_List:
    ''' Implementation of singly linked list
    
    Attributes:
    - head: Singly_Node, the head of Singly_list
    - len: int, the number of nodes
    '''
    
    def __init__(self):
        self.head = None
        self.len = 0            
    
    
    def insert_first(self, item):
        # O(1)
        ''' Insert a new node at the head
        
        Args:
        - item: the data of new node
        '''
        new_node = Singly_Node(item)            # 1. create a new node
        new_node.next = self.head               # 2. connect the new node to the first node 
        self.head = new_node                    # 3. point the head to the new node
        self.len += 1                           # 4. length plus 1
        
            
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
            
        # Insert at first
        if target_index == 0:                     
            self.insert_first(item)              # O(1)
            
        # Insert in between
        else:                                    
            new_node = Singly_Node(item)         # 1. create a new node
            predecessor = self.head
            for i in range(target_index-1):      # O(n)
                predecessor = predecessor.next   # 2. locate the location to insert            
            new_node.next = predecessor.next     # 3. connect the new node with successor
            predecessor.next = new_node          # 4. connect the new node with predecessor
            self.len += 1                        # 4. length plus 1
            
                        
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
            
        # Delete at first
        if target_index == 0:                     
            self.head = self.head.next           # 1. move head to next node
            self.len -= 1                        # 2. length minus 1
            
        # Delete in between
        else:                                    
            predecessor = self.head 
            for i in range(target_index-1):      # O(n)     
                predecessor = predecessor.next   # 1. locate the node before deleted node
            predecessor.next = predecessor.next.next # 2. connect the front and back of the deleted node
            self.len -= 1                        # 3. length minus 1