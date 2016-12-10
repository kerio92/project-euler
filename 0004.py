#!/usr/bin/env python3
palimdromes=[]
for i in range(100,1000):
    for j in range(i, 1000):
        string=repr(i*j)
        if string[:3] == string[6:2:-1]:
            palimdromes.append(i*j)

print(max(palimdromes))
