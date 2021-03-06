#!/usr/bin/env python3
#Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
#1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
#By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
def fib(hi):
    a,b = 1,1
    while a <= hi:
        yield a
        a,b=b,a+b

val=0
for i in list(fib(4000000)):
    if not i % 2:
        val += i

print(val)
