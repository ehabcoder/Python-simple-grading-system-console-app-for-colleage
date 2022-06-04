# -*- coding: utf-8 -*-
"""
Created on Fri May 20 11:34:36 2022

@author: "EhabCoder"
"""
from csv import reader
from math import sqrt
import sys

def getGrade(score): 
    if(score>=90): return 'A'
    elif(score>=75 and score < 90): return 'B'
    elif(score>=60 and score < 75): return 'C'
    elif(score>=50 and score < 60): return 'D'
    else: return 'F'
    
def getMinimum(students):
    min = float('inf')
    for row in students:
        if(row[0] == 'id'): continue
        if((int(row[2])+int(row[3]))<min):
            min = (int(row[2])+int(row[3]))
    return min

def getMaximum(students):
    max = 0
    for row in students:
        if(row[0] == 'id'): continue
        if((int(row[2])+int(row[3]))>max):
            max = (int(row[2])+int(row[3]))
    return max
    
def getAverage(students):
    count = 0
    ssum = 0
    for row in students:
        if(row[0] == 'id'): continue
        count += 1
        ssum += int(row[2]) + int(row[3])
    return ssum/count
    
def getStandardDeviation(students):
    Xdash = 0
    count = 0
    for row in students:
        if(row[0] == 'id'): continue
        count += 1
        x = int(row[2]) + int(row[3])
        Xdash += x - getAverage(students)
    withoutRoot =  (Xdash * Xdash) / count
    standard = sqrt(withoutRoot)
    return standard
    
def getVariance(students):
  
    count = 0
    ssum = 0
    for row in students:
        if(row[0] == 'id'): continue
        count += 1
        ssum += ((int(row[2]) + int(row[3])) - getStandardDeviation(students)) ** 2
    variance = ssum 
    return variance
print("############### WELCOME ###############\n")
choice = input("Enter any key to start: ")

while(choice != 8):
    print("############### WELCOME ###############")
    print("1. Show Data.")
    print("2. Cound number of students.")
    print("3. Compute final score.")
    print("4. Compute and show grades.")
    print("5. Column Statics.")
    print("6. Show students of grade A")
    print("7. Search by name.")
    print("8. Exit.")
    print("\n")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        with open('students.csv', 'r') as read_obj:
            csv_reader = reader(read_obj)
            print('[ID, Name, midterm, classwok_grade')
            for row in csv_reader:
                print(row)
        print('\n\n\n\n\n\n')
    elif choice == 2:
        with open('students.csv', 'r') as read_obj:
            csv_reader = reader(read_obj)
            numOfStuents = -1
            for row in csv_reader:
                numOfStuents+=1
            print("The number of stuedents is:" , numOfStuents)
        print('\n\n\n\n\n\n')
    elif choice == 3:
        with open('students.csv', 'r') as read_obj:
            csv_reader = reader(read_obj)
            for row in csv_reader:
                if(row[0] == 'id'): continue
                final = float(row[2]) + float(row[3])
                print('Student', row[1], 'final score: ', final)
        print('\n\n\n\n\n\n')
    elif choice == 4: 
        with open('students.csv', 'r') as read_obj:
            csv_reader = reader(read_obj)
            for row in csv_reader:
                if(row[0] == 'id'): continue
                studGrade = getGrade(int(row[2]) + int(row[3]))
                print(row[0], row[1], 'And Grade is:', studGrade)
        print('\n\n\n\n\n\n')
    elif choice == 5: 
        with open('students.csv', 'r') as read_obj:
            csv_reader = reader(read_obj)
            minGrade = getMinimum(csv_reader)
            print("The minimum grade is: " , minGrade)
        with open('students.csv', 'r') as read_obj:
            csv_reader = reader(read_obj)
            maxGrade =  getMaximum(csv_reader)
            print("The maximum grade is: " , maxGrade)
        with open('students.csv', 'r') as read_obj:
            csv_reader = reader(read_obj)
            average =  getAverage(csv_reader)
            print("The average grade is: " , average)
        with open('students.csv', 'r') as read_obj:
            csv_reader = reader(read_obj)
            stardard =  getStandardDeviation(csv_reader)
            print("The standard diviation is: " , stardard)
        with open('students.csv', 'r') as read_obj:
            csv_reader = reader(read_obj)
            variance = getVariance(csv_reader)
            print("The variance is: " , variance)
        print('\n\n\n\n\n\n')
    elif choice == 6:
        with open('students.csv', 'r') as read_obj:
            csv_reader = reader(read_obj)
            for row in csv_reader:
                if(row[0] == 'id'): continue
                score = int(row[2]) + int(row[3])
                if(getGrade(score) == 'A'):
                    print("Student", row[1], 'got Score of A')
        print('\n\n\n\n\n\n')
    elif choice == 7: 
        found = False
        name = str(input('Please Enter the name that you wanna search for: '))
        with open('students.csv', 'r') as read_obj:
            csv_reader = reader(read_obj)
            for row in csv_reader:
                if(row[1] == name):
                    found = True
                    print('The Student has been found and the details of him is:')
                    print('id:', row[0])
                    print('name:', row[1])
                    print('midterm_grade:', row[2])
                    print('classwork_grade:', row[3])
                    print('Total Grade:', int(row[2]) + int(row[3]))
                    print('Score:', getGrade(int(row[2]) + int(row[3])))
        if(found == False):
            print('Sorry! No Students By This name have been found.')
        print('\n\n\n\n\n\n')
    else: 
        input("Created by EhabCoder...")
        sys.exit("Tanks for using my program.")  
