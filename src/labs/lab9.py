# Author:         Anthony Segura
# ULID/Section:   C00441031 - 002
# lab9.py 

#****************** LAB Average  ******************
def LabAvg(): 

    infile1 = open("C:/Users/Anthony/Desktop/Stoof/CMPS 150/labs/lab9_labGrades.py","r")
    num = eval(input("How many lab grades are in the file? "))

    print("Lab Grades: ", end='')
    sum = 0
    for i in range(num):
        grade = eval(infile1.readline())
        sum = sum + grade
        print(grade,end=' ')

    print()
    avg = sum / num      # computes avg (number between 1 & 10)
    return avg  

#****************** PA Average  ****************** 
def PaAvg():
    infile2 = open("C:/Users/Anthony/Desktop/Stoof/CMPS 150/labs/lab9_paGrades.py","r")
    num = eval(input("How many PA grades are in the file? "))
    

    
#****************** EXAM Average  ****************** 
def ExamAvg():
    infile3 = open("C:/Users/Anthony/Desktop/Stoof/CMPS 150/labs/lab9_examGrades.py","r")
    num = eval(input("How many exam grades are in the file? "))
    
    
 
#****************** MAIN/DRIVER  ******************

def main():

    # main will call each of your average functions to compute each component of overall class avg
    # call the function to compute your LAB average put the return value in the variable labAverage 

    print()
    labAverage = LabAvg()
    labAverage = labAverage / 10   # this is the number of points for labs

    # call other functions and then divide return values by 100 points
    paAverage = paAvg()
    paAverage = paAverage/100

    examAverage = examAvg()
    examAverage = examAverage/100
    
    # compute your OVERALL class average using the weights
    # provided on the lab instruction sheet 
    overallAverage = labAverage*10
    
    # print results
    print()
    print("  Lab Average =", format(labAverage*100,'6.2f'), '%')
    print("   PA Average =", format(paAverage*100,'6.2f'), '%')
    print(" Exam Average =", format(examAverage*100,'6.2f'), '%')
    print("-------------")
    print("Class Average =", format(overallAverage,'6.2f'), '%')
    print()

main()
