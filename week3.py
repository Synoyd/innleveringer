# // Task: Example (demonstrating how to complete a task)
# // Define the variable "puppyName" and instanciate it with the name Fido
puppyName = "Fido"

# // Task 1
# // Fix the following code

puppyAge = 4

# // Task 2
# // Define a variable "breed" of type String
puppyBreed = ("Labrador")

# // Task 3
# // Set the value of breed to Labrador Retriever
puppyBreed = ("Labrador retriever")

# // Task 4
# // Fix the following code

def concatinatePuppyInfo(puppyAge,puppyBreed,puppyName):
    return(puppyName, puppyAge, puppyBreed)


def dogAgeToHumanAge(puppyAge):
    humanAge = puppyAge*8
    return humanAge
print('task 1',puppyAge)
print('task 2',puppyName)
print('task 3',puppyBreed)

print('task 4', concatinatePuppyInfo(puppyAge, puppyBreed, puppyName))
print('task 5', dogAgeToHumanAge(puppyAge))