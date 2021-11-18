# Author:          Anthony Segura
# ULID:            C00441031
# Course/Section:  CMPS 150 – 002
# Assignment:      pa6 
# Date Assigned:   Wednesday, November 10, 2021 
# Date/Time Due:   Monday, November 15, 2021 –- 11:59 pm 
# 
# Description:     This program calculates a hospital bill.  It uses room type,  
#                  as well as cable and hospitality room options. 
# 
# Certification of Authenticity: 
# I certify that this assignment is entirely my own work.

def main():

    # open the file
    infile = open("hospital.txt", 'r')

    # print the header
    print(
        format("\nName", '20s'), 
        format("Room Type", '17s'), 
        format("Cost", '11s'), 
        format("Cable", '7s'), 
        format("Hospitality Rm"),
        )
    print("-" * 73)

    # read the file
    name = infile.readline().strip()
    num_days = eval(infile.readline().strip())
    room_type = infile.readline().strip()
    cable = infile.readline().strip()
    hospitality = infile.readline().strip()

    # calculate the totals
    total_cost = 0
    total_cable = 0
    total_hospitality = 0

    # costs
    private_room = 950.00
    semi_private_room = 695.00
    deluxe_cable = 24.50
    hospitality_charge = 15.00

    while name != "END":

        # calculate the cost for the room
        if room_type == "P":
            room_type = "Private"
            cost = private_room * num_days
            total_cost += cost
        else:
            room_type = "Semi-Private"
            cost = semi_private_room * num_days
            total_cost += cost
        
        # calculate the cost for the cable
        if cable == "Y":
            cable = deluxe_cable * num_days
            if cable < 300:
                total_cable += cable
            elif cable > 300:
                cable = 300.00
                total_cable += cable
        elif cable == "N":
            cable = 0

        # calculate the cost for the hospitality
        if hospitality == "Y" and room_type == "Semi-Private":
            hospitality = hospitality_charge * num_days
            if hospitality < 300:
                total_hospitality += hospitality
            elif hospitality > 300:
                hospitality = 300.00
                total_hospitality += hospitality
        else:
            hospitality = 0.00

        # debug
        #print(name, room_type, cost, cable, hospitality)
        print(
        format(str(name), '19s'), 
        format(str(room_type), '17s'), 
        format(str(format(cost, '.0f')), '11s'), 
        format(str(format(cable, '.2f')), '13s'), 
        format(str(format(hospitality, '.2f')), '^s')
        )

        # read the next lines
        name = infile.readline().strip()
        num_days = eval(infile.readline().strip())
        room_type = infile.readline().strip()
        cable = infile.readline().strip()
        hospitality = infile.readline().strip()

    print("-" * 73)
    print(
        format("Totals", '37s'), 
        format(str(format(total_cost, '.0f')), '11s'), 
        format(str(format(total_cable, '.2f')), '13s'),
        format(format(total_hospitality, '.2f'), '>3s'),
        "\n"
        )
    
    infile.close()

main()
