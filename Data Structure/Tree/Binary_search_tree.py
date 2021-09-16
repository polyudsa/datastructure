class Node(object):
    def __init__(self, value):
        self.value = value
        self.right_child = None
        self.left_child = None
        self.parent = None
        self.successor = None
    
    def Minimum(self):
        """遍历找到从self结点出发的最小值"""
        min = self
        while min.left_child is not None:
            min = min.left_child
        return min.value
    
    def _successor(self):
        """隐藏方法"""
        """找到比当前结点稍大的继任者"""
        min_max = self
        if self.right_child is not None:
            return self.right_child.Minimum()
        else:
            while min_max.parent is not None and min_max.parent.right_child == self:
                min_max = min_max.parent
            return min_max

    def insert(self, value):
        new_node = Node(value)
        if value > self.value:
            if self.left_child == None:
                self.left_child = new_node
                new_node.parent = self
            else:
                self.left_child.insert(value)
        elif value == self.value:
            print("no duplicated value is allowed")
            return
        else:
            if self.right_child == None:
                self.right_child = new_node
                new_node.parent = self
            else:
                self.right_child.insert(value)
        
    def delete(self, value):
        if self.right_child == None and self.left_child == None:
            if self.parent.left_child == self:
                self.parent.left_child = None
            else:
                self.parent.right_child = None
        if self.right_child is not None or self.right_child is not None:
            if self.right_child is not None:
                self.parent.right_child = self.right_child
            if self.left_child is not None:
                self.parent.left_child = self.left_child
        if self.right_child != None and self.left_child != None:
            self = self._successor()
    
    def find_value(self, value):
        if self.value == value:
            print("Founded")
        elif self.value < value:
            if self.left_child is None:
                print("Unfounded")
            else:
                return self.left_child.find_value(value)
        elif self.value > value:
            if self.right_child is None:
                print("Unfounded")
            else:
                return self.right_child.find_value(value)
        
    def Print_Tree(self):
        if self.left_child is None and self.right_child is None:
            print(self.value)
        if self.left_child != None:
            self.left_child.Print_Tree()
        if self.right_child != None:
            self.right_child.Print_Tree()




if __name__ == "__main__":
    root = Node(12)
    root.insert(6)
    root.insert(14)
    root.insert(3)
    print(root.find_value(7))
    print(root.find_value(14))
    root.Print_Tree()
