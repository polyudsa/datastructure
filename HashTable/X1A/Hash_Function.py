import numpy as np

class hash_func():
    '''Implementation of hash function
    h_0(k) = (a * k + b) mod [mod]
    
    Args:
    - a: int, coefficient of hash function
    - b: int, constant of hash function
    - mod: int, quotient of hash function
    
    Attributes:
    - a: int, coefficient of hash function
    - b: int, constant of hash function
    - mod: int, quotient of hash function
    '''
    
    def __init__(self, a, b, mod):
        self.a = a
        self.b = b
        self.mod = mod
        print('Hash Function:\nh_0(k) = ({}k+{}) mod {}'.format(a, b, mod))
        
    def cal(self, k):
        ''' Calculate the hash value
        Args:
        - k: int, divided number
        
        Return:
        - hash_value: int, hash value of k
        '''
        return np.mod(self.a*k + self.b, self.mod)
    

class linear_probing():
    '''Implementation of linear probing function
    h(k, i) = [h_0(k) + i] mod [mod]
    where h_0(k) = (a * k + b) mod [mod]
    
    Args:
    - mod: int, quotient of quadratic probing function
    
    Attributes:
    - mod: int, quotient of quadratic probing function
    '''
    
    def __init__(self, mod, hash_func):
        self.mod = mod
        self.hash_func = hash_func
        print('Linear Probing function:')
        print('h(k, i) = [h_0(k) + i] mod {}'.format(mod))
    
    def cal(self, k, i):
        ''' Calculate the hash value
        Args:
        - i: int, the number of collision
        - k: int, divided number
        
        Return:
        - hash_value: int, hash value of k
        '''
        h0 = self.hash_func.cal(k)        
        return np.mod(h0+i, self.mod)

    
class quadratic_probing():
    '''Implementation of quadratic probing function
    h(k, i) = [h_0(k) + ai + bi^2] mod [mod]
    where h_0(k) = (a * k + b) mod [mod]
    
    Args:
    - a: int, coefficient of quadratic probing function
    - b: int, constant of quadratic probing function
    - mod: int, quotient of quadratic probing function
    
    Attributes:
    - a: int, coefficient of quadratic probing function
    - b: int, constant of quadratic probing function
    - mod: int, quotient of quadratic probing function
    '''
    
    def __init__(self, a, b, mod, hash_func):
        self.a = a
        self.b = b
        self.mod = mod
        self.hash_func = hash_func
        print('Quadratic Probing function:')
        print('h(k, i) = [h_0(k) + {}i + {}i^2] mod {}'.format(a, b, mod))
        
    def cal(self, k, i):
        ''' Calculate the hash value
        Args:
        - i: int, the number of collision
        - k: int, divided number
        
        Return:
        - hash_value: int, hash value of k
        '''
        h0 = self.hash_func.cal(k)   
        return np.mod( h0 + self.a*i + self.b*i**2, self.mod)