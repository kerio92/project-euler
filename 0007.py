#!/usr/bin/env python3
from libs import primes
primegen=primes.prime(100000000)
lastnum=next(primegen)
for i in range(10000):
    lastnum=next(primegen)
print(lastnum)
