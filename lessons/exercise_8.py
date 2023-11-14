# 8. Write python code to print numbers from the below list if they satisfy the following conditions:
#    - The number must be divisible by 5
#    - If the number is greater than 150, skip it and move to the next number (look up `continue` statement in python)
#    - If the number is greater than 500, stop the loop (look up `break` statement in Python)


numbers = [12, 75, 150, 180, 145, 525, 50]
# expected_output:
#     75
#     150
#     145

for num in numbers:
    if num > 500:
        break
    if num > 150:
        continue
    if num % 5 == 0:
        print(num)
  