""" 
    TASK 3: 

    Create a function that takes two arrays as input parameters and returns a third array that combies the first two. 
    Example:
    MyStrangeFunction([1,2,3],["A","B","C"]) //-> [1,2,3,"A","B","C"]

    Remember that quality of code (naming, structure etc.) is important

"""

list1 = [1,2,3]
list2 = ["A","B","C"]
def mergeArrays(list1, list2):
    mergedList = [*list1, *list2]
   
    return mergedList


print(mergeArrays(list1, list2))