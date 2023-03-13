
""" 
    TASK 4: 

    Create a function that given a number returns an array with the frequenzy of the digits in the number.

    Example:
    MyStrangeFunction(123) //-> [0,1,1,1,0,0,0,0,0,0]
    MyStrangeFunction(81118) //-> [0,3,0,0,0,0,0,0,2,0]
    MyStrangeFunction(249226) //-> [0,0,3,0,1,0,1,0,0,1]


    Remember that quality of code (naming, structure etc.) is important
"""
number = 1234567869

def freqOfDigit(number):
    freqArray = [0] * 10 
    while number > 0:
        digit = number % 10 
        freqArray[digit] += 1 
        number //= 10 
    return freqArray

print(freqOfDigit(number))