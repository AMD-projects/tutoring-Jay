# Additional Python Exersizes

# 1. Given a list, write the code to swap the first and last element of the list. The code must work for a list of any 
# size and order
# ```angular2html
list_original = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# expected output: [10, 2, 3, 4, 5, 6, 7, 8, 9, 1]
# ```

place_holder = list_original[-1]
print(place_holder)
list_original[-1] = list_original[0]
list_original[0] = place_holder
print(list_original)
# list_original[-1] = list_original[1]
# print(list_original)