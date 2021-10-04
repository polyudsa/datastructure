class Chaining:
    '''Implementaion of Chaining Hash Table
    
    Args:
    - size: int, bucket numbers(mod size)
    - hash_func: hash function
    
    Attributes:
    - Hash_Table: dict
      - .keys: hash values / buckets
      - .values: lists
    - size: int, bucket numbers(mod size)
    '''
    
    def __init__(self, size, hash_func):
        self.size = size
        self.hash_func = hash_func
        self.Hash_Table = {hash_val : []  for hash_val in range(size)}
        
    def search(self, x):
        '''Search x in Chaining Hash Table
        
        Args:
        - x: int, the element to be searched
        
        Returns:
        if founded:
        - x_hash: int, hash value of x, also the bucket number of x in hash table
        - idx: int, the index of x in bucket x_hash        
        if not founded:
        return None
        '''
        
        # Compute the hash value
        x_hash = self.hash_func.cal(x)
        
        # Search the list in bucket x_hash
        try:
            return (x_hash, self.Hash_Table[x_hash].index(x))
        except:
            return (None, None)
        
    def insert(self, x):
        '''Insert x into Chaining Hash Table
        
        Args:
        - x: int, the element to be inserted
        '''
        
        # Compute the hash value
        x_hash = self.hash_func.cal(x)
        
        # Insert X into bucket x_hash at the head
        self.Hash_Table[x_hash].insert(0, x)
        
    def delete(self, x):
        '''Delete x from Chaining Hash Table
        
        Args:
        - x: int, the element to be inserted
        '''
        (bucket, idx) = self.search(x)
        if idx is None:
            raise Exception("Error! X is not is hash table")
        del self.Hash_Table[bucket][idx]