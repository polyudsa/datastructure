from Hash_Function import hash_func, linear_probing, quadratic_probing
from Open_Addressing import Open_Addressing

############################
##### Linear Probing ######
############################
print('############################')
print('##### Linear Probing ######')
print('############################')

# Define simple hash function
class hash_func_2():
    def __init__(self):
        print('Hash Function: \nh_0(k)=k')
    def cal(self, k):
        return k
    
print('')
# Create hash function
HF = hash_func_2()
# Create linear probing function
LP = linear_probing(mod=5, hash_func=HF)
# Create Open Addressing Hash Table
OA = Open_Addressing(size=5, probing_func=LP)

# Insert
print('\nHash Table:')
for i in [293, 598, 308]:
    OA.insert(i)
for (bucket, values) in zip(OA.Hash_Table.keys(), OA.Hash_Table.values()):
    print(bucket, ':', values)

dic = {0: 308, 1: None, 2: None, 3: 293, 4: 598}
assert(OA.Hash_Table==dic)

# Search
assert(OA.search(293)==3)

# Delete
print('\nDelete 393:\nHash Table:')
OA.delete(293)
for (bucket, values) in zip(OA.Hash_Table.keys(), OA.Hash_Table.values()):
    print(bucket, ':', values)

dic = {0: 308, 1: None, 2: None, 3: 'Deleted', 4: 598}
assert(OA.Hash_Table==dic)



############################
#### Quadratic Probing #####
############################
print('\n############################')
print('#### Quadratic Probing #####')
print('############################\n')

# Create hash function
HF = hash_func(a=1, b=0, mod=11)
# Create quadratic probing function
OP = quadratic_probing(a=1, b= 1, mod=11, hash_func=HF)
# Create Open Addressing Hash Table
OA = Open_Addressing(size=11, probing_func=OP)

# Insert
print('\nHash Table:')
for i in [12, 44, 13, 88, 23, 94, 11, 39, 20]:
    OA.insert(i)
    
for (bucket, values) in zip(OA.Hash_Table.keys(), OA.Hash_Table.values()):
    print(bucket, ':', values)

dic = {0: 44,
 1: 12,
 2: 13,
 3: 23,
 4: 20,
 5: None,
 6: 88,
 7: 39,
 8: 94,
 9: 11,
 10: None}
assert(OA.Hash_Table==dic)