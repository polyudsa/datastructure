from Doubly_List import Doubly_List

# Insert node to the head of Doubly Linked List
# [head] 0 <-> 1 <-> 2 [Tail]
mylist = Doubly_List()
print('Insert node to the head of Doubly Linked List')
mylist.insert_first(2)
mylist.insert_first(1)
mylist.insert_first(0)
print('The list is:')
mylist.print_list()
print('Length is: ', mylist.LEN)

# Insert 30 at index 2
# [head] 0 <-> 1 <-> 30 <-> 2 [Tail]
print('\nInsert 30 at index 2:')
mylist.insert(30, 2)
mylist.print_list()

# Insert 40 to the head
# [head] 40 <-> 0 <-> 1 <-> 30 <-> 2 [Tail]
print('\nInsert 40 to the head:')
mylist.insert(40, 0)       # or mylist.insert_first(40) 
mylist.print_list()

# Insert 50 to the tail
# [head] 40 <-> 0 <-> 1 <-> 30 <-> 2 <-> 50 [Tail]
print('\nInsert 50 to the tail:')
mylist.insert(50, -1)       # or mylist.insert_last(50) 
mylist.print_list()

# Delete index 2
# [head] 40 <-> 0 <-> 30 <-> 2 <-> 50 [Tail]
print('\nDelete index 2:')
mylist.delete(2)
mylist.print_list()

# Delete the head
# [head] 0 <-> 30 <-> 2 <-> 50 [Tail]
print('\nDelete the head:')
mylist.delete(0)            # or mylist.delete_first()
mylist.print_list()

# Delete the tail
# [head] 0 <-> 30 <-> 2 [Tail]
print('\nDelete the tail:')
mylist.delete(-1)            # or mylist.delete_last()
mylist.print_list()