#!/usr/bin/env python

from random import randint
allNums = []

for eachNum in range(9):
    allNums.append(randint(1,99))
print allNums
print [n for n in allNums if n%2]
