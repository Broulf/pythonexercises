# Author:          Anthony Segura
# ULID:            C00441031
# Course/Section:  CMPS 150 – 002
# Assignment:      pa5 
# Date Assigned:   Friday, October 29, 2021 
# Date/Time Due:   Saturday, November 6, 2021 –- 11:55 pm 
# 
# Description:    This program reads ISBN numbers from an input file and  
#   determines if the number is valid.  Results are displayed in a  
#   formatted table.   
# 
# Certification of Authenticity: 
# I certify that this assignment is entirely my own work. 

infile = open("C:/Users/Anthony/Desktop/Stoof/CMPS 150/assignments/ISBNdata.txt","r")
#infile = open("ISBNdata.py","r")

isbn_number = infile.readline().strip()

print(format("ISBN", '15s'), format("#Digits", '10s'), format("Check#", '11s'), format("Sum", '5s'), "Validity")
print("-" * 54)

while isbn_number != '-1':

    for i in range(len(isbn_number)):
        if len(isbn_number) == 10 and isbn_number[9] != 'X':
            check_num = isbn_number[9]
            isbn_sum = (int(isbn_number[0]) * 1) + (int(isbn_number[1]) * 2) + (int(isbn_number[2]) * 3) + (int(isbn_number[3]) * 4) + (int(isbn_number[4]) * 5) + (int(isbn_number[5]) * 6) + (int(isbn_number[6]) * 7) + (int(isbn_number[7]) * 8) + (int(isbn_number[8]) * 9) + (int(isbn_number[9]) * 10)
            isbn_valid = isbn_sum % 11
            if isbn_valid == 0:
                isbn_validity = "Valid"
            else:
                isbn_validity = "Not Valid"
        elif len(isbn_number) == 10 and isbn_number[9] == 'X':
            check_num = isbn_number[9]
            isbn_sum = (int(isbn_number[0]) * 1) + (int(isbn_number[1]) * 2) + (int(isbn_number[2]) * 3) + (int(isbn_number[3]) * 4) + (int(isbn_number[4]) * 5) + (int(isbn_number[5]) * 6) + (int(isbn_number[6]) * 7) + (int(isbn_number[7]) * 8) + (int(isbn_number[8]) * 9) + (10 * 10)
            isbn_valid = isbn_sum % 11
            if isbn_valid == 0:
                isbn_validity = "Valid"
            else:
                isbn_validity = "Not Valid"
        elif len(isbn_number) == 13:
            check_num = isbn_number[12]
            isbn_sum = (int(isbn_number[0]) * 1) + (int(isbn_number[1]) * 3) + (int(isbn_number[2]) * 1) + (int(isbn_number[3]) * 3) + (int(isbn_number[4]) * 1) + (int(isbn_number[5]) * 3) + (int(isbn_number[6]) * 1) + (int(isbn_number[7]) * 3) + (int(isbn_number[8]) * 1) + (int(isbn_number[9]) * 3) + (int(isbn_number[10]) * 1) + (int(isbn_number[11]) * 3) + (int(isbn_number[12]) * 1)
            isbn_valid = isbn_sum % 10
            if isbn_valid == 0:
                isbn_validity = "Valid"
            else:
                isbn_validity = "Not Valid"
        elif len(isbn_number) < 10:
            check_num = "N/A"
            isbn_sum = "N/A"
            isbn_validity = "Not Valid"

        print(format(isbn_number, '18s'), format(str(len(isbn_number)), '10s'), format(str(check_num), '8s'), format(str(isbn_sum), '6s'), isbn_validity)
        isbn_number = infile.readline().strip()

infile.close()
