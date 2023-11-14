# Write a function called count_occurrences that takes a list of numbers and a target number as arguments. 
# The function should return the number of times the target number appears in the list.

numbers = [1, 4, 8, 2, 7, 9, 8, 10, 11, 12, 1, 2 , 3 ,7 ,2 , 0]

target = int(input("Please input a number: "))

def count_occurrences(numbers, target):
    """Counts the occurrences of a target number in a list."""
    result = numbers.count(target)
    print(result)

count_occurrences(numbers, target)    