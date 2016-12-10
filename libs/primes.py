import math
def prime(hi):
    primes=[2,3,5,7]
    yield 2
    yield 3
    yield 5
    yield 7
    for n in range(8,hi):
        upper=int(math.floor(math.sqrt(n)))
        try:
            for d in [i for i in primes if i <=upper+1]:
                if not n%d:
                    raise Exception
            primes.append(n)
            yield n
        except Exception:
            continue

def factorOut(num):
    for d in prime(max(num,1000)):
        if num == d:
            return [num]
        if not num % d:
            retlist = factorOut(num//d)
            retlist.append(d)
            return retlist
    return [num]


