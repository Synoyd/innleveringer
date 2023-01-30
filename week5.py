# NB!! DO NOT CHANGE code as it is given, unless spesificly told to do so.
# Task: Example (demonstrating how to compe a task)
# Create a function that returns the circumference of a circle given the radius
def calculateCircumference(radius) :
  return 2 * math.pi * radius

# Task 1
# Output "good" if isBanana is true
isBanana = False
if isBanana == True:
    print ('good')

# Task 2
# Output "monkey sad" if isBanana is false, but "good" if true
if isBanana == True:
    print ('good')
elif isBanana == False:
    print ('monkey sad')

# Task 3
# Output "hmmm" if isBanana is not true or false, but "good" if true, and "monkey 
if isBanana == True:
    print ('good')
elif isBanana == False:
    print ('monkey sad')
else:
    print ('hmmm')


# Task 4
# if isBanana and isPrimate then output, "Eating that banana".
isPrimate = True
if isBanana & isPrimate == True :
    print ('Eating that banana')

# Task 5
# if isBanana or isPrimate then output, "Everything is fine"
if isBanana or isPrimate == True:
    print ('Everything is fine')

# Task 6
# if not isBanana and not isPrimate then output, "Ooops."
isBanana = isPrimate = False
if not isBanana & isPrimate == True:
    print ('Ooops')

# Task 7
# Fix the following code
# NB! 
# * This will requier you to make judgments about what is god or bad.
# * This will requier you to think about the safty of the code. 
def shorten(name):
  return name.split(" ")[0][0,3] + ". " + name.split(" ")[1]
ShortenedName = shorten("Christian Simonsen")
print(ShortenedName)