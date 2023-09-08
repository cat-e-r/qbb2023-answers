#!/usr/bin/env python

#EXERCISE 5

def mean_min_max_dictionary(X, file_name):
    data = open(file_name)
    inflammation = data.readlines()
    patient = inflammation[X]
    print(patient)
    patient_clean = patient.strip()
    patient_split = patient_clean.split(",")
    days_int = []
    for day in patient_split:
        days_int.append(int(day))
    patient_mean = sum(days_int)/len(days_int)
    patient_min = 100
    for i in days_int:
        if days_int[i] < patient_min:
            patient_min = days_int[i]
    patient_max = 0
    for i in days_int:
        if days_int[i] > patient_max:
            patient_max = days_int[i]

    patient_mean_min_max = {}
    patient_mean_min_max["mean"] = patient_mean
    patient_mean_min_max["min"] = patient_min
    patient_mean_min_max["max"] = patient_max
    return patient_mean_min_max

print(mean_min_max_dictionary(25, "inflammation-01.csv"))




