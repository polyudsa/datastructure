from Array import Array

# Create a new array: [1, 2, 3, 4, 5]
test_list = [1, 2, 3, 4, 5]
a = Array(test_list, capacity=test_list.__len__())
assert test_list==a.data
assert test_list.__len__()==a.capacity==a.logical_size

print('Origin array is: ')
print(a.data)
print('Logical size is: ', a.logical_size)
print('Physical size is ', a.capacity)


print('\n+++++++++++++++++++++++')
print('++++++ Insertion ++++++')
print('+++++++++++++++++++++++')

# Insert 5 at the head
print('\nInsert 5 at the head')
print('Before: ', a.data)
a.insert(5, 0)
print('After:  ', a.data)
print('Logical size is: ', a.logical_size)
print('Physical size is ', a.capacity)

# Insert 9 at the tail
print('\nInsert 9 at the tail')
print('Before: ', a.data)
a.insert(9, 6)
print('After:  ', a.data)
print('Logical size is: ', a.logical_size)
print('Physical size is ', a.capacity)

# Double the capacity if the capacity is full at the time of insertion
print('\nDouble the capacity if the capacity is full at the time of insertion')
print('Insert 10 at the tail')
print('Before: ', a.data)
a.insert(10, 7)
print('After:  ', a.data)
print('Logical size is: ', a.logical_size)
print('Physical size is ', a.capacity)


print('\n++++++++++++++++++++++++')
print('+++++++ Deletion +++++++')
print('++++++++++++++++++++++++')

# Delete the head
print('\nDelete the head')
print('Before: ', a.data)
a.delete(0)
print('After:  ', a.data)
print('Logical size is: ', a.logical_size)
print('Physical size is ', a.capacity)

# Delete the tail
print('\nDelete the tail')
print('Before: ', a.data)
a.delete(6)
print('After:  ', a.data)
print('Logical size is: ', a.logical_size)
print('Physical size is ', a.capacity)

# When logical size <= capacity // 4, reducing the capacity to one-half
print('\nWhen logical size <= capacity // 4, reducing the capacity to one-half')
a.delete(0)
a.delete(0)
print('Before: ', a.data)
a.delete(0)
print('After:  ', a.data)
print('Logical size is: ', a.logical_size)
print('Physical size is ', a.capacity)