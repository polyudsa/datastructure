import numpy as np
from numpy.linalg import matrix_power

def power_n(x, n):
    if n == 1:
        return x
    else:
        if n % 2 == 0:
            sub = power_n(x,n/2)
            return sub ** 2 

        else:
            sub = power_n(x,(n-1)/2)
            return sub ** 2 * x

def fabonacci(n):
    """Returns the nth fabonacci number"""
    i = np.matrix([[1,1], [1,0]])
    return matrix_power(i, n)


if __name__ == '__main__':
    print(power_n(2, 5))
    print(fabonacci(5))