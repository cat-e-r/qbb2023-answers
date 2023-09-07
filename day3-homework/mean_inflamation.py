#!/usr/bin/env python

#EXERCISE 3
import sys



def my_mean(X, file_name):
    data = open(file_name)
    inflammation = data.readlines()
    patient = inflammation[X]
    patient_clean = patient.strip()
    patient_split = patient_clean.split(",")
    days_int = []
    for day in patient_split:
        days_int.append(int(day))
    return sum(days_int)/len(days_int)
    

print(my_mean(40, "inflammation-01.csv"))
