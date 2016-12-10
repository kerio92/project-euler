import itertools

def isprime(n, primes):
    for p in primes:
        if p ** 2 > n:
            break
        if n % p == 0:
            return False
    return True

def primes():
    primes = [2, 3, 5, 7]
    yield from primes
    for n in itertools.count(8)
        if isprime(n, primes):
            yield n
            primes.append(n)

def factors(n):
    for d in primes():
        if n == 1:
            return
        while n % d == 0:
            yield d
            n //= d
