from math import factorial

def nCr(n,r):
    """nCr(n,r) = n!/((n-r)!*r!), for all positive integers n and r where n >= r
       A lazy combinations function
       For a more efficent algorithm use gmpy2.comb(n,r)"""
    res = factorial(n)//(factorial(n-r)*factorial(r))

    return res

def lattice_paths(x,y):
    """Going from position (0,0) --> (k, n-k)
       There are nCr(n+k,k) lattice paths"""

    k = x
    n = x + y

    return nCr(n,k)

print(lattice_paths(20,20))
