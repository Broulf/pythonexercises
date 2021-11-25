# Author:         Anthony Segura
# ULID/Section:   C00441031 - 002
import random

def main():
    #infile = open("/home/broulf/Documents/VSCodeProjects/lab12/numbers.py", "r")
    infile = open("numbers.py", "r")

    num = eval(infile.readline().strip())

    num_list = []

    randomint = 0

    while num != 0:
        #print(num)
        num_list.append(num)
        num = eval(infile.readline().strip())

    randomint = random.randint(1, 25)

    print("List =", num_list)
    print("Length of list =", len(num_list))
    print("\nnewInt =", randomint, "\n")

    if randomint in num_list:
        print(randomint, "is already in the list ... not added!")
    else:
        print(randomint, "is NOT in the list ... it has been added!")
        num_list.append(randomint)

    print("\nList =", num_list)
    print("Length of list =", len(num_list))
    
    infile.close()

main()
