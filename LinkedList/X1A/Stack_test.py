from Stack import Stack

# Create a stack
s = Stack(LEN=7)
s.Push(1)
s.Push(2)
s.Push(3)
assert s.data == [1, 2, 3, None, None, None, None]
print('Original data:\n', s.data)
print('Top index:', s.top)
print('Length:', s.LEN)

s.Push(100)
assert s.data == [1, 2, 3, 100, None, None, None]
print('\nPush 100:\n', s.data)
print('Top index:', s.top)
print('Length:', s.LEN)

assert s.Top() == 100
assert s.data == [1, 2, 3, 100, None, None, None]
print('\nTop, return:', s.Top(), '\n', s.data)
print('Top index:', s.top)
print('Length:', s.LEN)

s.Pop()
assert s.data == [1, 2, 3, None, None, None, None]
print('\nPop:\n', s.data)
print('Top index:', s.top)
print('Length:', s.LEN)