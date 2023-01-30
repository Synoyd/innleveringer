# Task: Example (demonstrating how to complete a task)Orozco
# # Create a function that returns the circumference of a circle given the radius
# def calculateCircumference(radius) :
#   return 2 * math.pi * radius

# # Task 1
# # Create a list (array) "people" and populate it with the names from 
# # httpeople:#github.com/MM-203/misc/blob/main/text/names.txt
people = ['Benedict Thompeopleon','Lennon Kline','Trinity Cox', 'Angela Willis','Oliwia Walter','Halle Orozco','Gregory Carrillo','Leyla Dalton','Roosevelt Harrington','Antonia Aguilar']

# # Task 2
# # Output all the names in the list people
print ("Task 2", people)

# # Task 3
# # Output only the longest name in the list people

def Sorting(people):
    people.sort(key=len)
    return people

print('Task 3', Sorting(people)[9])

# # Task 4
# Output all the names in alphabetical order.
people.sort(key=str.lower)
print('Task 4', people)

# # Task 5
# # Output all the names in order from longest to shortest last name.
def sortLastnames(nameList):
    nameList.sort(key=lambda x: len(x.split()[-1]), reverse=True)

    return nameList

print ("Task 5", sortLastnames(people))

# NB! last name (not full name)

# Task 6
# Fix the following code
def splitFirstAndLastName(nameList):
  nameList = []
  for i in len:
    nameList.append(people[i].split(" ")[0])
    nameList.append(people[i].split(" ")[1])
  return nameList

people = splitFirstAndLastName(people)
print("Task 6", people)
