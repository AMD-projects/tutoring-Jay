# 6. Print the below list in reverse order using a for loop

list1 = [10, 20, 30, 40, 50]
# expected_output = [50, 40, 30, 20, 10]

# empty list
list2 = []

# start, stop, and step in range() function
for i in range(len(list1) -1, -1, -1):
    list2.append(list1[i]) # add values to list2
print(list2)

print(list1[::-1])
