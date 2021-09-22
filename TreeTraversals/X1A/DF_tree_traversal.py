def DF_tree_traversal(Binary_Tree, order='preorder'):
    '''Inplementation of Depth-first tree traversal
    
    Args:
    - Binary_Tree: binary tree
    - order: traversal order, default 'preorder'
    
    '''
    if order not in ['preorder', 'inorder', 'postorder']:
        raise Exception("'order' can noly be 'preorder', 'inorder' or 'postorder'")
        
    def preorder(node, indent='-'):
        if node is None:
            return None   
        print(indent+str(node.value))
        indent = '|'+indent
        preorder(node.left, indent=indent)
        preorder(node.right, indent=indent)
        
    def inorder(node):
        if node is None:
            return None
        inorder(node.left)
        print(node.value)
        inorder(node.right)
        
    def postorder(node):
        if node is None:
            return None
        postorder(node.left)
        postorder(node.right)
        print(node.value)
        
    if order == 'preorder':
        preorder(Binary_Tree.root)
    elif order == 'inorder':
        inorder(Binary_Tree.root)
    else:
        postorder(Binary_Tree.root)