from Hash_Function import *

# Hash Function
# Create (2*k + 5) mod 11
HF = hash_func(a=2, b=5, mod=11)
# Calculate the hash value of 12
assert (HF.cal(12) == 7)

# Linear Probing function
class hash_func_2():
    def __init__(self):
        print('Hash Function: \nh_0(k)=k')
    def cal(self, k):
        return k
    
print('')
HF = hash_func_2()
LP = linear_probing(mod=9, hash_func=HF)
assert(LP.cal(21, 0)==3)

# Quadratic Probing Function
print('')
HF = hash_func(a=1, b=0, mod=11)
QP = quadratic_probing(a=1, b=1, mod=11, hash_func=HF)
assert(QP.cal(12, 0)==1)
assert(QP.cal(44, 4)==9)