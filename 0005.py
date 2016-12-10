#!/usr/bin/env python3
from libs import primes
def uniqify(a,b):
    countsa = dict()
    for i in a:
        countsa[i] = countsa.get(i, 0) +1
    countsb = dict()
    for i in b:
        countsb[i] = countsb.get(i, 0) +1
    counts = dict(countsa)
    for key, value in countsb.items():
        counts[key] = max(counts.get(key, 0), value)
    retlist=[]
    for key, value in counts.items():
        retlist.extend((key,)*value)
    return retlist
factors=[]
for i in range(2,21):
    factors=uniqify(factors,primes.factorOut(i))

final=1
for i in factors:
    final=final*i
print(final)
