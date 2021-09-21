from Doubly_List import Doubly_List

def print_list(douly_list):
    # O(n)
    current = douly_list.head
    while current is not None:
        print(current.data)
        current = current.next
        
def assert_list(test_list, true_list):
    current = test_list.head
    i = 0
    while current is not None:
        assert current.data == true_list[i]
        current = current.next
        i += 1
        
        
# Create a new doubly list
mylist = Doubly_List()
mylist.insert_last(7)
mylist.insert_last(0)
mylist.insert_last(4)
mylist.insert_last(9)
mylist.insert_last(15)

assert_list(mylist, [7, 0, 4, 9, 15])
print('Create new doubly list:')
print_list(mylist)

# 'head', 'tail', 'next' and 'prev'
assert mylist.head.data == 7
print('\nThe head of doubly list is:', mylist.head.data)
assert mylist.tail.data == 15
print('The tail of doubly list is:', mylist.tail.data)
assert mylist.head.next.data == 0
print('The next node of head is:', mylist.head.next.data)
assert mylist.tail.prev.data == 9
print('The previous node before tail is:', mylist.tail.prev.data)

# Insert at the head O(1)
mylist.insert_first(100)
true_list = [100, 7, 0, 4, 9, 15]
assert_list(mylist, true_list)
print('\nInsert 100 at the head:')
print_list(mylist)

# Insert at the tail O(1)
mylist.insert_last(200)
true_list = [100, 7, 0, 4, 9, 15, 200]
assert_list(mylist, true_list)
print('\nInsert 200 at the tail:')
print_list(mylist)

# Insert in between O(n)
mylist.insert(300, 3)
true_list = [100, 7, 0, 300, 4, 9, 15, 200]
assert_list(mylist, true_list)
print('\nInsert 300 at index 3:')
print_list(mylist)

# Delete at the head O(1)
mylist.delete_first()
true_list = [7, 0, 300, 4, 9, 15, 200]
assert_list(mylist, true_list)
print('\nDelete the head:')
print_list(mylist)

# Delete at the tail O(1)
mylist.delete_last()
true_list = [7, 0, 300, 4, 9, 15]
assert_list(mylist, true_list)
print('\nDelete the tail:')
print_list(mylist)


# Delete in between O(n)
mylist.delete(4)
true_list = [7, 0, 300, 4, 15]
assert_list(mylist, true_list)
print('\nDelete the element at index 4:')
print_list(mylist)