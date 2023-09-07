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
    
        #patient_split[day]
    #     patient_split = int(patient_split)
    # print(patient_split)




# def my_mean(X, file_name):
#     #X is a row
#     #file_name is a string
#     file_name = sys.argv[1]
#     data = open(file_name)
#     inflammation = data.readlines()

print(my_mean(40, "inflammation-01.csv"))



    

# numbers = []
# for line in data:
#     cleanline = line.rstrip("\n")
#     patient_data = line.split(",")
#     score = int(cleanline)
#     numbers.append(score)

#print(numbers)

#print(my_mean(numbers))