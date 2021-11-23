def PrintAnswerHeader(keyList, answerList):
    # This function prints to the screen the answer key solutions
    # and the student's answers
    # Inputs:  a list containing the answer key
    #          a list of the student's answers
    # Return:  no value is returned

    # print problem numbers
    print ()
    print ("          ", end = '')
    for i in range (len(keyList)):
        print (i+1, end = '  ')


    #print ("\n----------------------------------------")
    # print the dashed line of varying length, dependent on number
    # of problems to display
    print()
    print ("----------", end="")
    for i in range (len(keyList)):
        print ("---", end="")
    print ()


    # print key answers    
    print ("Key    ", end = '   ')
    for i in range (len(keyList)):
        print (keyList[i], end = '  ')
        

    # print student answers
    print ()
    print ("Student", end = '   ')
    for i in range(len(answerList)):
        print (answerList[i], end = '  ')
    print ()
    print ()
