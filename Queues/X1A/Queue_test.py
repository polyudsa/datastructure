from Queue import Queue

# Create a queue
q = Queue(LEN=7)
q.Enqueue(1)
q.Enqueue(2)
q.Enqueue(3)
q.Enqueue(4)
q.Enqueue(5)
assert q.data == [1, 2, 3, 4, 5, None, None]
assert q.head == 1
assert q.tail == 6
assert q.is_empty() == False
assert q.is_full() == False
print('Original data:\n', q.data)
print('Head position:', q.head)
print('Tail position:', q.tail)
print('Empty:', q.is_empty())
print('Full:', q.is_full())


q.Enqueue(100)
assert q.data == [1, 2, 3, 4, 5, 100, None]
print('\nEnqueue 100:\n', q.data)
print('Head position:', q.head)
print('Tail position:', q.tail)
print('Empty:', q.is_empty())
print('Full:', q.is_full())


q.Dequeue()
assert q.data == [None, 2, 3, 4, 5, 100, None]
print('\nDequeue :\n', q.data)
print('Head position:', q.head)
print('Tail position:', q.tail)
print('Empty:', q.is_empty())
print('Full:', q.is_full())


q.Enqueue(100)
assert q.data == [None, 2, 3, 4, 5, 100, 100]
print('\nEnqueue 100:\n', q.data)
print('Head position:', q.head)
print('Tail position:', q.tail)
print('Empty:', q.is_empty())
print('Full:', q.is_full())