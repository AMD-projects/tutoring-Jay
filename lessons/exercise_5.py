# 5. Write python code to get the maximum and minimum value from the example dictionary below. Print the key (name) and the value for the maximum and minimum


dict = {'Bob': 26, 'Sarah': 34, 'John':41, 'Mike': 19, 'Kyle': 92, 'Rob': 72}
# minimum: Mike 19
# maximum: Kyle 92

# get min and max values
min_val = min(dict.values())
max_val = max(dict.values())

# get min and max keys
max_key = max(dict, key=dict.get)
min_key = min(dict, key=dict.get)

print("minimum:", min_key, min_val) 
print("maximum:", max_key, max_val) 
