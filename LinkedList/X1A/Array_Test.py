from Array import Array

# Create a new array: [1, 2, 3, 4, 5]
test_list = [1, 2, 3, 4, 5]
a = Array(test_list, CAPACITY = test_list.__len__())
print('Original array:', a.data)
print('Capacity:', a.CAPACITY)
print('Len:', a.len)
assert a.data == test_list
assert a.CAPACITY == a.len == test_list.__len__()

# Delete data at index 2
a.delete(2)
assert a.data == [1, 2, 4, 5, None]
assert a.CAPACITY == 5
assert a.len == 4
print('\nDelete index 2:', a.data)
print('Capacity:', a.CAPACITY)
print('Len:', a.len)

# Insert 100 at last
a.insert(100, -1)
assert a.data == [1, 2, 4, 5, 100]
assert a.CAPACITY == 5
assert a.len == 5
print('\nInsert 100 at last:', a.data)
print('Capacity:', a.CAPACITY)
print('Len:', a.len)

# Find the max
assert a.array_max() == 100
print('\nThe maximum element of array:', a.array_max())