""" 
    TASK 5: 

    Create a function that given a dimension (number for length and height) returns a square start pattern.

    Example:
    MyStrangeFunction(1) //->   *
    
    MyStrangeFunction(2) //->   **
                                **

    MyStrangeFunction(5) //->   *****
                                *****
                                *****
                                *****
                                *****


    Remember that quality of code (naming, structure etc.) is important
"""

SquareSize = 10

def squareMAKER(sqSize):
    for i in range(sqSize):
        for j in range(sqSize):
            print ("*", end=" ")
        print()

print(squareMAKER(SquareSize))