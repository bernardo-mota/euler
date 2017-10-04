#!/bin/env python3
#I used gmpy2, for that I had to manually install to C libraries libmpc3 and mpfr

from gmpy2 import comb


counter = 0

for a in range(1,101):
    for b in range(1,101):
        try:
            if comb(a,b) > 10**6:
                counter +=1

        except:
            pass

print(counter)
