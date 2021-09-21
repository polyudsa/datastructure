from Singly_List import Singly_List

def print_list(singly_list):
    # O(n)
    current = singly_list.head
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
            
# Create a new singly list
mylist = Singly_List()
mylist.insert(30, -1)
mylist.insert(10, -1)
mylist.insert(70, -1)
assert_list(mylist, [30, 10, 70])
print('Create new singly list:')
print_list(mylist)

# Insert at the head O(1)
mylist.insert_first(100)
assert_list(mylist, [100, 30, 10, 70])
print('\nInsert 100 at the head:')
print_list(mylist)

# Insert in between O(n)
mylist.insert(200, 3)
assert_list(mylist, [100, 30, 10, 200, 70])
print('\nInsert 200 at index 3:')
print_list(mylist)

# Delete element in between O(n)
mylist.delete(2)
assert_list(mylist, [100, 30, 200, 70])
print('\nDelete element at index 2:')
print_list(mylist)

# Delete element at the tail O(1)
mylist.delete(-1)
assert_list(mylist, [100, 30, 200])
print('\nDelete element at the tail:')
print_list(mylist)