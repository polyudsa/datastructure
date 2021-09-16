class BinaryTree(object):
    def __init__(self, rootobj):
        self.key = rootobj
        self.left_children = None
        self.right_children = None
        self.parent = None
    
    def insert_left(self, name=None, node=None):
        if name is not None and node is None:
            node = BinaryTree(name)
        elif not isinstance(self.node, BinaryTree):
            raise ValueError("Please insert into Tree object")
        else:
            node = node
        
        if self.left_children is not None:
            # 在parent和其child中间插入
            node.left_children = self.left_children
            self.left_children.parent = node
            self.left_children = node
            node.parent = self
        else:
            self.left_children = node
            node.parent = self
    
    def insert_right(self, name=None, node=None):
        if name is not None and node is None:
            node = BinaryTree(name)
        elif not isinstance(self.node, BinaryTree):
            raise ValueError("Please insert into Tree object")
        self.right_children = node

        if self.right_children is not None:
            # 在parent和其child中间插入
            node.right_children = self.left_children
            self.right_children.parent = node
            self.right_children = node
            node.parent = self
        else:
            self.right_children = node
            node.parent = self
    
    def get_left(self):
        print(self.left_children.key)
    
    def get_right(self):
        print(self.right_children.key)
    
    def set_root(self, name):
        self.key = name
    
    def peek_root(self):
        print(self.key)

if __name__ == "__main__":
    tree = BinaryTree('c')
    tree.insert_right('m')
    tree.insert_left('n')
    tree.insert_left('x')
    tree.get_left()

    