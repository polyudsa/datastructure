class Bi_node:
    '''Implementation of binary search tree node
    
    Args:
    - value: int, the value of binary search tree node
    
    Attributes:
    - value: int, the value of binary search tree node
    - left: Bi_node, left node of this node, default None
    - right: Bi_node, right node of this node, default None
    - prev: Bi_node, parent node of this node, default None
    
    '''
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.prev = None

        
class Bi_Search_Tree:
    '''Implementation of binary search tree
        
    Attributes:
    - root: Bi_node, the root node of binary search tree
    
    '''
    
    def __init__(self):
        self.root = None
        
    
    def search(self, value):
        # O(h)
        '''Determine whether the value is in the tree
        
        Return: 
        - Bi_node, if the node of value is found, otherwise False
        
        '''
        temp = self.root
        while temp is not None:
            if value == temp.value:
                return temp
            elif value < temp.value:
                temp = temp.left
            else:
                temp = temp.right
        return False
            
    
    def insert(self, value):
        # O(h)
        '''Insert a new node at the bottom of the tree
        
        Args:
        - value: int, the value of new node
        
        Return: 
        - None
        
        '''
        temp = self.root
        
        # 1. find a place for inserting new node
        while temp is not None: 
            prev = temp                  # find the parent node of new node
            if value < temp.value:       # go left if smaller  
                temp = temp.left        
            elif value > temp.value:     # go right if bigger
                temp =temp.right        
            else:                        # do not allow duplicate value
                return None
        
        # 2. insert new value into leaf node
        if self.root is None:            # if tree is empty
            self.root = Bi_node(value)   # -> make new node as the root node
        elif value < prev.value:         # if new value is smaller than leaf node
            prev.left = Bi_node(value)   # -> make new node as the left node of leaf node
            prev.left.prev = prev        # -> assign new node's parent node
        else:                            # if new value is bigger than leaf node
            prev.right = Bi_node(value)  # -> make new node as the right node of leaf node
            prev.right.prev = prev       # -> assign new node's parent node
            
            
    def minimum(self, subtree_value=None):
        '''Find the minimal value of the tree
        
        Args:
        - subtree_value: int, value of subtree root node, default None(the whole tree)
        
        Return: 
        - Bi_node, the minimal node of the tree(subtree)
        
        '''
        if subtree_value is None:             # search the whole tree
            temp = self.root
        else: 
            temp = self.search(subtree_value) # find the subtree
            
        # go left all the way
        while temp.left is not None:
            temp = temp.left
        return temp
    
    
    def successor(self, value):
        '''Find the successor node of the value
        
        Args:
        - value: int, the value of the node
        
        Return: 
        - Bi_node, return the successor node if found, otherwise None
        
        '''
        
        # 1. find the node of value
        temp = self.search(value)
        if temp is False:
            raise Exception("The value is not in the tree")
                
        # 2. find the successor
        # 2.1 if the node have right subtree
        #     -> successor is the minimum of right subtree
        if temp.right is not None:           
            return self.minimum(temp.right.value)
        
        # 2.2 if the node don't have right subtree
        while (temp.prev is not None) and (temp == temp.prev.right):
            temp = temp.prev
        return temp.prev
        
        
    def delete(self, value):
        '''Delete the node of the value
        
        Args:
        - value: int, the value of the node
        
        Return:
        - None
        
        '''
        # 1. find the node of value
        temp = self.search(value)
        if temp is False:
            raise Exception("The value is not in the tree")
            
        # 2. delelte the node
        # 2.1 if the node has no child, simply delete the node
        if (temp.left==None) and (temp.right==None):
            if temp is self.root:             # if there is only one root node in the tree
                self.root = None              # delete the root node
                return None
            if temp.prev.left == temp:
                temp.prev.left = None
            else:
                temp.prev.right = None   
                           
                    
        # 2.2 if the node has one child, replace it by it's child
        elif (temp.left==None) or (temp.right==None):
            child = temp.left if temp.left is not None else temp.right
            child.prev = temp.prev
            if temp is not self.root:
                if temp==temp.prev.left:
                    temp.prev.left = child 
                else:
                    temp.prev.right = child
            else:
                self.root = child
            
            
        # 2.3 if the node has two children, replace it by it's successor
        else:
            # 2.3.1 find the successor
            successor = self.successor(value)
            
            # special case: successor.prev is temp
            # (to be more specify, successor is the right child of the temp)
            if successor.prev is temp:
                successor.prev = temp.prev
                successor.left = temp.left
                if temp is not self.root:
                    if temp.prev.left == temp:
                        temp.prev.left = successor
                    else:
                        temp.prev.right = successor
                else:
                    self.root = successor
                    
            else:
                # 2.3.2 take the successor out of the tree
                # successor can only have a right child node
                if successor.right is not None:                
                    successor.right.prev = successor.prev  
                # successor must on it's parent's left side
                successor.prev.left = successor.right  
                
                # 2.3.3 replace the node by the successor
                # connect successor with temp's left node
                successor.left = temp.left
                temp.left.prev = successor
                # connect successor with temp's right node
                successor.right = temp.right
                temp.right.prev = successor
                # connect successor with temp's parent node
                if temp is not self.root:
                    if temp.prev.left == temp:
                        temp.prev.left = successor
                    else:
                        temp.prev.right = successor
                else:
                    self.root = successor