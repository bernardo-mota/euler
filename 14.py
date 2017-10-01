"""

837799

real    2m13.318s
user    2m13.160s
sys 0m0.024s


"""



def collatz(n):
    """Given an argument, it returns the numbers of elements its collatz sequence has"""
    counter = 0#Number of terms. Local scope
    while n > 1:

        if n % 2 == 0:#If n is even
            n = n / 2
            counter +=1

        else:#If n is not even
            n = 3*n + 1
            counter += 1

    return counter#Only executes after while loop is over, therefore when n == 1

li = [(0,0)]#Tuple is a placeholder (n, collatz(n))

for i in range(2,10**6):#This range function iterable may be a waste of RAM
    calc = collatz(i)
    if calc > li[-1][-1]:
        li.append((i, calc))# == li.append(i,collatz(i))

print(li[-1][0])
