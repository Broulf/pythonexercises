# Author:          Anthony Segura
# ULID:            C00441031
# Course/Section:  CMPS 150 – 002
# Assignment:      pa7 
# Date Assigned:   Sunday, November 21, 2021 
# Date/Time Due:   Monday, November 29, 2021 –- 11:55 pm 
# 
# Description:    This program reads an answer key and student answers from input  
#   files and stores the data in two lists. The solutions are  
#   compared to the key and various statistics computed.   
# 
# Certification of Authenticity: 
# I certify that this assignment is entirely my own work.

from PrintAnswerHeader import PrintAnswerHeader

def main():

    # Opens the files
    #key_file = open("C:/Users/Anthony/Desktop/Stoof/CMPS 150/pythongit/src/pas/key.txt", "r")
    #student_file = open("C:/Users/Anthony/Desktop/Stoof/CMPS 150/pythongit/src/pas/studentAnswers.txt", "r")
    key_file = open("key.py", "r")
    student_file = open("studentAnswers.py", "r")

    # Lists
    key_list = key_file.read().splitlines()
    student_list = student_file.read().splitlines()

    # Removes the X because I'm lazy/dumb and it's 3am on the 23rd
    key_list.remove("X")
    student_list.remove("X")

    # Storage Values!!!
    correct = 0
    correct_list = []
    incorrect = 0
    incorrect_list = []
    true_answers = 0
    false_answers = 0
    most_common = ""

    # Compares the lists and stores the results for correct/incorrect answers
    for i in range(len(key_list)):
        if key_list[i] == student_list[i]:
            correct_list.append(i + 1)
            correct += 1
        elif key_list[i] != student_list[i]:
            incorrect_list.append(i + 1)
            incorrect += 1

    # Compares the lists and stores the results for true/false answers
    for i in range(len(student_list)):
        if student_list[i] == "T":
            true_answers += 1
        elif student_list[i] == "F":
            false_answers += 1
    
    # Compares the stored values and stores the most common answer type(s)
    if true_answers > false_answers:
        most_common = "T"
    elif false_answers > true_answers:
        most_common = "F"
    elif true_answers == false_answers:
        most_common = "T and F"

    # Calculates the percentage grade of the student
    grade = (correct / (correct + incorrect)) * 100

    # Defines the percentage to a letter grade
    if grade >= 90:
        grade_letter = "A"
    elif grade >= 80 and grade < 90:
        grade_letter = "B"
    elif grade >= 70 and grade < 80:
        grade_letter = "C"
    elif grade >= 60 and grade < 70:
        grade_letter = "D"
    elif grade < 60:
        grade_letter = "F"

    # Uses the required header
    PrintAnswerHeader(key_list, student_list)
    
    # Prints the results
    print("CORRECT answers: #", *correct_list)
    print("Number correct:", correct, "\n")
    print("WRONG answers: #", *incorrect_list)
    print("Number wrong:", incorrect, "\n")
    print("The student has", true_answers, "True answers.")
    print("The student has", false_answers, "False answers.")
    print("The student answered", most_common, "the most often.")
    print("\nThe student's average is", grade, "%.")
    print("The student's letter grade is:", grade_letter)
    print("\n")

main()
