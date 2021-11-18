# Author:         Your-Name
# ULID/Section:   Your-ULID & section-number go here
# lab11.py 
 
import math

def AC(radius):
    area = math.pi * radius ** 2
    return area 
 
# WRITE ALL THE OTHER FUNCTIONS 
 
 
 
 
 
def main():

    infile = open("lab11_input.py","r")

    # get first calculation type,
    # but wait on dimension(s) because number of dimensions
    # is dependent on type of shape

    type = infile.readline().strip()
    dimension = eval(infile.readline().strip())

    while (type != "###"): 

        if (type == "AC"):

            # call the function AC and pass radius as a parameter
            # the return value from the function AC will be stored in circleArea

            circleArea = AC(dimension)
            print(format("Area of a Circle","30s"),format(circleArea,"15.2f"))
 

        # do the processing for all other types of calculations 
        elif 
 
 
        # get next calculation type
        type = infile.readline().strip()
        dimension = eval(infile.readline().strip())


    # close the file when you exit the while loop 
    infile.close()
    
main() 
