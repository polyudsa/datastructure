class Open_Addressing():
    '''Implementaion of Open Addressing Hash Table
    
    Args:
    - size: int, max number that hash table can contain(mod size)
    - probing_func: probing function
    
    Attributes:
    - Hash_Table: dict
      - .keys: int, hash values
      - .values: int, keys of hash table
    - size: int, max number that hash table can contain(mod size)
    '''
    
    def __init__(self, size, probing_func):
        self.size = size
        self.probing_func = probing_func
        self.Hash_Table = {hash_val : None  for hash_val in range(size)}
        
        
    def insert(self, k):
        '''Insert k into Open Adressing Hash Table
        
        Args:
        - k: int, the element to be inserted
        '''
        
        i = 0
        slot = self.probing_func.cal(k, i) # the slot of k
        while (self.Hash_Table[slot] is not None and 'Delete') and (i<self.size):
            i += 1
            slot = self.probing_func.cal(k, i)
        if i == self.size:
            raise Exception("Error! Hash table is full")
        self.Hash_Table[slot] = k
        
        
    def search(self, k):
        '''Search k in Open Addressing Hash Table
        
        Args:
        - k: int, the element to be searched
        
        Returns:
        if founded:
        - slot: int, the slot of k in hash table
        if not founded:
        return None
        '''
        i = 0
        slot = self.probing_func.cal(k, i) # the slot of k
        while (self.Hash_Table[slot] is not None and 'Delete')\
        and (self.Hash_Table[slot]!=k)and (i<self.size):
            i += 1
            slot = self.probing_func.cal(k, i)
        if (self.Hash_Table[slot]!=k) or (i==self.size):
            return None
        return slot
    
    
    def delete(self, k):
        '''Delete x from Chaining Hash Table
        
        Args:
        - x: int, the element to be inserted
        '''
        
        slot = self.search(k)
        if slot is None:
            raise Exception("Error! The element is not in hash table")
        self.Hash_Table[slot] = 'Deleted'