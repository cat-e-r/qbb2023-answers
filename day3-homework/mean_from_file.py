#!/usr/bin/env python

#EXERCISE 2
import sys

fname = sys.argv[1]

data = open(fname)

def my_mean(list_a):
    total = 0
    for i in range(len(list_a)):
        total = total + list_a[i]
    return total/len(list_a)

numbers = []
for line in data:
    cleanline = line.rstrip("\n")
    score = int(cleanline)
    numbers.append(score)

#print(numbers)

print(my_mean(numbers))
