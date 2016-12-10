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
