#!/usr/bin/env python
import numpy #as np #this imports useful external functions, and allows you to refer to it as np
f = open("/Users/cmdb/Desktop/swc-python/data/inflammation-01.csv", "r")
patients = f.readlines()
# print(type(patients))
# print(patients)

#-----------------------------------------------------------
#EXERCISE 1 - flare-ups of 5th patient on 1st, 10th, and last day

# patients is a list of strings where each value is separated by a comma, each string is a patient
# Goal: get rid of the \n at the end of each patient string
# Goal: split the lists at the commas

index = 0 #start a variable to iterate throgh and modify the items WITHIN the existing list

for patient in patients:
	patient = patient.rstrip() #gets rid of \n at the end of the patient string and stores it as the new patient
	patient = patient.split(",") #splits the string at the commas and stores it as the new patient
	patients[index] = patient #updates the item in the existing list with the stripped and split string
	index = index + 1 #steps to the next index for the next iteration of the for loop


# print(patients)

print('ANSWERS Ex 1')
print(patients[4][0]) #number of flare-ups, 5th patient, 1st day
#0
print(patients[4][9]) #number of flare-ups, 5th patient, 10th day
#4
print(patients[4][-1]) #number of flare-ups, 5th patient, last day
#1

#--------------------------------------------------------------
#EXERCISE 2 - average of patient flare-ups over total days

#Goal: make a list of integers so we can do mathematical operations on the list items

patients_int = [] #start an empty list to store each patient's integers in
for patient in patients:
	patient_int = [] #start a list to store each integer for each day in
	for day in patient:
		day = int(day) #update each item in the list as an integer
		patient_int.append(day) #add the integer as the next item in this patient's list
	patients_int.append(patient_int) #add this patient's integer list as the next item in the list for all patients

#print(patients_int)

#Goal: find the average flare-ups for patient 1, then, 2, then 3, etc. up to 10

print('ANSWERS Ex 2')
for patient in patients_int[0:10]:
	avg_flare = numpy.mean(patient) #find the mean of the integer list for each of the first 10 patients
	print(avg_flare)
#5.45
#5.425
#6.1
#5.9
#5.55
#6.225
#5.975
#6.65
#6.625
#6.525

#--------------------------------------------------------------
#EXERCISE 3 - of all the patient averages calculated above which are the highest and lowest?

#Goal: make a list of patient averages

patient_avgs = [] #create an empty list to store each patient's average in

for patient in patients_int[0:10]:
	avg_flare = numpy.mean(patient) #find the average for each patient
	patient_avgs.append(avg_flare) #add the average as the next item in the averages list

print('ANSWERS Ex 3')
print(numpy.max(patient_avgs)) #print the max value in the list of ten averages
#6.65
print(numpy.min(patient_avgs)) #print the min value in the list of ten averages
#5.425

#----------------------------------------------------------------
#EXERCISE 4 - flare-up difference between patient 1 and 5 on each day

print('ANSWERS Ex 4')
diff_1_5 = [] #create an empty list to store the differences in
for i in range(len(patients_int[0])): #for each item in the range of each list
	diff_1_5.append(patients_int[0][i] - patients_int[4][i]) #store the value that is at this index for patient 1 minus that of patient 5

print(diff_1_5)
"""
[0, -1, 0, 0, -2, 1, 1, 2, 6, -1, -1, -4, 4, 0, 4, -6, -1, -3, 6, 1, -3,
 -1, 2, 4, -6, -2, -8, 0, 1, 1, -5, -2, 2, 5, 1, 0, 0, 3, -1, -1]
"""





