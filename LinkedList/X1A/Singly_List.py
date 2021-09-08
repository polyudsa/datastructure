class Singly_Node:
    ''' Implementation of Node
    
    Args:
    - initData: initiate data of a node
        
    Attributes:
    - data: the data of the node
    - next: the pointer that points to the next node
    
    '''
    def __init__(self, initData):
        self.data = initData
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
        
    def print_list(self):
        # O(n)
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next
    
    def insert_first(self, item):
        # O(1)
        ''' Insert a new node at the head
        
        Args:
        - item: the data of new node
        '''
        newNode = Singly_Node(item)             # 1. create a new node
        newNode.next = self.head                # 2. connect the new node to the first node 
        self.head = newNode                     # 3. point the head to the new node
        self.len += 1                           # 4. length plus 1
            
    def insert(self, item, targetIndex):
        # O(n)
        ''' Insert a new node to the target index  
        
        Args:
        - item: the data of new node
        - targetIndex: int, the target index of new node
        '''
        if (targetIndex > self.len) and (self.len != 0):
            raise Exception("Error! The index is out of range")
        elif targetIndex < 0:
            if -targetIndex > self.len +1 :
                raise Exception("Error! The index is out of range")
            targetIndex = targetIndex + self.len + 1
            
        # Insert at first
        if targetIndex == 0:                     
            self.insert_first(item)              # O(1)
            
        # Insert in between
        else:                                    
            newNode = Singly_Node(item)          # 1. create a new node
            predecessor = self.head
            for i in range(targetIndex-1):       # O(n)
                predecessor = predecessor.next   # 2. locate the location to insert            
            newNode.next = predecessor.next      # 3. connect the new node with successor
            predecessor.next = newNode           # 4. connect the new node with predecessor
            self.len += 1                        # 4. length plus 1
                        
    def delete(self, targetIndex):
        # O(n)
        ''' Delete the node at target index    
        
        Args:
        - targetIndex: int, the target index of deleting node        
        '''
        if targetIndex+1 > self.len:
            raise Exception("Error! The index is out of range")
        elif targetIndex < 0:
            if -targetIndex > self.len:
                raise Exception("Error! The index is out of range")
            targetIndex += self.len
            
        # Delete at first
        if targetIndex == 0:                     
            self.head = self.head.next           # 1. move head to next node
            self.len -= 1                        # 2. length minus 1
            
        # Delete in between
        else:                                    
            predecessor = self.head 
            for i in range(targetIndex-1):       # O(n)     
                predecessor = predecessor.next   # 1. locate the node before deleted node
            predecessor.next = predecessor.next.next # 2. connect the front and back of the deleted node
            self.len -= 1                        # 3. length minus 1