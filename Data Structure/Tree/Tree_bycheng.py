class TreeNode(object):
    def __init__(self,name, parent=None):
        super(TreeNode, self).__init__()
        self.parent = parent
        self.name = name
        self.child = {}

    def __repr__(self):
        return("name:%s"%self.name)

    def __contains__(self,item):
        return item in self.children
    
    @property
    def path(self):
        """return path (from root to current node)
            recurrance print path"""
        if self.parent:
            return "%s %s" % (self.parent.path.strip(), self.name)
        else:
            return self.name
    
    def get_child(self, name, defval=None):
        """get a childnode of current node"""
        return self.child.get(name, defval)
    
    def add_child(self, name, obj=None):
        """add a childnode of current node"""
        if obj and not isinstance(obj,TreeNode):
            raise ValueError("only can add treenode to the tree")
        if obj is None:
            obj = TreeNode(name)
        obj.parent = self
        self.child[name] = obj
        return obj
    
    def del_child(self, name):
        """remove a treenode from the current node"""
        if name in self.child:
            del self.child[name]
        
    def find_child(self, path, create=False):
        """"find child by path/name, return None if not found"""
        path = path if isinstance(path, list) else path.split()
        cur = self
        for sub in path:
            # search
            obj = cur.get_child(sub)
            if obj is None and create:
                # create new node if needed
                obj = cur.add_child(sub)
            if obj is None:
                break
            cur = obj
        return obj
    
    def items(self):
        return self.child.items()
    
    def dump(self, indent=0):
        """dump tree to String"""
        tab = '   '*(indent - 1) + '|-' if indent > 0 else ''
        print('%s%s'%(tab, self.name))
        for name, obj in self.items():
            # recurrence produce tree
            obj.dump(indent+1)

if __name__ == '__main__':
    print('test add_child()') 
    root = TreeNode('')
    a1 = root.add_child('a1')
    a1.add_child('b1') 
    a1.add_child('b2')
    a2 = root.add_child('a2')
    a2.add_child('c1')
    root.dump()      
        


