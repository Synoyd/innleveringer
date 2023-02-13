
# NB!! DO NOT CHANGE code as it is given, unless spesificly told to do so.

# Task: Example (demonstrating how to complete a task)
# Create a function that writes out all the names in the list, one name per line.
print("Task: Example")
people = ["Tony","Christian","Håkon"]

for person in people :
    print(person)


#    Task 1:
#    Create variables for the following cases:
#    * Houers in a day
#    * Minutes in an houer
#    * Seconds in a minute.
#    * The ratio between "saft" and water when mixing
#    * Days untill your birthday 
#    * mm of rain that falls in a day.

print("Task: 1")
hoursInDay = 24
minutesInHour = 60
secondsInMinute= 60
saftWaterRatio = 4/2
daysUntilBirthday = 99
mmRainPerDay = 15   #eg er fra vestlandet, forestillingen min av hvor mye regn som kommer er kanskje litt forvridd...


#    Task 2: 
#    Use your variables from task 1 (do not redeclear them) to do the following tasks
#    * Calculate how many seconds there are in 2.5 hours?
#    * Calculate how many minutes there are in 123 days?
#    Remember to allocate the results to a apropriate variable
#    Example:
#    # How many dl is 4.5 coups?
#    dlInCoups = 2.36588
#    numDl = dlInCoups * 4.5
#
print("Task 2:")
twoandhalfhour = secondsInMinute*minutesInHour*2.5
onethwothreedays = secondsInMinute*minutesInHour*hoursInDay*123
print(twoandhalfhour)
print(onethwothreedays)

#
#    Task 3:
#    Use a loop (for) to write out the numbers from 1 to 10

print("Task 3:")
for i in range(1,11):
    print(i)

#    Task 4: 
#    Use a loop (for) to write out the numbers from 10 to 1

print("Task 4:")

for y in range(10, 0, -1):
    print(y)


#    Task 5:
#    This is a bit more complicated, but you can do it :)
#    Use a loop (for) to write out the *even numbers* from 1 to 100

print("Task 5:")
for i in range(0,101,2):
    print(i)



#    Tak 6:
#    Change the code so the following code works as intended. 

print("Task 6:")

DICTIONARY_ML = {
        "hello":"Hei på deg",
        "howAreYou":"hvordan står det til?",
        "goodQuestionsLately":"Fått noen gode spørsmål i det siste?"
    }

print(f'{DICTIONARY_ML["hello"]} Christian {DICTIONARY_ML["howAreYou"]}') #-> Hei på deg Christian, hvordan står det til?
print(f'{DICTIONARY_ML["goodQuestionsLately"]}') #-> Fått noen gode spørsmål i det siste?



#    Task 7:
#    Change the code so the following code works as intended. 

print("Oppgave: G")

DICTIONARY_ML = {
    "no":{
        "hello":"Hei på deg",
        "howAreYou":"hvordan står det til?",
        "goodQuestionsLately":"Fått noen gode spørsmål i det siste?"
    },
    "en":{
        "hello":"Hi hello",
        "howAreYou":"How are you today?",
        "goodQuestionsLately":"Gotten any good questions lately??"
    }
}


print(f'{DICTIONARY_ML["en"]["hello"]} Christian {DICTIONARY_ML["en"]["howAreYou"]}') #-> Hi Christian, how are you?
print(f'{DICTIONARY_ML["en"]["goodQuestionsLately"]}') #-> Gotten anny good questions latly?