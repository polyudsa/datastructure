import numpy as np
from Chaining import Chaining
from Hash_Function import hash_func

# Define the hash function
HF = hash_func(a=2, b=5, mod=11)


# Create a Chaining Hash Table
size = 11
HT = Chaining(size=size, hash_func=HF)

# Insert new element
keys = [12, 44, 13, 88, 23, 94, 11, 39, 20, 16]
for k in keys:
    HT.insert(k)

print('keys:', keys, '\nHash Table:')
for (bucket, values) in zip(HT.Hash_Table.keys(), HT.Hash_Table.values()):
    print(bucket, ':', values)


dic = {0: [],
 1: [20],
 2: [],
 3: [],
 4: [16],
 5: [11, 88, 44],
 6: [39, 94],
 7: [23, 12],
 8: [],
 9: [13],
 10: []}
assert(HT.Hash_Table == dic)

# Search for element
(bucket, idx) = HT.search(88)
print('\nSearch\n88 in bucket:',bucket, 'with index:', idx)
assert(HT.search(88) == (5, 1))

# Delete element
HT.delete(88)
print('\nDelete 88:')
for (bucket, values) in zip(HT.Hash_Table.keys(), HT.Hash_Table.values()):
    print(bucket, ':', values)

dic = {0: [],
 1: [20],
 2: [],
 3: [],
 4: [16],
 5: [11, 44],
 6: [39, 94],
 7: [23, 12],
 8: [],
 9: [13],
 10: []}
assert(HT.Hash_Table == dic)