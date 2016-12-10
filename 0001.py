#!/usr/bin/env python3
def multiples(hi, divisors):
    for i in range(hi):
        for d in divisors:
            if not i % d:
                yield i
                break

print(sum(multiples(1000, [3,5])))
