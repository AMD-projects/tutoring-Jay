# functions

# cost = [5, 6, 10, 9, 22, 4]

# def total_cost(x): #  total_cost(x: int) indicates that the function requires an integer
#     total = sum(x)
#     return total

# final_cost = total_cost(cost) * 5
# print(final_cost)

# pass by value
# def multiplyer(x, y):
#     x = x * y
#     return x
    
# x = 5

# result = multiplyer(x, 10)
# print(result, x)

# pass by reference
ingredients = ["eggs", "bacon", "muffin"]


str1 = "Pepper"
def cook(x, y, z = str1):
    x.append("Cheese")
    print(y)
    print(z)
    return "Omelette"

print(ingredients)
print(cook(ingredients, 10))
print(ingredients)