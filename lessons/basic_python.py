# 1. Write a program that asks the user for their name and age, and then prints a message that says "Hello, [name]! You are [age] years old."

# name = input("What is your name: ")
# age = input("What is your age: ")
# print("Hello, " + name)
# print("Your are, " + age, "years old.")

# 2. Write a program that asks the user to enter two numbers and then prints the sum, difference, product, and quotient of the two numbers.

# num1 = int(input("Input a number: "))
# num2 = int(input("Input another number: "))

# print(num1 + num2)
# print(num1 - num2)
# print(num1 * num2)
# print(num1 / num2)

# 3. Write a program that asks the user to enter a temperature in Fahrenheit and then converts it to Celsius using the formula C = (F - 32) * 5/9. Print the result with two decimal places. 
# temp = int(input("Input a number: "))

# C = (temp - 32) * 5/9
# print(round(C, 2))

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# nums = 0
# for number in numbers:
#     if number % 2 == 0:
#         nums += number
# print(nums)

# nums = []
# for number in numbers:
#     if number % 2 == 0:
#         nums.append(number)
# print(nums)
# print(sum(nums))

# var1 = "Python is weird"
# print(var1[0:6])

# #this makes it go in reverse
# var2 = var1[::-1]
# print(var2)

# dict1 ={"Jay" : {"Age": 36, "Occupation": "UoC", "Location": "England"}, "Travis": 22, "Penny": 8}
# matrix = [[1,2,3],
#           [4,5,6]]

# print(matrix[:][0])

#  4. Write a program that asks the user to enter a string and then prints the string reversed.

# str1 = input("Please enter some text: ")
# rev_str1 = str1[::-1]
# print(rev_str1)

# 5. Write a program that generates a random number between 1 and 100 and then asks the user to guess the number. 
# If the user's guess is too high, the program should print "Too high!" If the user's guess is too low, the program should print "Too low!" 
# If the user's guess is correct, the program should print "Congratulations, you guessed the number!"

#### Part 2 ####

# 1. Write a program that takes a list of integers as input and outputs the sum of all the even numbers in the list. 
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# nums = []
for num in numbers:
    if num % 2 == 0:
        nums.append(num) # why don't I have to use 'if' 'then'?
print(sum(nums))

# 2. Write a program that takes a list of strings as input and outputs the number of strings that start with the letter "a".

fruits = ["apple", "banana", "cherry", "orange", "pineapple", "grapefruit"]
for fruit in fruits:
    if fruit[-1] == "e":
        print(fruit)
   

# Create a dictionary of names and ages
ages = {"Alice": 25, "Bob": 30, "Charlie": 35}

# Add a new key-value pair to the dictionary
ages["David"] = 40 # Why is 'David in a list format?
print(ages)

# in dictionaries is the word name like i (for index in for loops)? Does this mean that name is essentially a call for the key value?
key_list = []
value_list = []
name_list = ["Alice", "Charlie"]

# 'name' takes on the datatype of the element in the loop, in the case string
for name in name_list: # access to name_list
    name_value = ages[name]
    value_list.append(name_value) # name is the dict key
    print(name)

print(value_list)

