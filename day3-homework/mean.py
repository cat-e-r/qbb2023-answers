#!/usr/bin/env python

#EXERCISE 1
def my_mean(list_a):
    total = 0
    for i in range(len(list_a)):
        total = total + list_a[i]
    return total/len(list_a)

a = [2, 5, 6, 1, 9, 2]

print(my_mean(a))




