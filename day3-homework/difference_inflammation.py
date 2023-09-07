#!/usr/bin/env python

#EXERCISE 4
import sys



def my_difference(X, Y, file_name):
    data = open(file_name)
    inflammation = data.readlines()
    patient1 = inflammation[X]
    patient2 = inflammation[Y]
    patient1_clean = patient1.strip()
    patient2_clean = patient2.strip()
    patient1_split = patient1_clean.split(",")
    patient2_split = patient2_clean.split(",")
    p1_days_int = []
    p2_days_int = []
    for day in patient1_split:
        p1_days_int.append(int(day))
    for day in patient2_split:
        p2_days_int.append(int(day))
    diff_vals = []
    for i in range(len(p2_days_int)):
        diff_vals.append(p2_days_int[i] - p1_days_int[i])
    return diff_vals
    

print(my_difference(20, 5, "inflammation-01.csv"))

