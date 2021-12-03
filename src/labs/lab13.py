#  Author:          Anthony Segura
#  ULID/Section:    C00441031 - 002
#  lab13.py 

def CreateDistinctList(theList):
    distinct_list = []
    for i in theList:
        if i not in distinct_list:
            distinct_list.append(i)
    return distinct_list

def ReverseList(theList):
    reverse_list = []
    for i in CreateDistinctList(theList):
        reverse_list.insert(0, i)
    return reverse_list

def main():

    # open the file
    #infile = open("C:/Users/Anthony/Desktop/Stoof/CMPS 150/pythongit/src/labs/lab13_numbers.py", "r")
    infile = open("lab13_numbers.py", "r")

    # read the first data item
    num = eval(infile.readline().strip())

    # create an empty list
    num_list = []

    # while loop for sentinel control
    while num != 0:
        # process the data, which for this program is to append it to the list
        num_list.append(num)
        # read the next data item
        num = eval(infile.readline().strip())

    # print the list and length of the list
    print("\nOriginal List =", num_list)
    print("Original List Length =", len(num_list))

    # print the new distinct List
    print("\nDistinct List =", CreateDistinctList(num_list))

    # print the reversed list
    print("Reversed List =", ReverseList(num_list))
    print()
    
main()
