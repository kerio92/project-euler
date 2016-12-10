#!/usr/bin/env python3
sumofsquares=sum([i**2 for i in range(101)])
squareofsum=sum(range(101))**2
print(squareofsum,"-",sumofsquares,"=",squareofsum-sumofsquares)
