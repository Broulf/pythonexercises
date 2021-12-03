# Author:          Anthony Segura
# ULID:            C00441031
# Course/Section:  CMPS 150 – 002
# Assignment:      pa8 
# Date Assigned:   Sunday, November 28, 2021 
# Date/Time Due:   Thursday, December 2, 2021 –- 11:55 pm 
# 
# Description:    This program is an extension of pa7.  It reads an answer key  
#     from an input file and stores the data in a list. It then reads 
#    a file containing strings of several students’ answers. The 
#   students’ answers are compared to the key and various statistics 
#   computed.     
# 
# Certification of Authenticity: 
# I certify that this assignment is entirely my own work.

from PrintAnswerHeader import PrintAnswerHeader

def createStringList(list, file, sen):
        list += file.read().splitlines()
        list.remove(sen)
        return list

def main():

    #key_file = open("C:/Users/Anthony/Desktop/Stoof/CMPS 150/pythongit/src/pas/key.py", "r")
    #student_file = open("C:/Users/Anthony/Desktop/Stoof/CMPS 150/pythongit/src/pas/studentAnswersPA8.py", "r")
    key_file = open("key.py", "r")
    student_file = open("studentAnswers.py", "r")

    # Create a list to hold the key
    key_list = []
    createStringList(key_list, key_file, "X")

    # Create a list to hold the students' answers
    student = student_file.readline().strip()
    student_list = []

    # Storage Values!!
    student_number = 1
    correct = 0
    incorrect = 0
    correct_list = []
    incorrect_list = []
    true_answers = 0
    false_answers = 0
    most_common = ""
    class_total = 0
    highest_grade = 0
    lowest_grade = float('inf')

    while student != "END":

        # Creates the list of students' answers
        for i in range(len(student)):
            student_list += student[i]

        # Prints the header
        print("\n" + "*" * 39)
        print("Student", student_number, "Summary:")
        PrintAnswerHeader(key_list, student_list)

        # Compares the students answers to the key
        for i in range(len(key_list)):
            if key_list[i] == student_list[i]:
                correct += 1
                correct_list.append(i + 1)
            else:
                incorrect += 1
                incorrect_list.append(i + 1)
        
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

        # Prints the results
        print("CORRECT answers: #", *correct_list)
        print("Number correct: ", correct)
        print("\nWRONG answers: #", *incorrect_list)
        print("Number wrong: ", incorrect)
        print("\nThe student has", true_answers, "True answers.")
        print("The student has", false_answers, "False answers.")
        print("The student answered", most_common, "the most often.")
        print("\nThe student's average is", grade, "%.")
        print("The student's letter grade is:", grade_letter)

        # Stores a total, highest, and lowest grade of the class
        class_total += grade
        if grade > highest_grade:
            highest_grade = grade
        if grade < lowest_grade:
            lowest_grade = grade

        # Adds '1' to the student number
        student_number += 1

        # Resets the variables for the next student
        correct = 0
        incorrect = 0
        correct_list = []
        incorrect_list = []
        true_answers = 0
        false_answers = 0
        most_common = ""
        
        # Reads the next student
        student_list = []
        student = student_file.readline().strip()

    # Creates an average grade for the class
    class_average = class_total / (student_number - 1)

    # Prints the results of the class
    print("\n" + "*" * 39)
    print(format("Students:", '15s'), student_number - 1)
    print(format("Class Avg:", '15s'), format(class_average, '.2f'))
    print(format("Highest Grade:", '15s'), format(highest_grade, '.2f'))
    print(format("Lowest Grade:", '15s'), format(lowest_grade, '.2f'))
    print()

    # Closes the files, helps to prevent leaks in memory
    key_file.close()
    student_file.close()

main()
