# Various implementations of dynamic programming algorithms
import numpy as np

# Fibonacci

def rec_fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return rec_fib(n-1) + rec_fib(n-2)

def dp_fib(n):
    F = np.zeros(n)
    F[0] = 0
    F[1] = 1
    for i in range(n):
        if i >= 2:
            F[i] = F[i-1] + F[i-2]
    return F[n-1]

# Longest increasing subsequece

def dp_lis(arr):
    return 0
