# NB!! DO NOT CHANGE code as it is given, unless spesificly told to do so.
# Task: Example (demonstrating how to complete a task)
# Create a function that writes out all the names in the list, one name per line.
from datetime import datetime
print("Task: Example")
people = ["Tony", "Christian", "Håkon"]
for person in people:
    print(person)
    

#    Task 1:
#    The following code has errors, pleace fix the mistakes.
#    AND add a comment behind explaining your change

#    # Example:
#    pi = 3.14
#    # changed to
#    const PI = 3.14 # pi represent the ratio of a circle's circumference to its diameter, it does not change so it is a CONSTANT

print("Task 1:")

USER_NAME = "haxor_56"
GOLDEN_RATIO = 1.618033988749
currentTimeOfDay = datetime.now() #datetime was redundant having datetime.datetime.now so i removed one of the datetimes

#    Task 2:
#    Decleare the variables and constants you would need to do the following.
#    Calculate the Average, the Median and the Sum of this list :
print("Task 2:")

numbers = [97,45,34,33,86,93,52,41,1,85,6,15,60,53,86,0,93,57,13,8,83,24,34,39,45,60,83,34,71,60,11,35,34,54,6]
sumOfNumbers = 0
mini = min(numbers)
maxi = max(numbers)
#    Then calculate the Average, the Median and the sum using your variables.
def findSum(myList):
    sumOfNumbers = 0
    for number in myList:
        sumOfNumbers = sumOfNumbers + number
    return sumOfNumbers
def findAverage(myList):
    sumOfNumbers = 0
    for number in myList:
        sumOfNumbers = sumOfNumbers + number
    average = sumOfNumbers/len(myList)
    return average

print((mini+maxi)/2)
print(findAverage(numbers))
print(findSum(numbers))

#    Task 3:
#    Present the following statment as code
#    Tony has 5 apples and Christian has 3, combinde they have 5+3 = 8 apples

print("Task 3:")
TonyApples = 5
ChristianApples = 3
CombinedApples = TonyApples + ChristianApples
print( CombinedApples)

#    Task 4:
#    Use exactly one for loop to find the largest and smalest numbers in the give array.
#    Output the smalest and largest number.
print("Task 4:")
DATA = [86.02, 41.74, 80.42, 49.94, 28.96, 72.23, 77.41, 40.01, 61.63, 37.67, 
59.34, 22.06, 18.87, 1.80, 42.60, 68.40, 79.10, 93.33, 25.92, 19.79, 91.19, 11.78, 
63.68, 5.04, 41.66, 63.62, 41.16, 27.46, 21.72, 68.90, 38.03, 76.78, 90.11, 51.01, 
80.35, 9.24, 80.79, 60.05, 15.76, 25.74, 61.92, 50.02, 2.09, 69.96, 21.02, 35.61, 
31.13, 88.73, 29.68, 75.07, 47.28, 43.28, 36.52, 49.72, 72.97, 82.16, 72.32, 59.00, 
53.73, 86.04, 10.65, 9.66, 89.93, 74.16, 96.50, 26.35, 60.33, 8.15, 94.43, 41.80, 
20.04, 86.94, 60.87, 52.41, 35.15, 41.01, 16.87, 52.09, 30.77, 75.27, 87.54, 82.27, 
54.43, 17.25,43.72, 1.99, 59.32, 81.91, 91.02, 14.48, 97.49, 45.07, 73.58, 52.00, 
17.33, 93.74, 86.00, 28.96, 47.53, 17.36]


minimum = maximum = DATA[0]
for number in DATA[1:]:
    if number < minimum:
        minimum = number
    elif number > maximum:
        maximum = number

print("The minimum number is:", minimum)
print("The maximum number is:", maximum)

# uten for loop er dette så mye lettere.
# print(min(DATA))
# print(max(DATA))



#   Task 5:
#   Create a function that calculates the hypotenuse length in a right-angled triangle,
#   given the length of the two opposing sides. i.e. Implement the Pythagorean theorem as a function

print("Task 5:")

def pythagoras(smallside1, smallside2):
    smallside1doubled = smallside1**2
    smallside2doubled = smallside2**2
    longsideDoubled = smallside1doubled+smallside2doubled
    longsideLength = longsideDoubled/2
    return longsideLength

print(pythagoras(4,8))


# Task 6:
# Use the following descriptions to create a function that returns the propper greeting for the current time of day.

#  morgen: etter kl 06 - 09
#  formiddag: kl 09 - 12
#  ettermiddag: kl 12 - 18
#  kveld: kl 18 - 24
#  natt: kl 00 - 06
#  i.e. if the time is between 18:00 and 24:00 the function should return "Good kveld"
#  For info about dates and time in Python :http://bit.ly/3IgUGUj

print("Task 6:")
from datetime import datetime

current = datetime.now()

hour = current.hour

def hilsenPåDagen(hour):
    if hour >= 6 and hour < 9:
        print("Good morning")
    elif hour >= 9 and hour < 12:
        print("god formiddag")
    elif hour >= 12 and hour < 18:
        print("god ettermiddag")
    elif hour >= 18 and hour < 24:
        print("god kveld")
    elif hour >= 0 and hour < 6:
        print("god natt og sov godt <3")

hilsenPåDagen(hour)