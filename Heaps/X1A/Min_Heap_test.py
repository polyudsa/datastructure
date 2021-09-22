from Min_Heap import Min_Heap

# Create a min heap
a = Min_Heap(CAPACITY=7)
for i in [2, 5, 6, 9, 7]:
    a.insert(i)
print('Original data:\n', a.data)

# Insert a new node
a.insert(1)
assert a.data == [None, 1, 5, 2, 9, 7, 6]
print('\nInsert 1:\n', a.data)

# Delete the minimum node
a.remove_min()
assert a.data == [None, 2, 5, 6, 9, 7, None]
print('\nDelete the minimum node:\n', a.data)

# Minimum value of heap
assert a._min() == 2
print('\nMinimum value:', a._min())

# Maximum value of heap
assert a._max() == 9
print('Maximum value:', a._max())