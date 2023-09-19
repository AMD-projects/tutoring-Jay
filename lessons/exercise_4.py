# 4. Write python code to check if a key already exists in a dictionary. The key you want to check is 'John' in the below example
#    - Sub-question: Can there exist identical keys in the dicitonary? 

original_dictionary = {'Bob': 26, 'Sarah': 34, 'John':41, 'Mike': 19}
# expected_output = True (key exists in the dictionary)

# print(original_dictionary.keys() == 'John')

# A variable outside of the loop is changed by something inside of the loop (good for search problems!)
key_found = False

for name in original_dictionary.keys():
    if name == 'John':
        key_found = True
        break # exit the loop if a condition has been found
print(key_found)
