""" 
    TASK 2: 

    Write a function to calculate sum of digits using a loop. 
    example: 
    MyStrangeFunction(123) //-> 6
    MyStrangeFunction(417) //-> 12
    MyStrangeFunction(-12) //-> -3

    Remember that quality of code (naming, structure etc.) is important

"""
number = 123

def sumOfNumber(number):
    number = 987654321
    result = []
    for n in str(number):
	    result.append(int(n))
        
    return sum(result)

print (sumOfNumber(number))