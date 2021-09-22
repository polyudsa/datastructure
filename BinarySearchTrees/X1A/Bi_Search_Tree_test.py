import sys
sys.path.append('../../TreeTraversals/X1A/')

from DF_tree_traversal import DF_tree_traversal
from Bi_Search_Tree import Bi_Search_Tree

# Create an binary search tree
BST = Bi_Search_Tree()
for i in [15, 9, 18, 7, 13, 16, 19, 8]:
    BST.insert(i)

# Preorder deep-first tree traversal
print('Original tree:')
DF_tree_traversal(BST, order='preorder')

# Insert a new node
BST.insert(14)
assert BST.root.left.right.right.value == 14
print('\nInsert 14:')
DF_tree_traversal(BST, order='preorder')

# Minimum of tree
assert BST.minimum().value == 7
print('\nMinimum is: ', BST.minimum().value)

# Find the successor
assert BST.successor(15).value == 16
print('\nSuccessor of 15 is: ', BST.successor(15).value)

# Delete the node
BST.delete(9)
assert BST.root.left.value == 13
print('\nDelete node 9:')
DF_tree_traversal(BST, order='preorder')