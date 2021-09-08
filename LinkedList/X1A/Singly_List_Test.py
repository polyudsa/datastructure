from Singly_List import Singly_List

# Insert node to the head of Singly Linked List
# [head] 0 -> 1 -> 2 -> [None]
mylist = Singly_List()
print('Insert node to the head of Singly Linked List')
mylist.insert_first(2)
mylist.insert_first(1)
mylist.insert_first(0)
print('The list is:')
mylist.print_list()
print('Length is: ', mylist.len)

# Insert 30 at index 2
# [head] 0 -> 1 -> 30 -> 2 -> [None]
print('\nInsert 30 at index 2:')
mylist.insert(30, 2)
mylist.print_list()

# Insert 40 to the head
# [head] 40 -> 0 -> 1 -> 30 -> 2 -> [None]
print('\nInsert 40 to the head:')
mylist.insert(40, 0)
mylist.print_list()

# Insert 50 to the tail
# [head] 40 -> 0 -> 1 -> 30 -> 2 -> 50 -> [None]
print('\nInsert 50 to the tail:')
mylist.insert(50, -1)
mylist.print_list()

# Delete index 2
# [head] 40 -> 0 -> 30 -> 2 -> 50 -> [None]
print('\nDelete index 2:')
mylist.delete(2)
mylist.print_list()

# Delete the head
# [head] 0 -> 30 -> 2 -> 50 -> [None]
print('\nDelete the head:')
mylist.delete(0)
mylist.print_list()

# Delete the tail
# [head] 0 -> 30 -> 2 -> [None]
print('\nDelete the tail:')
mylist.delete(-1)
mylist.print_list()