# The point of this assignment is not to use the functional elements that are part 
# of your chosen language (JavScript/Python).
# But, rather, implement the functionality from scratch using pure functions and 
# higher level functions.
# Do the implimentation in order as given. 
# We have linked to info at MDN, this is just to give a sence of how the reduce,forEach,map and filter functions should work.

#   Prerequisite:🛠️
# You must create an array persons that will contain the data from https:#raw.githubusercontent.com/MM-203/misc/main/data/data.json
# This must be done before the first task

-----------------------------------------------------------------------------------
-----------------------------------------------
# Bonus challenge (a bit hard), the functions forEach, filter and map can all be created using the function reduce. 
# If you feel up for a challenge, try doing so. NB! The bonus challenge is optional. 
# 
-----------------------------------------------------------------------------------
-----------------------------------------------
peopleInfo = [
    {"name":"Paula Key", "age":23},
     {"name":"Riya Dickerson" , "age":99},
     {"name":"Layne Colon" , "age":53},
     {"name":"Pranav Giles" , "age":51},
     {"name":"Kamryn Davis" , "age":27},
     {"name":"Taniyah Yu" , "age":17},
     {"name":"Brendon Porter" , "age":23},
     {"name":"Jordin Hancock" , "age":86},
     {"name":"Shawn Vargas" , "age":88},
     {"name":"Sawyer Copeland" , "age":14},
     {"name":"Gustavo Baldwin" , "age":7},
     {"name":"Renee Wilson" , "age":29}
]
# 1
# Implement your own reduce function and count the number of people above the age of 50
# You can read about a reduce function 
# https:#developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/reduce 

# 2
# Implement your own forEach function and use it to greet all the people in the 
# persons array (say Hi, persons name).
# Read about forEach 
#https:developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/forEach

# 3
# Implement your own map function and make everyone a year older.
# You can read about what the map function should do 
#https:developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/map 

# 4
# Implement your own filter function, and use it to find evryone under the drinking age.
# Read about filter 
#https:#developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/filter

# 5
# Now create a function sum, that takes a list of numbers and returns the sum
# Try to use your previously created functions to make this function 
# Sum the total age of persons using this new function 
# NB! Do not manualy create the age listing

# 6
# Now create a function average, that returns the average of a list of numbers
# Try to use your previously created functions to make this function 
# calculate the average age of the persons using this function
# NB! Do not manualy create the age listing

# 7
# Finaly create a max and a min function that respectivly returns the maximum value
# and the minimum value
# Only use previously created functions to acchive this.
# Then find the min and max age of ther persons.