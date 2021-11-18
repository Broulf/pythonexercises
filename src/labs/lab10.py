# Author:         Anthony Segura
# ULID/Section:   C00441031 - 002
# Lab #10

def main():
    
    # open the file
    infile = open("trees.txt", 'r')

    # print the column headings
    print("\nJob Type   Hrs/Trees    Cost")
    print("----------------------------")

    # read the first set of data
    job = infile.readline().strip()
    num = eval(infile.readline().strip())

    # base prices
    trim_hour = 80
    removal = 500

    # maximums
    max_cost = -1
    max_job = ""
    max_num = -1

    # minimums because this was easy and I got bored
    min_cost = float("inf")
    min_job = ""
    min_num = float("inf")

    # sentinel-controlled while loop
    while num != 0:

        if job == "TRIM":
            cost = num * trim_hour
        elif job == "REMOVE":
            cost = num * removal

        # maximums again
        if cost > max_cost:
            max_job = job
            max_num = num
            max_cost = cost
        
        # minimums again
        if cost < min_cost:
            min_job = job
            min_num = num
            min_cost = cost

        print(format(job, '6s'), format(num, '10d'), format(cost, '10d'))
        
        job = infile.readline().strip()
        num = eval(infile.readline())

    # print maximums
    print("----------------------------")
    print("\nMost Expensive Job")
    print(format(max_job, '6s'), format(max_num, '10d'), format(max_cost, '10d'))
    print("Least Expensive Job")
    print(format(min_job, '6s'), format(min_num, '10d'), format(min_cost, '10d'))
    print()

    # close file    
    infile.close()

main()
